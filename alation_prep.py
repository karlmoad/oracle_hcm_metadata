import json
import re
from mo_sql_parsing import parse

schema = {}

tables = []
columns = []
views = []
data = {}

root_dir = '/Users/karl/Documents/data/alation/oracleHCM'

with open('{}/22b-2/22b.json'.format(root_dir), 'r') as file:
    data = json.loads(file.read())

def extract_schema_structure(obj):
    if 'name' in obj:
        schema[obj['name'].upper()] = {}
        schema[obj['name'].upper()]['x_re_pattern'] = re.compile(obj['name'].upper(), re.IGNORECASE)

        if 'columns' in obj:
            for c in obj['columns']:
                if 'name' in c and 'type' in c:
                    schema[obj['name'].upper()][c['name'].upper()] = re.compile(c['name'].upper(), re.IGNORECASE)


def tokenizer(statement):
    tokens = []
    statement = statement.upper()
    buffer = ''
    pos = 0
    while True:
        if pos+1 > len(statement) -1:
            break

        tmp = statement[pos: pos+1]
        if tmp in [' ', ',']:
            tokens.append(buffer)
            buffer = ''
        else:
            buffer = buffer + tmp

        pos = pos + 1

    return tokens

def process_view(obj):
    if 'query' in obj:
        obj['statement'] = ' '.join(obj['query'])
        obj['parts'] = find_sql_objects_pass1(obj['statement'])
        views.append(obj)


def process_table(obj):
    table = {}
    if 'name' in obj and 'schema' in obj and 'columns' in obj:
        table['key'] = "{}.{}".format(obj['schema'], obj['name']).upper()
        table['title'] = obj['name'].upper()
        table['description'] = obj['description']
        table['table_type'] = 'TABLE'
        if 'section' in obj:
            table['table_comment'] = "Scope: {}".format(obj['section'], obj['owner'])
        if 'owner' in obj:
            tmp = ''
            if 'table_comment' in table:
                tmp = "{},".format(table['table_comment'])
            table['table_comment'] = "{}Owner: {}".format(tmp,obj['owner'])

        tables.append(table)

        for c in obj['columns']:
            column = {}
            if 'name' in c and 'type' in c:
                column['key'] = "{}.{}".format(table['key'], c['name']).upper()
                column['title'] = c['name'].upper()
                column['column_type'] = c['type'].upper()

                if 'nullable' in c:
                    column['nullable'] = c['nullable']
                if 'position' in c:
                    column['position'] = c['position']
                if 'comments' in c:
                    column['description'] = c['comments']
                    column['column_comment'] = c['comments']

                columns.append(column)


for obj in data['objects']:
    extract_schema_structure(obj)

    if 'type' in obj:
        if obj['type'] == 'VIEW':
            process_view(obj)
        
        #TODO uncomment
        #process already complete comment while dev work on view processing
        #else:
            #process_table(obj)

#TODO uncomment
# process already complete comment while dev work on view processing
# write out table and column info to files aligned with cli tool standards
# with open('{}/tables.json'.format(root_dir), 'w') as to:
#     to.write(json.dumps(tables))
#
# with open('{}/columns.json'.format(root_dir), 'w') as co:
#     co.write(json.dumps(columns))

#temp
with open('{}/views.json'.format(root_dir), 'w') as fo:
    fo.write(json.dumps(views))
#END temp

print("----END OF LINE----")








