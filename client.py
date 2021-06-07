from session import Session

help_message = 'Choose number:\n' \
               '1: get my friends\n' \
               '2: get person`s friends\n' \
               'or type exit \n'


def main():
    session = Session()
    command = input(help_message)
    while command != 'exit':
        if command == '2':
            print(session.get_friends(input('Type user`s id: ')))
        elif command == '1':
            print(session.get_friends())
        else:
            print('Unknown command')
        command = input(help_message)


if __name__ == '__main__':
    main()
