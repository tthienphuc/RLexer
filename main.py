from tokenizer import Tokenizer
from token import *
        
def main():
    # read from file
    input_file = open('input.txt')
    input_text = input_file.read()
    input_file.close()

    tokenizer = Tokenizer(input_text)
    tokens = tokenizer.GetTokens()

    for token in tokens:
        print(token)

if __name__ == "__main__":
    # execute only if run as a script
    main()