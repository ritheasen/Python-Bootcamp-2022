


def hex_to_dec(hexa):
    hexDigits = set("0123456789abcdef")
    for char in hexa:
        if (char in hexDigits):
            print(f'hex_to_dec("{hexa}")')
            decimal = int(hexa,16)
            print(decimal)
            break
            
        elif not (char in hexDigits):
            print("This is not a hexa-decimal number")
            break

hex_to_dec("ba1")
