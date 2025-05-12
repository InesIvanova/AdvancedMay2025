word = list(input())

while word:
    print(word.pop(), end='')



text = list(input())
stack = []

for i in range(len(text)):
    stack.append(text.pop())

print("".join(stack))
