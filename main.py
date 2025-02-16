from sys import exit


def main() -> None:
    NUM_OF_DIGITS: int = 16
    first_digits: dict[str: int] = {'American Express': 3,
                                    'Visa': 4, 'Mastercard': 5, 'Discover': 6}
    exit_message: str = 'Exiting program...'
    print('Welcome to The 💳 Validator!')

    while True:
        try:
            user_input: str = input('Enter a credit card number: ')
            
        except KeyboardInterrupt:
            print(exit_message)
            exit()

        if user_input == 'exit':
            print(exit_message)
            exit()

        credit_card_num: str = user_input

        invalid_msg: str = f'The credit card number {credit_card_num} is not valid.'
        valid_msg: str = f'The credit card number {credit_card_num} is valid!'

        if not credit_card_num.isnumeric():
            print(invalid_msg)
            continue

        if len(credit_card_num) != NUM_OF_DIGITS:
            print(invalid_msg)
            continue

        if int(credit_card_num[0]) not in first_digits.values():
            print(invalid_msg)
            continue

        string: str = ''
        for i in range(len(credit_card_num)):
            if i % 2 == 0:
                string += str(int(credit_card_num[i])*2)
            else:
                string += credit_card_num[i]

        sum: int = 0
        for digit in string:
            sum += int(digit)

        if sum % 10 == 0:
            print(valid_msg)
        else:
            print(invalid_msg)


if __name__ == '__main__':
    main()
