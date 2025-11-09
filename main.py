from play_atbash import *

def main():
    sicret = Encryption(atbash_dict(),start())
    create_file(sicret)
    translate(atbash_dict(), sicret)

if __name__ == "__main__":
    main()



