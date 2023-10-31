### chack numbers even or odd

def chack():
    print('---Please put a space between numbers---')
    text = input('input numbers : ')
    numbers = text.split(' ')
    odd = []
    even = []
    for number in numbers:
        try:
            if int(number)%2 == 0:
                even.append(number)
            else:
                odd.append(number) 
        except:
            return "---- Only numbers should be entered ----"
    return even, odd

even, odd = chack()  
print(f'Even numbers` {even}')
print(f'Odd numbers` {odd}')
