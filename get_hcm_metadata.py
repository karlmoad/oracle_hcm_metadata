import json
import urllib.request
from bs4 import BeautifulSoup
import os
import threading
import queue

version = "22b"
root_output_dir="/Users/Karl/Documents/data/alation/oracleHCM"
base_uri = "https://docs.oracle.com/en/cloud/saas/human-resources/{}/oedmh/".format(version)


def find_output_dir(ver, root_dir):
    ext = ""
    counter = 0
    # determine output dir
    while True:
        tmp = "{}/{}{}".format(root_dir, ver, ext)
        if os.path.isdir(tmp):
            counter = counter + 1
            ext = "-{}".format(counter)
        else:
            os.mkdir(tmp)
            return tmp


def extract_view_sql(section):
    statements = []
    if section is not None:
        body = section.find('tbody', {'class': 'tbody'})
        if body is not None:
            lines = body.find_all('p', {'class': 'p'})
            for line in lines:
                statements.append(line.text)
        else:
            return None
    else:
        return None

    return statements


def extract_table_columns(section):
    columns = []
    if section is not None:
        body = section.find('tbody', {'class': 'tbody'})
        if body is not None:
            pos = 1
            for column in body.find_all('tr', {'class': 'row'}):
                parts = column.find_all('td')
                if len(parts) >= 6:
                    col_data = {'name': parts[0].text, 'nullable': len(parts[4].text.strip()) == 0, 'comments': parts[5].text, 'position': pos}
                    dt = parts[1].text.strip()
                    dtl = parts[2].text.strip()
                    dtp = parts[3].text.strip()

                    if len(dtl) == 0 and len(dtp) == 0:
                        col_data['type'] = dt
                    else:
                        if len(dtp) == 0:
                            col_data['type'] = "{}({})".format(dt, dtl)
                        else:
                            col_data['type'] = "{}({},{})".format(dt, dtl, dtp)

                    columns.append(col_data)
                    pos = pos + 1
                else:
                    return None
        else:
            return None
    else:
        return None

    return columns


def process_document(section, uri, output):
    data = {"section": section}
    output.append(data)

    req = urllib.request.urlopen(uri)
    page = BeautifulSoup(req.read().decode("utf8"), 'html.parser')
    req.close()

    page_article = page.find('article')
    e_name = page_article.find('header').find('h1')
    if e_name is None:
        data["error"] = "Error: Unable to extract header: name from [{}] uri: {}".format(section, uri)
        return

    e_body = page_article.find('div', {'class': 'body'})
    if e_body is None:
        data["error"] = "Error: Unable to extract header: body from [{}] uri: {}".format(section, uri)
        return

    e_desc = e_body.find('p', {'class': 'p'})
    if e_desc is None:
        data["error"] = "Error: Unable to extract header: desc from [{}] uri: {}".format(section, uri)
        return

    data["name"] = e_name.text
    data["description"] = e_desc.text

    sections = e_body.find_all('section', {'class': 'section'})
    if len(sections) > 0:
        details = sections[0]
        attr = details.find('ul').find_all("li")
        if len(attr) >= 3:
            details = sections[0]
            tpe = attr[2].find('p').text
            tpe = tpe[tpe.index(':') + 1:].strip()
            data["type"] = tpe

            schema = attr[0].find('p').text
            data['schema'] = schema[schema.index(':')+1:].strip()

            owner = attr[1].find('p').text
            data['owner'] = owner[owner.index(':')+1:].strip()

            if tpe == 'TABLE':
                cols = extract_table_columns(sections[2])
                if cols is not None and len(cols) > 0:
                    data['columns'] = cols
                else:
                    data["error"] = "Error extracting columns from ({}) uri: {}".format(section, uri)
                    return

            if tpe == 'VIEW':
                vsql = extract_view_sql(sections[3])
                if vsql is not None and len(vsql) > 0:
                    data["query"] = vsql
                else:
                    data["error"] = "Error extracting view info from ({}) uri: {}".format(section, uri)
                    return
        else:
            data['error'] = "Invalid object attribute info structure from [{}] uri:{}".format(section, uri)
            return
    else:
        data["error"] = "Error: Unable to extract body section elements from [{}] uri: {}".format(section, uri)
        return

    return


def process(root):
    buffer = urllib.request.urlopen("{}toc.htm".format(root))
    idx = BeautifulSoup(buffer.read().decode("utf8"), 'html.parser')
    buffer.close()
    output = []

    q = queue.Queue(maxsize=0)

    article = idx.find('article')
    in_section = False
    section = ''
    for tag in article.children:
        if tag.name == 'h2':
            if tag.text != '1 Overview':
                section = tag.text[tag.text.index(' '):].strip()
                in_section = True

        if tag.name == 'ul' and in_section:
            for item in tag.findChildren('a', href=True):
                q.put((section, "{}/{}".format(root, item['href'])))

    while not q.empty():
        depth = q.qsize()
        print("Queue Depth: {}".format(depth))
        threads = []
        for _ in range(min(depth, 20)):
            itm = q.get()
            print("Submitting for processing {} , uri: {}".format(itm[0], itm[1]))
            threads.append(threading.Thread(target=process_document, args=(itm[0], itm[1], output)))

        for t in threads:
            t.start()

        for t in threads:
            t.join()

    return output


def main():
    out = process(base_uri)
    jzon = {"uri": base_uri, 'version': version, 'objects': out}
    fname = "{}/{}.json".format(find_output_dir(version, root_output_dir), version)
    with open(fname, 'w') as f:
        f.write(json.dumps(jzon))


if __name__ == '__main__':
    main()
