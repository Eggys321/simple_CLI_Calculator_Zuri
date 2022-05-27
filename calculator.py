first = float(input('Enter first Number => '))
second = float(input('Enter second Number => '))
opr = str(input('Enter operation (+, -, *, /, %) =>'))

if opr == '+':
    total = first + second
elif opr == '-':
    total = first - second
elif opr == '*':
    total = first * second
elif opr == '/':
    total = first / second
elif opr == '%':
    total = first % second
else:
    total = str('Please Enter A Valid Operation')
print (int(total))

