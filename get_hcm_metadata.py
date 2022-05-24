import json
import urllib.request
from bs4 import BeautifulSoup
import os
import re

version = "22b"


def find_output_dir(ver):
    output_path_root = "/Users/Karl/Documents/data/alation/oracleHCM"
    ext = ""
    counter = 0
    # determine output dir
    while True:
        tmp = "{}/{}{}".format(output_path_root, version, ext)
        if os.path.isdir(tmp):
            counter = counter + 1
            ext = "-{}".format(counter)
        else:
            return tmp

def extract_view_sql(section):
    statements = []
    # if section is not None:
    #     lines = section.find('tbody', {'class': 'tbody'}).find_all('p', {'class': 'p'})
    #     for line in lines:
    #         statements.append(line)

    return statements

def extract_table_columns(section):
    columns = []
    if section is not None:
        body = section.find('tbody', {'class': 'tbody'})
        if body is not None:
            for column in body.find_all('tr', {'class': 'row'}):
                parts = column.find_all('td')
                if len(parts) >= 6:
                    col_data = {'name': parts[0].text, 'nullable': len(parts[4].text.strip()) == 0, 'comments': parts[5].text}
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
        return columns

def process_document(section, uri):
    data = {"section": section}

    req = urllib.request.urlopen(uri)
    page = BeautifulSoup(req.read().decode("utf8"), 'html.parser')
    req.close()

    page_article = page.find('article')
    name = page_article.find('header').find('h1').text
    body = page_article.find('div', {'class': 'body'})
    desc = body.find('p', {'class': 'p'}).text

    data["name"] = name
    data["description"] = desc

    sections = body.find_all('section', {'class': 'section'})
    if len(sections) > 0:
        details = sections[0]
        tpe = details.find('ul').find_all("li")[2].find('p').text
        tpe = tpe[tpe.index(':')+1:].strip()
        data["type"] = tpe

        if tpe == 'TABLE':
            data['columns'] = extract_table_columns(sections[2])

        if tpe == 'VIEW':
            data["query"] = extract_view_sql(section[4])

    return data


output_path = find_output_dir(version)
os.mkdir(output_path)

root = "https://docs.oracle.com/en/cloud/saas/human-resources/{}/oedmh/".format(version)

buffer = urllib.request.urlopen("{}toc.htm".format(root))
idx = BeautifulSoup(buffer.read().decode("utf8"), 'html.parser')
buffer.close()

article = idx.find('article')
ctr = 0
in_section = False
section = ''
for tag in article.children:
    if tag.name == 'h2':
        if tag.text[0] != '1':
            section = tag.text[tag.text.index(' '):].strip()
            in_section = True

    if tag.name == 'ul' and in_section:
        for item in tag.findChildren('a', href=True):
            ctr = ctr + 1
            obj_data = process_document(section, "{}/{}".format(root, item['href']))
            sData = json.dumps(obj_data)
            if len(sData.strip()) > 0:
                filename = "{}/{}.json".format(output_path, obj_data['name'])
                with open(filename, 'w') as outfile:
                    outfile.write(sData)
    print('.', end='')

print("Extracted : {} objects".format(ctr))
