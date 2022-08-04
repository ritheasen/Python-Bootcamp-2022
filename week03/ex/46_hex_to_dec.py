

def hex_to_dec(hexa):
    hexa = str(hexa)
    hexDigits = set("0123456789abcdef")
    for char in hexa:
        if char in hexDigits:
            print(f'hex_to_dec("{hexa}")')
            decimal = int(hexa,16)
            print(decimal)
            break
            
        else:
            print("This is not a hexa-decimal number") #it print if the input begin with not hexa
            break

hex_to_dec("ba1") 
