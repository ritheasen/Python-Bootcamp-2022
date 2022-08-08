import string


def message_converter(stringMessage):

    stringMessageList = []

    for i in stringMessage:
        stringMessageList.append(ord(i))
    print(f'message_converter("{stringMessage}")\n')
    for j in stringMessageList:
        print(hex(j).upper().replace("0X",""),end="")

message_converter("Hello")