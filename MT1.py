from deep_translator import GoogleTranslator

def translator(input_text):
    # Use any translator you like, in this example GoogleTranslator
    #input_text_bg = "এটা চালিয়ে যান, আপনি আশ্চর্যজনক"

    translated = GoogleTranslator(source='auto', target='en').translate(input_text)
    #translated = GoogleTranslator(source='auto', target='maori').translate(translated)
    print(translated)
    return translated
