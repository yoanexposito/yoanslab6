
def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def encode(plus):
    encoder = ''
    for i in range(0, len(plus)):
        if int(plus[i]) <= 6:
            num = int(plus[i]) + 3
            encoder += str(num)
        if int(plus[i]) >= 7:
            num = int(plus[i]) + 3
            encoder += str(num)[1]
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
        elif option == 2:
            dePass = encode(password)
            print('the encoded password is ', encode(password), 'and the original password is #decode(dePass)')
        elif option == 3:
            gameCont = False
if __name__ == '__main__':
    main()