import re


def is_ip(ip):
    result = True
    numbers = ip.split('.')
    for number in numbers:
        if not number.isdigit() or int(number) > 255 or int(number) < 0 or len(numbers) != 4:
            result = False
            break
    return result


def is_phone(phone_number):
    code = phone_number[0:4]
    number = phone_number[4:]
    if code != "+380":
        return False
    if not number.isdigit() or len(number) != 9:
        return False
    return True


def is_email(email):
    if not re.match("[^@]+@[^@]+\.[^@]+", email):
        return False
    return True


def is_date(date):
    numbers = date.split('/')
    if not numbers[0].isdigit() or len(numbers[0]) != 4:
        return False
    if not numbers[1].isdigit() or len(numbers[1]) != 2 or int(numbers[1]) < 0 or int(numbers[1]) > 12:
        return False
    if not numbers[2].isdigit() or len(numbers[2]) != 2 or int(numbers[1]) < 0 or int(numbers[1]) > 31:
        return False
    return True


def what_is(what):
    if is_ip(what):
        print('IP')
    elif is_phone(what):
        print("Phone number")
    elif is_email(what):
        print('Email')
    elif is_date(what):
        print('Date')
    elif not what:
        print('Please, enter dada!')
        what_is(input("Enter data: "))
    else:
        print('Unknown')


what_is(input("Enter data: "))
