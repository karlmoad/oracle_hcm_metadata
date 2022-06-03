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
    INSERT = auto()
    UPDATE = auto()
    DELETE = auto()
    AS = auto()
    REFERENCE = auto()
    FIELD = auto()
    PERIOD = auto()


class Token:
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