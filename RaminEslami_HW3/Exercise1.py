
numbers_of_one_to_twenty = {
    'one ': '1 ', 'two ': '2 ', 'three ': '3 ', 'four ': '4 ', 'five ': '5 ', 'six ': '6 ', 'seven ': '7 ',
    'eight ': '8 ', 'nine ': '9 ', 'ten ': '10 ', 'eleven ': '11 ', 'twelve ': '12 ', 'thirteen ': '13 ',
    'fourteen ': '14 ', 'fifteen ': '15 ', 'sixteen ': '16 ', 'seventeen ': '17 ', 'eighteen ': '18 ',
    'nineteen ': '19 ', 'twenty ': '20 ',
    #The following are program bugs in this file:
    'of10': 'often', 'one--': '1--'
}


def replace_dicti(text):
    """use dictionary for replace item"""
    for letter, number in numbers_of_one_to_twenty.items():
        text = text.replace(letter, number)
    return text


def create_newfile(filename, content):
    """Creating the desired file using the received filename and your content"""
    with open(f'new_{filename}', mode='w') as new_file:
        new_file.write(content)
    return None


def replace_number(filename):
    """
    This function is supposed to receive the zen.txt and create a new file in the output
    and replace the equivalent of English numbers from 1 to 20,
    for example, whenever it sees the nine, it will replace it with 9.

    :param filename: The name of the file to be read
    :return: Create a new modified file(with a success message in terminal)
    """
    try:
        with open(filename, mode='r') as file:
            text = file.read()
        text = replace_dicti(text)
        create_newfile(filename, text)

    except FileNotFoundError:
        print('Your file not found, please check it and try again(Our program is case sensitive, please check)')

    else:
        print('your file is created successful')


def main():
    file_name = input()
    replace_number(file_name)


if __name__ == "__main__":
    main()
