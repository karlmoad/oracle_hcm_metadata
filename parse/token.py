from parse.common import EnumBase
from enum import auto

class TokenType(EnumBase):
    UNKNOWN = auto()
    DATATYPE = auto()
    KEYWORD = auto()
    OBJECT = auto()
    OPERATOR = auto()
    WILDCARD = auto()
    COMMENT = auto()
    COMMAND = auto()
    VALUE = auto()
    NAME = auto()
    SEPARATOR = auto()
    GROUPING = auto()
    LITERAL = auto()
    FUNCTION = auto()
    WHITESPACE = auto()
    SYNONYM = auto()
    PARAMETER = auto()
    SELECT = auto()
    FROM = auto()
    WHERE = auto()
    GROUP_BY = auto()
    ORDER_BY = auto()
    HAVING = auto()
    JOIN = auto()
    CONSTRAINT = auto()


class Token:
    def __init__(self, label: str = '', ttype: TokenType = TokenType.UNKNOWN):
        self._type = ttype
        self._label = label

    def get_type(self) -> TokenType:
        return self._type

    def set_type(self, value: TokenType):
        self._type = value

    def get_label(self) -> str:
        return self._label

    token_type = property(get_type, set_type)
    label = property(get_label, None)

    def __repr__(self):
        return "TOKEN(): ( LABEL: [{}], TYPE: {} )".format(self._label, self._type)

    def __str__(self):
        return "LABEL: [{}], TYPE: {}".format(self._label, self._type)


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
        ".": TokenType.SEPARATOR,
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
        "DISTINCT": TokenType.CONSTRAINT,
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
        "FROM": TokenType.FROM,
        "GROUP": TokenType.GROUP_BY,
        "HAVING": TokenType.HAVING,
        "IF": TokenType.KEYWORD,
        "ILIKE": TokenType.KEYWORD,
        "IN": TokenType.KEYWORD,
        "INNER": TokenType.KEYWORD,
        "INSERT": TokenType.KEYWORD,
        "INTERVAL": TokenType.KEYWORD,
        "INTERSECT": TokenType.KEYWORD,
        "INTO": TokenType.KEYWORD,
        "IS": TokenType.KEYWORD,
        "JOIN": TokenType.JOIN,
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
        "ORDER": TokenType.ORDER_BY,
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
        "SELECT": TokenType.SELECT,
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
        "WHERE": TokenType.WHERE,
        "WITH": TokenType.KEYWORD,
        "WITHOUT": TokenType.KEYWORD,
        "ZONE": TokenType.KEYWORD,
        "ARRAY": TokenType.DATATYPE,
        "BOOL": TokenType.DATATYPE,
        "BOOLEAN": TokenType.DATATYPE,
        "BYTE": TokenType.DATATYPE,
        "TINYINT": TokenType.DATATYPE,
        "SHORT": TokenType.DATATYPE,
        "SMALLINT": TokenType.DATATYPE,
        "INT2": TokenType.DATATYPE,
        "INTEGER": TokenType.DATATYPE,
        "INT": TokenType.DATATYPE,
        "INT4": TokenType.DATATYPE,
        "LONG": TokenType.DATATYPE,
        "BIGINT": TokenType.DATATYPE,
        "INT8": TokenType.DATATYPE,
        "DECIMAL": TokenType.DATATYPE,
        "MAP": TokenType.DATATYPE,
        "NUMBER": TokenType.DATATYPE,
        "NUMERIC": TokenType.DATATYPE,
        "FIXED": TokenType.DATATYPE,
        "REAL": TokenType.DATATYPE,
        "FLOAT": TokenType.DATATYPE,
        "FLOAT4": TokenType.DATATYPE,
        "FLOAT8": TokenType.DATATYPE,
        "DOUBLE": TokenType.DATATYPE,
        "JSON": TokenType.DATATYPE,
        "CHAR": TokenType.DATATYPE,
        "VARCHAR": TokenType.DATATYPE,
        "STRING": TokenType.DATATYPE,
        "TEXT": TokenType.DATATYPE,
        "BINARY": TokenType.DATATYPE,
        "BYTEA": TokenType.DATATYPE,
        "TIMESTAMP": TokenType.DATATYPE,
        "TIMESTAMPTZ": TokenType.DATATYPE,
        "DATE": TokenType.DATATYPE,
        "UUID": TokenType.DATATYPE,
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
        self._ttype_classification_pass()

    def _ttype_classification_pass(self):
        working = []
        for token in self._tokens:
            if token in self._OPERATORS:
                working.append(Token(label=token, ttype=self._OPERATORS[token]))
            elif token in self._KEYWORDS:
                working.append(Token(label=token, ttype=self._KEYWORDS[token]))
            else:
                working.append(Token(label=token, ttype=TokenType.UNKNOWN))
        self._tokens = working

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












