def input_numbers():
    print('---Please put a space between numbers---')
    text = input('input numbers : ')
    list_integers = []
    list_of_numbers = text.split(" ")
    for number in list_of_numbers:
        try:
            if int(number):
                list_integers.append(float(number))
        except:
            if number[0] == '-':
                list_integers.append(float(number))
                continue
            else:
                return "---- Only numbers should be entered ----"
    return list_integers  

def sum_of_elements(list_of_numbers, exclude_negative=False):
    if type(list_of_numbers) == str:
        return list_of_numbers
    if exclude_negative:
        summ = 0
        for num in list_of_numbers:
            summ += max(0,num)
    else:
        print(list_of_numbers)
        summ = sum(list_of_numbers)
    return summ

list_of_numbers = input_numbers()
print("outpute` ",sum_of_elements(list_of_numbers, exclude_negative = True))
