class HindiTokenizer:
    def __init__(self):
        self.delimiters = set([' ', '।', ',', '!', '?', '(', ')', '“', '”', '‘', '’'])

    def tokenize(self, text):
        tokens = []
        current_token = ""
        for char in text:
            if char in self.delimiters:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                if char != ' ':
                    tokens.append(char)
            else:
                current_token += char
        if current_token:
            tokens.append(current_token)
        return tokens
