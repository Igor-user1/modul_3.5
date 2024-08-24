def get_multiplied_digits(number):
    number = int(number)
    str_number = str(number)
    if len(str_number) == 1:
        return int(str_number)

    first = int(str_number[0])

    if len(str_number[1:]) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        if first == 0:
            return 1*int(str_number[1])
        else:
            return first*int(str_number[1])


re = get_multiplied_digits(354056)
print(re)
