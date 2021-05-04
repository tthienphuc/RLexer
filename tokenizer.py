from token import *

class Tokenizer:
    def __init__(self, text: str):
        self.lines = text.splitlines()
        self.line = ''
        self.tokens = []
        self.mark = 0

    # return current char
    def CurrentChar(self) -> chr:
        return self.line[self.mark]

    # check end of line
    def EOL(self) -> bool:
        return self.mark >= len(self.line)

    def Seek(self) -> chr:
        self.mark += 1
        return self.line[self.mark - 1]

    # scan strings beginning with a dot
    def ScanDot(self):
        token = Token()
        self.mark += 1

        while not self.EOL() and (self.CurrentChar().isalnum() or self.CurrentChar() == DOT or self.CurrentChar() == UNDERLINE):
            token.lexeme += self.Seek()

        if token.lexeme.isnumeric():
            token.tokenType = TokenType.Real
            token.value = '0.' + token.lexeme
        elif len(token.lexeme) > 0 and token.lexeme[0].isdigit():
            token.TokenType = TokenType.Error
            token.value = ''
        else:
            token.tokenType = TokenType.Id 
            token.value = '.' + token.lexeme
        token.lexeme = DOT + token.lexeme
        
        self.tokens.append(token)

    # scan ids or keywords
    def ScanIdOrKeyword(self):
        token = Token()
        token.tokenType = TokenType.Id
        while not self.EOL() and (self.CurrentChar().isalnum() or self.CurrentChar() == DOT or self.CurrentChar == UNDERLINE):
            token.lexeme += self.Seek()
        token.value = token.lexeme
        if token.lexeme in Keywords.keys():
            token.tokenType = TokenType.Keyword
            token.value = Keywords[token.lexeme]
        self.tokens.append(token)

    # scan numbers
    def ScanNum(self):
        token = Token()
        while not self.EOL() and self.CurrentChar().isdigit():
            token.lexeme += self.Seek()
        
        token.tokenType = TokenType.Integer
        if not self.EOL() and self.CurrentChar() == DOT:
            self.ScanDot()
            sub_token = self.tokens.pop()
            if sub_token.lexeme == DOT:
                token.value = token.lexeme
                token.lexeme += DOT
            elif sub_token.tokenType == TokenType.Real: 
                token.tokenType = TokenType.Real
                token.lexeme = token.lexeme + sub_token.lexeme
                token.value = token.lexeme
            else:
                token.tokenType = TokenType.Error
                token.lexeme = token.lexeme + sub_token.lexeme
        else:
            token.value = token.lexeme
        self.tokens.append(token)

    # scan operators
    def ScanOperator(self):
        token = Token()
        while not self.EOL() and self.CurrentChar() in Special_Characters:
            token.lexeme += self.Seek()
        if token.lexeme in Operators.keys():
            token.tokenType = TokenType.Operator
            token.value = Operators[token.lexeme]
        elif token.lexeme in Delimiters.keys():
            token.tokenType = TokenType.Delimiter
            token.value = Delimiters[token.lexeme]
        else:
            token.tokenType = TokenType.Error
        self.tokens.append(token)

    def GetToken(self):
        if self.CurrentChar().isspace():
            return self.Seek()
        elif self.CurrentChar().isdigit():
            return self.ScanNum()
        elif self.CurrentChar() == DOT:
            return self.ScanDot()
        elif self.CurrentChar().isalpha(): 
            return self.ScanIdOrKeyword()
        else:
            return self.ScanOperator()

    def ScanLine(self):
        self.mark = 0
        while not self.EOL():
            self.GetToken()

    def Scan(self):
        for line in self.lines:
            self.line = line.strip()
            self.ScanLine()

    def GetTokens(self) -> list:
        self.Scan()
        return self.tokens
    

