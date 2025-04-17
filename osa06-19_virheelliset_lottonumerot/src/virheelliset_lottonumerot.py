import os

def suodata_virheelliset():
    viikot = []
    tiedosto = os.path.join(os.path.dirname(__file__), 'lottonumerot.csv')
    tiedosto = 'lottonumerot.csv'
    
    if not os.path.exists(tiedosto):
        print("File not found:", tiedosto)
        return
    
    with open(tiedosto, "r") as alku:
        for line in alku:
            parts = line.strip().split(";")
            if len(parts) != 2:
                print("Invalid format, skipping line:", line)
                continue
            
            try:
                viikko = int(parts[0].split()[1])  # Extract integer from "viikko X"
                numerot = list(map(int, parts[1].split(",")))
            except (ValueError, IndexError):
                print("Invalid data, skipping line:", line)
                continue  # Skip invalid lines
            
            # Validate numbers
            if len(numerot) == 7 and all(1 <= num <= 39 for num in numerot):
                if len(numerot) != len(set(numerot)):
                    print("Duplicate numbers found, skipping line:", line)
                    continue
                viikot.append((viikko, numerot))
            else:
                print("Invalid numbers, skipping line:", line)
    
    # Write valid entries to the output file
    if not viikot:
        print("No valid entries found.")
        return
    
    tiedosto = os.path.join(os.path.dirname(__file__), 'korjatut_numerot.csv')
    tiedosto = 'korjatut_numerot.csv'
    with open(tiedosto, "w") as file:
        for viikko, numerot in viikot:
            file.write(f"viikko {viikko};{','.join(map(str, numerot))}\n")

    print("Processing complete. Output written to korjatut_numerot.csv")

if __name__ == "__main__":
    suodata_virheelliset()