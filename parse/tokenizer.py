from parse.common import TokenType, Token, _OPERATORS, _KEYWORDS, _WHITE_SPACE


class Tokenizer:
    def __init__(self, statement):
        self._tokens = []
        self._statement = statement.upper()

    def get_tokens(self):
        return self._tokens

    tokens = property(get_tokens, None)

    def parse(self):
        self._white_space_pass()
        self._operator_pass()
        self._ttype_classification_pass()

    def _ttype_classification_pass(self):
        working = []
        for token in self._tokens:
            if token in _OPERATORS:
                working.append(Token(label=token, ttype=_OPERATORS[token]))
            elif token in _KEYWORDS:
                working.append(Token(label=token, ttype=_KEYWORDS[token]))
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
                if self._tokens[pos] in _OPERATORS and _OPERATORS[self.tokens[pos]] == TokenType.OPERATOR:
                    if (pos+1) <= len(self._tokens) - 1 and \
                            self._tokens[pos+1] in _OPERATORS and \
                            _OPERATORS[self._tokens[pos+1]] == TokenType.OPERATOR: #potential multichar operator

                        mpop = self._tokens[pos] + self._tokens[pos+1]
                        if mpop in _OPERATORS and _OPERATORS[mpop] == TokenType.OPERATOR:
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
                if tmp in _WHITE_SPACE:
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
                    if tmp in _OPERATORS:
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
        self._condense_operators_pass()

    def to_json(self):
        return [x.to_json() for x in self._tokens]










