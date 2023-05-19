from user3 import User
import pwinput


def main():
    while True:
        input_order = input('\n---------------------------------Welcome to App-------------------------------\n'
                            'Signup ----> enter number 1 \n'
                            'Login ----> enter number 2 \n'
                            'Exit ----> enter number 0 \n'
                            'Please insert your choice : ')

        match input_order:
            case "1":
                print('---------------------------------- Signup ----------------------------------\n\n'
                      'hint: The length of the password must be more than 4 characters\n')
                try:
                    username = input('Username: ')
                    password = pwinput.pwinput(prompt='Password: ', mask='*')
                    phone_number = input('Phone number (optional): ')
                    User.create_user(username, password, phone_number)
                    print('\n--- Your registration was successful ---\n')
                except Exception as e:
                    print(str(e))
            case "2":
                print('---------------------------------- Login ----------------------------------\n\n'
                      'hint: The length of the password must be more than 4 characters\n')
                try:
                    username = input('Username: ')
                    password = pwinput.pwinput(prompt='Password: ', mask='*')
                    user = User.login(username, password)
                    if user:
                        while True:
                            input_order = input(f'\n------------------------ Welcome {username} ----------------------'
                                                f'\n\n'
                                                f'Information ----> enter number 1 \n'
                                                f'Change username and phone number ----> enter number 2 \n'
                                                f'Change password ----> enter number 3 \n'
                                                f'Logout ----> enter number 4 \n'
                                                f'please insert your choice : ')
                            match input_order:
                                case '1':
                                    print('---------------------------- Information -------------------------------')
                                    print(user)
                                case '2':
                                    print('------------------------- Change information ---------------------------')
                                    try:
                                        new_username = input('new username (if you want update it): ')
                                        new_phone_number = input('new phone_number (if you want update it): ')
                                        if new_username == '':
                                            new_username = user.username
                                        if new_phone_number == '':
                                            new_phone_number = user.phone_number
                                        user = User.change_info(username, new_username, new_phone_number)
                                        if user is not str:
                                            print('\n--- your account is updated successfully ---')
                                    except Exception as e:
                                        print(str(e))
                                case '3':
                                    print('------------------------- Change Password ---------------------------')
                                    try:
                                        old_password = pwinput.pwinput('old_password : ')
                                        new_password = pwinput.pwinput('new_password : ')
                                        confirm_new_password = pwinput.pwinput('confirm_new_password : ')
                                        user = User.change_password(user, old_password, new_password,
                                                                    confirm_new_password)
                                        print('--- your password updated successfully ---')
                                    except Exception as e:
                                        print(str(e))
                                case '4':
                                    break
                                case _:
                                    print('invalid choice!')
                except Exception as e:
                    print(str(e))
            case "0":
                break
            case _:
                print('invalid choice!')


if __name__ == '__main__':
    main()
