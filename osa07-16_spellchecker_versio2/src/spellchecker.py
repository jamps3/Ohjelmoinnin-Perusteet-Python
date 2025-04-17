import csv
import os
import difflib
import string

def spellchecker(text):
    """
    This function takes a string as input and returns it with misspelled words surrounded with *s and gives suggestions for them.
    - Handles punctuation (e.g., "hello." → hello)
    - Avoids duplicate correction suggestions
    - Cleans up formatting (no random commas or spacing)
    - Gives meaningful suggestions only once per misspelled word
    """
    # Load wordlist
    sanalista = os.path.join(os.path.dirname(__file__), "wordlist.txt")
    with open(sanalista, 'r') as file:
        words = set(file.read().splitlines())

    # Split the input text into words
    text_words = text.split()

    # Cleaned words for checking, map original -> cleaned
    word_map = {}
    for word in text_words:
        clean_word = word.strip(string.punctuation).lower()
        word_map[word] = clean_word

    # Build output with * for misspelled words
    returnstring = []
    misspelled = set()

    for word in text_words:
        if word_map[word] not in words:
            returnstring.append(f"*{word}*")
            misspelled.add(word_map[word])
        else:
            returnstring.append(word)

    result = " ".join(returnstring)

    # Suggestions
    for original in misspelled:
        matches = difflib.get_close_matches(original, words)
        if matches:
            result += "\nkorjausehdotukset:\n"
            result += f"{original}: {', '.join(matches)}\n"
        else:
            result += f"{original}: (ei ehdotuksia)\n"

    return result

#if __name__ == "__main__":
# text = "This is a smaple text with some misspelled words."
#text = "This iis good"
text = input("write text: ") # Get input from the user
print(spellchecker(text))
