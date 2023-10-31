####   caculator

def caculator():
    print('---Please put a space between numbers and actions---')
    text = input('input expression : ')
    sup = text.split(' ')
    try:
        first_number = float(sup[0])
        second_number = float(sup[2])
    except:
        return 'The imported numbers must be float'
    math_op = sup[1]
    output_text = f'{first_number} {math_op} {second_number} = '
    if math_op == '*':
        return output_text + str(first_number*second_number)
    elif math_op == '/':
        return output_text + str(round(first_number/second_number, 3))
    elif math_op == '-':
        return output_text + str(first_number-second_number)
    elif math_op == '+':
        return output_text + str(first_number+second_number)
    else:
        return 'Possible mathematical operations: {*, /, -, +}'
    
print(caculator())