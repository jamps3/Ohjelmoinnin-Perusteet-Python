import os
import csv
from datetime import datetime

def viralliset_pisteet():
    aloitus = os.path.join(os.path.dirname(__file__), 'tentin_aloitus.csv')
    data = []
    
    # Read starting times into a dictionary
    with open(aloitus) as tiedosto:
        for rivi in csv.reader(tiedosto, delimiter=";"):
            data.append(rivi)
        sanakirja = {key: value for key, value in data}

    palautus = os.path.join(os.path.dirname(__file__), 'palautus.csv')
    opiskelijat = {}

    with open(palautus) as tiedosto2:
        for rivi in csv.reader(tiedosto2, delimiter=";"):
            name, task, points, return_time = rivi
            task = int(task)
            points = int(points)
            
            # Ensure student exists in tentin_aloitus.csv
            if name not in sanakirja:
                continue
            
            format = "%H:%M"  # Time format
            tentinaloitus = datetime.strptime(sanakirja[name], format)  # Start time
            tentinlopetus = datetime.strptime(return_time, format)  # Submission time
            
            # Check if the submission is within 3 hours
            difference = abs((tentinlopetus - tentinaloitus).total_seconds() / 3600)
            if difference > 3:
                continue
            
            # Check if the student exists in the dictionary
            if name not in opiskelijat:
                opiskelijat[name] = {}
            
            # Update the points for the task if higher
            if task not in opiskelijat[name] or points > opiskelijat[name][task]:
                opiskelijat[name][task] = points

    # Calculate total points for each student
    total_points = {student: sum(tasks.values()) for student, tasks in opiskelijat.items()}
    return total_points

if __name__ == "__main__":
    print(viralliset_pisteet())