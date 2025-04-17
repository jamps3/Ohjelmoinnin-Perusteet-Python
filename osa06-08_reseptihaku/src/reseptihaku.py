import os # for file handling

def hae_nimi(tiedosto: str, sana: str):
    """
    This function takes a file and a string as input and returns a list of recipes
    that contain the string in their name.
    """
    # Read recipe file
    reseptit = os.path.join(os.path.dirname(__file__), tiedosto)
    reseptit = tiedosto
    with open(reseptit, 'r') as file:
        lines = file.readlines()

    # Find recipes that contain the string in their name
    reseptit = []
    for line in lines:
        if sana.lower() in line.lower():
            if line.strip() and line[0].isupper():  # Skip lines that start with noncapital letters
                reseptit.append(line.strip())
    return reseptit

def hae_aika(tiedosto: str, aika: int):
    """This function takes a file and time as input and returns a list of recipes
    that can be made within the given time.
    The time is given in minutes.

    Args:
        tiedosto (str): _path to the recipe file_
        aika (int): _time in minutes_
    """
    # Read recipe file
    reseptit = os.path.join(os.path.dirname(__file__), tiedosto)
    reseptit = tiedosto
    with open(reseptit, 'r') as file:
        lines = file.readlines()

    # Find recipes that can be made within the given time
    reseptit = []
    i = 0
    while i < len(lines):
        nimi = lines[i].strip()
        aika_resepti = int(lines[i + 1].strip())
        if aika_resepti <= aika:
            reseptit.append(nimi + ", valmistusaika " + str(aika_resepti) + " min")
        # Skip to the next recipe (name + time + ingredients)
        i += 2
        while i < len(lines) and lines[i].strip() != "":
            i += 1
        i += 1
    # Return the list of recipes
    return reseptit

def hae_raakaaine(tiedosto: str, aine: str):
    """
    This function takes a file and an ingredient as input
    and returns a list of recipes that contain the ingredient.
    """
    # Construct file path
    file_path = os.path.join(os.path.dirname(__file__), tiedosto)
    file_path = tiedosto
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        return f"File {tiedosto} not found."

    reseptit = []
    i = 0

    while i < len(lines):
        nimi = lines[i].strip()  # Recipe name
        aika_resepti = int(lines[i + 1].strip())  # Preparation time
        ingredients = []
        i += 2

        while i < len(lines) and lines[i].strip() != "":
            ingredients.append(lines[i].strip())
            i += 1

        if any(aine.lower() in ingredient.lower() for ingredient in ingredients):
            reseptit.append(f"{nimi}, valmistusaika {aika_resepti} min")

        i += 1  # Skip empty line

    return reseptit

if __name__ == "__main__":
    text = input("Hae reseptiä nimellä: ")
    results = hae_nimi("reseptit1.txt", text)
    # Print the results
    for result in results:
        print(result)
    text = input("Hae reseptiä ajalla: ")
    results = hae_aika("reseptit1.txt", int(text))
    # Print the results
    for result in results:
        print(result)
    text = input("Hae reseptiä raaka-aineella: ")
    results = hae_raakaaine("reseptit1.txt", text)
    # Print the results
    for result in results:
        print(result)