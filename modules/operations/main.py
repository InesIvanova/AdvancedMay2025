from modules.operations.core import calculate

expression= input()

num1, sign, num2 = expression.split()
num1 = float(num1)
num2 = float(num2)

print(calculate(num1, num2, sign))