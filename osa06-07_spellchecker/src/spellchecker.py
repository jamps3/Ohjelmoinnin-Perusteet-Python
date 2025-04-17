def spellchecker(text):
    """
    This function takes a string as input and returns it with misspelled words surrounded with *s.
    """
    # List of words
    import os
    sanalista = os.path.join(os.path.dirname(__file__), "wordlist.txt")
    with open(sanalista, 'r') as file:
        words = set(file.read().splitlines())

    # Split the input text into words
    text_words = text.split()

    # Check for misspelled words
    returnstring = ""
    for word in text_words:
        if word.lower() not in words:
            returnstring += " *" + word + "*"
        else:
            returnstring += " " + word
    return returnstring

text = input("Write text: ")
print(spellchecker(text))