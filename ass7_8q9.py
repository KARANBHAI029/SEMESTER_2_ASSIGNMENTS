import re

def tokenize(text):
    patterns = [
        (r'\d{1,2}/\d{1,2}/\d{4}', "DATE"),
        (r'https?://\S+', "URL"),
        (r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', "EMAIL"),
        (r'@\w+', "USERNAME"),
        (r'\d{1,3}(,\d{2,3})*', "NUMBER"),
        (r'[\u0A80-\u0AFF]+', "GUJARATI"),
        (r'[.,!?]', "PUNCTUATION")
    ]
    
    tokens = []
    for pattern, label in patterns:
        for match in re.finditer(pattern, text):
            tokens.append((match.group(), label))

    for token, label in tokens:
        print(token, ":", label)

text = "મારું નામ કરણ છે, મારી ઈમેલ karan@gmail.com, અને મારી સાઇટ https://karan.com. મારો મોબાઇલ નંબર 91,234,567 છે."
tokenize(text)
