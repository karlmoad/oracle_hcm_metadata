from parse.common import EnumBase
from enum import auto


class TokenType(EnumBase):
    UNKNOWN = auto()
    KEYWORD = auto()
    OBJECT = auto()
    OPERATOR = auto()
    WILDCARD = auto()
    COMMENT = auto()
    COMMAND = auto()
    VALUE = auto()
    SEPARATOR = auto()
    GROUPING = auto()
    LITERAL = auto()
    FUNCTION = auto()
    WHITESPACE = auto()

class Token:
    def __init__(self, label: str = '', ttype: TokenType = TokenType.UNKNOWN):
        self._type = ttype
        self._children = []
        self._label = label

    def has_sub_statement(self):
        return len(self._children) > 0

    def get_type(self) -> TokenType:
        return self._type

    def set_type(self, value: TokenType):
        self._type = value

    def get_label(self) -> str:
        return self._label

    def get_children(self) -> list:
        return self._children

    def add_child(self, token) -> None:
        self._children.append(token)


    token_type = property(get_type, set_type)
    label = property(get_label, None)
    children = property(get_children, None)

class Tokenizer:
    def __init__(self, statement):
        self._tokens = []
        self._statement = statement.upper()

    def get_tokens(self):
        return self._tokens

    tokens = property(get_tokens, None)

    _OPERATORS = {
        ",": TokenType.SEPARATOR,
        "'": TokenType.LITERAL,
        "(": TokenType.GROUPING,
        ")": TokenType.GROUPING,
        "[": TokenType.GROUPING,
        "]": TokenType.GROUPING,
        "{": TokenType.GROUPING,
        "}": TokenType.GROUPING,
        "&": TokenType.OPERATOR,
        "^": TokenType.OPERATOR,
        ":": TokenType.OPERATOR,
        ".": TokenType.OPERATOR,
        "-": TokenType.OPERATOR,
        "=": TokenType.OPERATOR,
        ">": TokenType.OPERATOR,
        "<": TokenType.OPERATOR,
        "%": TokenType.OPERATOR,
        "!": TokenType.OPERATOR,
        "|": TokenType.OPERATOR,
        "+": TokenType.OPERATOR,
        ";": TokenType.OPERATOR,
        "/": TokenType.OPERATOR,
        "*": TokenType.WILDCARD,
        "~": TokenType.OPERATOR,
        "--": TokenType.COMMENT,
        "/*": TokenType.COMMENT,
        "*/": TokenType.COMMENT,
        "==": TokenType.OPERATOR,
        "::": TokenType.OPERATOR,
        "||": TokenType.OPERATOR,
        ">=": TokenType.OPERATOR,
        "<=": TokenType.OPERATOR,
        "<>": TokenType.OPERATOR,
        "!=": TokenType.OPERATOR,
        "<<": TokenType.OPERATOR,
        ">>": TokenType.OPERATOR,
    }

    _KEYWORDS = {
        "ALL": TokenType.KEYWORD,
        "ALTER": TokenType.KEYWORD,
        "AND": TokenType.KEYWORD,
        "ASC": TokenType.KEYWORD,
        "AS": TokenType.KEYWORD,
        "AUTO_INCREMENT": TokenType.KEYWORD,
        "BEGIN": TokenType.KEYWORD,
        "BETWEEN": TokenType.OPERATOR,
        "BUCKET": TokenType.KEYWORD,
        "BY": TokenType.KEYWORD,
        "CACHE": TokenType.KEYWORD,
        "UNCACHE": TokenType.KEYWORD,
        "CASE": TokenType.KEYWORD,
        "CAST": TokenType.KEYWORD,
        "COLLATE": TokenType.KEYWORD,
        "COMMENT": TokenType.KEYWORD,
        "COMMIT": TokenType.KEYWORD,
        "COUNT": TokenType.KEYWORD,
        "CREATE": TokenType.KEYWORD,
        "CROSS": TokenType.KEYWORD,
        "DIV": TokenType.KEYWORD,
        "DEFAULT": TokenType.KEYWORD,
        "DELETE": TokenType.KEYWORD,
        "DESC": TokenType.KEYWORD,
        "DISTINCT": TokenType.KEYWORD,
        "DROP": TokenType.KEYWORD,
        "ELSE": TokenType.KEYWORD,
        "END": TokenType.KEYWORD,
        "ENGINE": TokenType.KEYWORD,
        "ESCAPE": TokenType.KEYWORD,
        "EXCEPT": TokenType.KEYWORD,
        "EXISTS": TokenType.KEYWORD,
        "EXPLAIN": TokenType.KEYWORD,
        "EXTRACT": TokenType.KEYWORD,
        "FALSE": TokenType.KEYWORD,
        "FILTER": TokenType.KEYWORD,
        "FULL": TokenType.KEYWORD,
        "FUNCTION": TokenType.KEYWORD,
        "FOLLOWING": TokenType.KEYWORD,
        "FROM": TokenType.KEYWORD,
        "GROUP": TokenType.KEYWORD,
        "HAVING": TokenType.KEYWORD,
        "IF": TokenType.KEYWORD,
        "ILIKE": TokenType.KEYWORD,
        "IN": TokenType.KEYWORD,
        "INNER": TokenType.KEYWORD,
        "INSERT": TokenType.KEYWORD,
        "INTERVAL": TokenType.KEYWORD,
        "INTERSECT": TokenType.KEYWORD,
        "INTO": TokenType.KEYWORD,
        "IS": TokenType.KEYWORD,
        "JOIN": TokenType.KEYWORD,
        "LATERAL": TokenType.KEYWORD,
        "LAZY": TokenType.KEYWORD,
        "LEFT": TokenType.KEYWORD,
        "LIKE": TokenType.KEYWORD,
        "LIMIT": TokenType.KEYWORD,
        "NOT": TokenType.KEYWORD,
        "NULL": TokenType.KEYWORD,
        "OFFSET": TokenType.KEYWORD,
        "ON": TokenType.KEYWORD,
        "OPTIMIZE": TokenType.KEYWORD,
        "OPTIONS": TokenType.KEYWORD,
        "OR": TokenType.KEYWORD,
        "ORDER": TokenType.KEYWORD,
        "ORDINALITY": TokenType.KEYWORD,
        "OUTER": TokenType.KEYWORD,
        "OVER": TokenType.KEYWORD,
        "OVERWRITE": TokenType.KEYWORD,
        "PARTITION": TokenType.KEYWORD,
        "PARTITIONED": TokenType.KEYWORD,
        "PERCENT": TokenType.KEYWORD,
        "PRECEDING": TokenType.KEYWORD,
        "PRIMARY KEY": TokenType.KEYWORD,
        "QUALIFY": TokenType.KEYWORD,
        "RANGE": TokenType.KEYWORD,
        "RECURSIVE": TokenType.KEYWORD,
        "REGEXP": TokenType.KEYWORD,
        "REPLACE": TokenType.KEYWORD,
        "RIGHT": TokenType.KEYWORD,
        "RLIKE": TokenType.KEYWORD,
        "ROWS": TokenType.KEYWORD,
        "SELECT": TokenType.KEYWORD,
        "SET": TokenType.KEYWORD,
        "SHOW": TokenType.KEYWORD,
        "STORED": TokenType.KEYWORD,
        "TABLE": TokenType.KEYWORD,
        "TBLPROPERTIES": TokenType.KEYWORD,
        "TABLESAMPLE": TokenType.KEYWORD,
        "TEMP": TokenType.KEYWORD,
        "TEMPORARY": TokenType.KEYWORD,
        "THEN": TokenType.KEYWORD,
        "TIME": TokenType.KEYWORD,
        "TRUE": TokenType.KEYWORD,
        "TRUNCATE": TokenType.KEYWORD,
        "TRY_CAST": TokenType.KEYWORD,
        "UNBOUNDED": TokenType.KEYWORD,
        "UNION": TokenType.KEYWORD,
        "UNNEST": TokenType.KEYWORD,
        "UPDATE": TokenType.KEYWORD,
        "USE": TokenType.KEYWORD,
        "VALUES": TokenType.KEYWORD,
        "VIEW": TokenType.KEYWORD,
        "WHEN": TokenType.KEYWORD,
        "WHERE": TokenType.KEYWORD,
        "WITH": TokenType.KEYWORD,
        "WITHOUT": TokenType.KEYWORD,
        "ZONE": TokenType.KEYWORD,
        "ARRAY": TokenType.KEYWORD,
        "BOOL": TokenType.KEYWORD,
        "BOOLEAN": TokenType.KEYWORD,
        "BYTE": TokenType.KEYWORD,
        "TINYINT": TokenType.KEYWORD,
        "SHORT": TokenType.KEYWORD,
        "SMALLINT": TokenType.KEYWORD,
        "INT2": TokenType.KEYWORD,
        "INTEGER": TokenType.KEYWORD,
        "INT": TokenType.KEYWORD,
        "INT4": TokenType.KEYWORD,
        "LONG": TokenType.KEYWORD,
        "BIGINT": TokenType.KEYWORD,
        "INT8": TokenType.KEYWORD,
        "DECIMAL": TokenType.KEYWORD,
        "MAP": TokenType.KEYWORD,
        "NUMBER": TokenType.KEYWORD,
        "NUMERIC": TokenType.KEYWORD,
        "FIXED": TokenType.KEYWORD,
        "REAL": TokenType.KEYWORD,
        "FLOAT": TokenType.KEYWORD,
        "FLOAT4": TokenType.KEYWORD,
        "FLOAT8": TokenType.KEYWORD,
        "DOUBLE": TokenType.KEYWORD,
        "JSON": TokenType.KEYWORD,
        "CHAR": TokenType.KEYWORD,
        "VARCHAR": TokenType.KEYWORD,
        "STRING": TokenType.KEYWORD,
        "TEXT": TokenType.KEYWORD,
        "BINARY": TokenType.KEYWORD,
        "BYTEA": TokenType.KEYWORD,
        "TIMESTAMP": TokenType.KEYWORD,
        "TIMESTAMPTZ": TokenType.KEYWORD,
        "DATE": TokenType.KEYWORD,
        "UUID": TokenType.KEYWORD,
    }

    _WHITE_SPACE = {
        " ": TokenType.WHITESPACE,
        "\t": TokenType.WHITESPACE,
        "\r": TokenType.WHITESPACE,
        "\n": TokenType.WHITESPACE,
        "\rn": TokenType.WHITESPACE,
    }

    def tokenize(self):
        self._white_space_pass()
        self._operator_pass()
        self._condense_operators_pass()

    def _condense_operators_pass(self):
        # scan token set and condense multi character operators when found
        working = []
        pos = 0
        while True:
            if pos > len(self._tokens) -1:
                break
            else:
                if self._tokens[pos] in self._OPERATORS and self._OPERATORS[self.tokens[pos]] == TokenType.OPERATOR:
                    if (pos+1) <= len(self._tokens) - 1 and self._tokens[pos+1] in self._OPERATORS and self._OPERATORS[self._tokens[pos+1]] == TokenType.OPERATOR: #potential multichar operator
                        mpop = self._tokens[pos] + self._tokens[pos+1]
                        if mpop in self._OPERATORS and self._OPERATORS[mpop] == TokenType.OPERATOR:
                            working.append(mpop)
                            pos = pos+2
                            continue
                    else:
                        working.append(self._tokens[pos])

                else:
                    working.append(self._tokens[pos])
                pos = pos + 1

        self._tokens = working

    def _white_space_pass(self):
        buffer = ''
        pos = 0
        while True:
            if pos == len(self._statement) - 1:
                self._tokens.append(buffer + self._statement[pos])
                break
            else:
                tmp = self._statement[pos]
                if tmp in self._WHITE_SPACE:
                    if len(buffer.strip()) > 0:
                        self._tokens.append(buffer)
                    buffer = ''
                else:
                    buffer = buffer + tmp

            pos = pos + 1

    def _operator_pass(self):
        working = []
        for i, token in enumerate(self._tokens):
            tokens = []
            buffer = ''
            pos = 0
            while True:
                if pos > len(token) - 1:
                    if len(buffer) > 0:
                        tokens.append(buffer)
                    break
                else:
                    tmp = token[pos]
                    if tmp in self._OPERATORS:
                        if len(buffer) > 0:
                            tokens.extend([buffer, tmp])
                        else:
                            tokens.append(tmp)
                        buffer = ''
                    else:
                        buffer = buffer + tmp
                pos = pos + 1

            working.append(tokens)
        self._tokens = [token for tokens in working for token in tokens]












