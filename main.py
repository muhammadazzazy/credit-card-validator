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

        invalid_message: str = f'The credit card number {credit_card_num} is not valid.'
        valid_message: str = f'The credit card number {credit_card_num} is valid!'

        if not credit_card_num.isnumeric():
            print(invalid_message)
            continue

        if len(credit_card_num) != NUM_OF_DIGITS:
            print(invalid_message)
            continue

        if int(credit_card_num[0]) not in first_digits.values():
            print(invalid_message)
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
            print(valid_message)
        else:
            print(invalid_message)


if __name__ == '__main__':
    main()
