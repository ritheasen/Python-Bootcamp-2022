def hex_to_oct(hexa):

    hexDigits = set("0123456789abcdef")
    for char in hexa:
        if (char in hexDigits):
            print(f'hex_to_dec("{hexa}")')
            decimal = int(hexa,16)
            
            octal = oct(decimal)
            print(octal.replace("0o",""))
            break
            
        elif not (char in hexDigits):
            print("This is not a hexa-decimal number")
            break












hex_to_oct("2b9")