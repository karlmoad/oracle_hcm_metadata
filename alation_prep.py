import json
import re
from parse.tokenizer import Tokenizer
from parse.common import Token, TokenType

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


def find_tables(tokens, names):
    rez = {'tables': {}}
    in_from_clause = False
    for i, token in enumerate(tokens):
        if token.token_type == TokenType.FROM:
            in_from_clause = True
            continue
        if in_from_clause and \
                token.token_type in [TokenType.SELECT, TokenType.WHERE, TokenType.GROUP_BY, TokenType.ORDER_BY]:
            in_from_clause = False
            continue
        if in_from_clause and token.token_type == TokenType.UNKNOWN:
            if token.label in names:
                # establish table to alias idx entry
                if token.label not in rez['tables']:
                    rez['tables'][token.label] = []

                # identify is alias is present
                if i+1 < len(tokens) and tokens[i+1].token_type is TokenType.UNKNOWN:
                    lbl = tokens[i + 1].label
                    if lbl not in rez['tables'][token.label]:
                        rez['tables'][token.label].append(lbl)
    return rez


def process_view(obj):
    view = {}
    if 'name' in obj and 'schema' in obj and 'query' in obj:
        view['key'] = "{}.{}".format(obj['schema'], obj['name']).upper()
        view['title'] = obj['name'].upper()
        view['description'] = obj['description']
        view["table_type"] = "VIEW"

        if 'section' in obj:
            view['table_comment'] = "Scope: {}".format(obj['section'], obj['owner'])
        if 'owner' in obj:
            tmp = ''
            if 'table_comment' in view:
                tmp = "{},".format(view['table_comment'])
            view['table_comment'] = "{}Owner: {}".format(tmp, obj['owner'])

        sql = ''
        for s in obj["query"]:
            sql += s + "\n"

        t = Tokenizer(sql.upper())
        t.parse()
        t_refs = find_tables(t.tokens, schema.keys())
        view['view_sql'] = sql.upper()
        view["table_refs"] = t_refs
        views.append(view)

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
    fo.write(json.dumps(views[0:100]))
#END temp

print("----END OF LINE----")








