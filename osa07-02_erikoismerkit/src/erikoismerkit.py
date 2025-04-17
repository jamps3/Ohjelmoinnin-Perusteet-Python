import string

def jaa_merkkeihin(merkkijono: string):
    ascii_letters = ''.join([char for char in merkkijono if char in string.ascii_letters])
    punctuation = ''.join([char for char in merkkijono if char in string.punctuation])
    others = ''.join([char for char in merkkijono if char not in string.ascii_letters and char not in string.punctuation])
    return (ascii_letters, punctuation, others)

if __name__ == "__main__":
    result = jaa_merkkeihin("'__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt_")
    print(result)