import json

schema = {}

tables = []
columns = []
views = []
data = {}

root_dir = '/Users/karl/Documents/data/alation/oracleHCM'

with open('{}/22b-2/22b.json'.format(root_dir), 'r') as file:
    data = json.loads(file.read())


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

        schema[obj['name'].upper()] = {}

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
                schema[obj['name'].upper()][c['name'].upper()] = 'TABLE'


for obj in data['objects']:
    if 'type' in obj:
        if obj['type'] == 'VIEW':
            views.append(obj)
        else:
            process_table(obj)

with open('{}/tables.json'.format(root_dir), 'w') as to:
    to.write(json.dumps(tables))

with open('{}/columns.json'.format(root_dir), 'w') as co:
    co.write(json.dumps(columns))


print("----END OF LINE----")








