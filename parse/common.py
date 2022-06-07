import json
from enum import Enum, auto


class EnumBase(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class TokenType(EnumBase):
    UNKNOWN = auto()
    DATATYPE = auto()
    KEYWORD = auto()
    OBJECT = auto()
    OPERATOR = auto()
    WILDCARD = auto()
    COMMENT = auto()
    COMMAND = auto()
    COMMA = auto()
    VALUE = auto()
    NAME = auto()
    SEPARATOR = auto()
    GROUPING = auto()
    LITERAL = auto()
    FUNCTION = auto()
    WHITESPACE = auto()
    ALIAS = auto()
    PARAMETER = auto()
    SELECT = auto()
    FROM = auto()
    WHERE = auto()
    GROUP_BY = auto()
    ORDER_BY = auto()
    HAVING = auto()
    JOIN = auto()
    CONSTRAINT = auto()
    INSERT = auto()
    UPDATE = auto()
    DELETE = auto()
    AS = auto()
    REFERENCE = auto()
    FIELD = auto()
    PERIOD = auto()

_OPERATORS = {
    ",": TokenType.COMMA,
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
    ".": TokenType.PERIOD,
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
    "AS": TokenType.AS,
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


class Token(dict):
    def __init__(self, label: str = '', ttype: TokenType = TokenType.UNKNOWN):
        self._type = ttype
        self._label = label
        self._subitems = []

    def get_type(self) -> TokenType:
        return self._type

    def set_type(self, value: TokenType):
        self._type = value

    def get_label(self) -> str:
        return self._label

    def set_sub_items(self, tokens):
        self._subitems = tokens

    def get_sub_items(self):
        return self._subitems

    token_type = property(get_type, set_type)
    label = property(get_label, None)
    sub_items = property(get_sub_items,set_sub_items)

    def __repr__(self):
        return '<Token : [{}]>'.format(self.token_type)

    def __str__(self, level=0):
        s = "\t"*level + 'Label: [{}], Type[{}]\n'.format(self._label, self._type)
        for item in self._subitems:
            s += item.__str__(level+1)
        return s

    def to_json(self):
        return {"label": self._label,
                "type": self._type.name,
                "sub_tokens": json.dumps([x.to_json() for x in self._subitems])}

