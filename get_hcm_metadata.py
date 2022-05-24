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


def process_document(section, uri):
    print(section)
    print("-----------")
    page = urllib.request.urlopen(uri)
    print(page.read().decode("utf8"))
    page.close()
    print("-----------")

output_path = find_output_dir(version)

root = "https://docs.oracle.com/en/cloud/saas/human-resources/{}/oedmh/".format(version)

buffer = urllib.request.urlopen("{}toc.htm".format(root))
idx = BeautifulSoup(buffer.read().decode("utf8"), 'html.parser')
buffer.close()

article = idx.find('article')
itot = 2
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
            if ctr <= itot:
                ctr = ctr + 1
                process_document(section, "{}/{}".format(root, item['href']))

