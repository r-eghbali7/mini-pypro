from deep_translator import GoogleTranslator

# Translate the text from English to Persian

def my_translator(text):
    translator = GoogleTranslator(source='en', target='fa').translate(text)
    return translator

text = "Hello"
print(my_translator(text))