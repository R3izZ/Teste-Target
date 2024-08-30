def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

string = "Gabriel Reis"  
print(f"String original: {string}")
print(f"String invertida: {inverter_string(string)}")
