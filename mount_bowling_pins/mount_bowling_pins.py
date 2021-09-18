# Kata hecha por @keizar76 , @aleepsy

def bowling_pins(arr):
    bowling_pins = "I I I I\n I I I \n  I I  \n   I   "
    bowling_pins_number = "7 8 9 10\n 4 5 6 \n  2 3  \n   1   "
    diccionario = {
        '7': 0,
        '8': 2,
        '9': 4,
        '10': 6,
        '4': 9,
        '5': 11,
        '6': 13,
        '2': 18,
        '3': 20,
        '1': 27
    }
    
    for item in arr:
        item_string = str(item)
        indice = diccionario[item_string]      
        bowling_pins = bowling_pins[:indice] + ' ' + bowling_pins[indice + 1:]
    
    return bowling_pins