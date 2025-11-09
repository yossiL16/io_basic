


def start():
    sentes = input("please enter a sentens: ").upper()
    return sentes

def atbash_dict():
    atbash = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
            'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
            'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
            'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
            'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}
    return atbash

def Encryption(atbash, sentes):
    sicret = ''
    for latter in sentes:
        if latter in atbash.keys():
            sicret += atbash[latter]
        else:
            sicret += latter
    return sicret

def create_file(sicret):
    f = open("secret.txt", "w")
    f.write(sicret)
    f.close()

    f = open("secret.txt", "r")
    sicret_print = f.read()
    print("--- That encrypted sentence ---")
    print(sicret_print.lower())
    f.close()
    return sicret_print

def translate(atbash, sicret_print):
    translate = ""
    for latter in sicret_print:
        if latter in atbash.keys():
            translate += atbash[latter]
        else:
            translate += latter
    print("--- The translated sentence is ---")
    print(translate.lower())



