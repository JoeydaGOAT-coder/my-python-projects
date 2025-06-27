def main():
    en_de = input("enter '1' for encryption and '2' for decryption: ")
    if en_de == "1":
        inputter = input("enter text to be encrypted: ")
        mapping = {
            '9': 'a',
            '0': 'b',
            ' ': 'c',
            'a': 'd',
            'b': 'e',
            'c': 'f',
            'd': 'g',
            'e': 'h',
            'f': 'i',
            'g': 'j',
            'h': 'k',
            'i': 'l',
            'j': 'm',
            'k': 'n',
            'l': 'o',
            'm': 'p',
            'n': 'q',
            'o': 'r',
            'p': 's',
            'q': 't',
            'r': 'u',
            's': 'v',
            't': 'w',
            'u': 'x',
            'v': 'y',
            'w': 'z',
            'x': '1',
            'y': '2',
            'z': '3',
            '1': '4',
            '2': '5',
            '3': '6',
            '4': '7',
            '5': '8',
            '6': '9',
            '7': '0',
            '8': ' '
        }
        result = []
        for char in inputter:
            lower_char = char.lower()
            mapped = mapping.get(lower_char, char)
            result.append(mapped)
        print("".join(result))
    elif en_de == "2":
        inputter = input("enter text to be decrypted: ")
        mapping = {
            'a': '9',
            'b': '0',
            'c': ' ',
            'd': 'a',
            'e': 'b',
            'f': 'c',
            'g': 'd',
            'h': 'e',
            'i': 'f',
            'j': 'g',
            'k': 'h',
            'l': 'i',
            'm': 'j',
            'n': 'k',
            'o': 'l',
            'p': 'm',
            'q': 'n',
            'r': 'o',
            's': 'p',
            't': 'q',
            'u': 'r',
            'v': 's',
            'w': 't',
            'x': 'u',
            'y': 'v',
            'z': 'w',
            '1': 'x',
            '2': 'y',
            '3': 'z',
            '4': '1',
            '5': '2',
            '6': '3',
            '7': '4',
            '8': '5',
            '9': '6',
            '0': '7',
            ' ': '8'
        }
        result = []
        for char in inputter:
            lower_char = char.lower()
            mapped = mapping.get(lower_char, char)
            result.append(mapped)
        print("".join(result))
    else:
        print("invalid value")
        main()
    ask = input("enter 'y' to encrypt/decrypt again: ")
    if ask.lower() == "y":
        main()

main()
