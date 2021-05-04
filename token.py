from enum import Enum

class TokenType(Enum):
    Error = 'ERROR'
    Integer = 'NUMBERIC'
    Real = 'NUMBERIC'
    Id = 'ID'
    Keyword = 'KEYWORD'
    Operator = 'OPERATOR'
    Delimiter = 'DELIMITER'

# special keyworks
Keywords = {
    'if': 'IF',
    'else': 'ELSE',
    'repeat': 'REPEAT',
    'while': 'WHILE',
    'function': 'FUNCTION',
    'for': 'FOR',
    'in': 'IN',
    'break': 'BREAK',
    'TRUE': 'TRUE',
    'FALSE': 'FALSE',
    'NULL': 'NULL',
    'Inf': 'INF',
    'NaN': 'NAN',
    'NA': 'NA',
    'NA_integer': 'NA_INTEGER',
    'NA_real': 'NA_REAL',
    'NA_complex': 'NA_COMPLEX',
    'NA_charact': 'NA_CHARACT'
}

# operators
Operators = {
    # arithmetic
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'MULTIPLY',
    '/': 'DIVIDE',
    '%': 'MOD',
    '&/%': 'INTEGER DIVIDE',
    '^': 'POWER',
    '**': 'POWER',
    # relational
    '<': 'LESS',
    '<=': 'LESS OR EQUAL',
    '>': 'GREATER',
    '>=': 'GREATER OR EQUAL',
    '==': 'EQUAL',
    '!=': 'NOT EQUAL',
    # logical
    '!': 'NOT',
    '|': 'OR',
    '||': 'OR',
    '&': 'AND',
    '&&': 'AND',
    # assign
    '=': 'EQUAL ASSIGN',
    '<<-': 'LEFT FUNCTION ASSIGN',
    '->>': 'RIGHT FUNCTION ASSIGN',
    '<-': 'ARROW LEFT ASSIGN',
    '->': 'ARROW RIGHT ASSIGN'
}

Delimiters = {
    '{': 'LEFT BRACE',
    '}': 'RIGHT BRACE',
    '[': 'LEFT BOX BRACKET',
    ']': 'RIGHT BOX BRACKET',
    '(': 'LEFT PARENTHESE',
    ')': 'RIGHT PARENTHESE',
    ',': 'COMMA',
    "'": 'APOSTROPHE',
    '"': 'QUOTATION MARK' 
}

Special_Characters = """{}[](),'"+-*/%^<>=!&|"""

# dot
DOT = '.'

# underline
UNDERLINE = '_'

class Token:
    def __init__(self):
        self.tokenType = TokenType.Error
        self.lexeme = ''
        self.value = ''

    def __str__(self):
        return "[{}, {}, {}]".format(self.tokenType.value, self.lexeme, self.value)