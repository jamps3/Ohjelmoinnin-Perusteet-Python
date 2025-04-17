import os

def suodata_laskut():
    # Construct file path
    tiedosto = os.path.join(os.path.dirname(__file__), 'laskut.csv')
    with open(tiedosto, 'r') as laskut_file:
        lines = laskut_file.readlines()
        laskut = [lasku.strip().split(';') for lasku in lines if lasku.strip()]
        with open('oikeat.csv', 'w') as oikeat_file, open('vaarat.csv', 'w') as vaarat_file:
            for lasku in laskut:
                
                expression = lasku[1].strip()
                operator = '+' if '+' in expression else '-' if '-' in expression else '*' if '*' in expression else '/'
                operand1, operand2 = expression.split(operator)
                operand1 = float(operand1)
                operand2 = float(operand2)
                result = float(lasku[2])

                if operator == '+':
                    calculation = operand1 + operand2
                elif operator == '-':
                    calculation = operand1 - operand2
                elif operator == '*':
                    calculation = operand1 * operand2
                elif operator == '/':
                    calculation = operand1 / operand2
                else:
                    continue

                if calculation == result:
                    #print("Correct!")
                    oikeat_file.write(';'.join(lasku) + '\n')
                else:
                    #print("Incorrect!")
                    vaarat_file.write(';'.join(lasku) + '\n')

if __name__ == "__main__":
    suodata_laskut()