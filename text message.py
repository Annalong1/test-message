#text messaging

#main
if __name__ == "__main__":

    #key mapping dictionary
    key_mapping = {
        'a': '2', 'b': '22', 'c': '222',
        'd': '3', 'e': '33', 'f': '333',
        'g': '4', 'h': '44', 'i': '444',
        'j': '5', 'k': '55', 'l': '555',
        'm': '6', 'n': '66', 'o': '666',
        'p': '7', 'q': '77', 'r': '777', 's': '7777',
        't': '8', 'u': '88', 'v': '888',
        'w': '9', 'x': '99', 'y': '999', 'z': '9999',
        ' ': '0',
        '.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111'
    }

    key_presses = []
    key_presses_string = ""

    # input
    message = input("Enter message: ").strip().lower()

    #turning into list
    message_list = list(message)

    #looping through list
    for character in message_list:
        press = key_mapping.get(character)
        key_presses.append(press)

    #if one of the characters entered is not in keyboard
    if None in key_presses:
        print("Message entered is not possible to print")

    #if every character is vaild
    else: 
        
        #join list to make string
        key_presses_string = "".join(map(str, key_presses))

        #print
        print("The key presses you need to press to print {}, are {}". format(message, key_presses_string))
        

