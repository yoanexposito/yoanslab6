
def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def encode(plus):
    encoder = ''
    for i in range(0, len(plus)):
        num = int(plus[i]) + 3
        encoder += str(num)
    return encoder


def main():
    gameCont = True

    while gameCont:
        menu()
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            encode(password)
            print('Your password has been encoded ans stored!')
            print(encode(password))

if __name__ == '__main__':
    main()