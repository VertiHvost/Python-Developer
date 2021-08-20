def calc(line):
    print(f'Total {line}')
    operand_1, opertion, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if opertion == '+':
        value = operand_1 + operand_2
    elif opertion == '-':
        value = operand_1 - operand_2
    elif opertion == '/':
        value = operand_1 / operand_2
    elif opertion == '*':
        value = operand_1 * operand_2
    elif opertion == '//':
        value = operand_1 // operand_2
    elif opertion == '%':
        value = operand_1 % operand_2
    else:
        print(f'Unknown operand {opertion}')
    return value

total = 0
with open('calc.txt', 'r') as ff:
    for line in ff:
       try:
           total= calc(line)
       except ValueError as exc:
           print(f'Не могу вычисьить')
print(f'Total {total}')
