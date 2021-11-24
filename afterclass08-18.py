stack = []

def push(value):
    stack.append(value)
    
def pop(value):18

    if not empty():
        return stack.pop()
    else:
        return None

def empty():
    return len(stack)==0

def display():
    for i in stack:
        print(i, end=" ")
    print()
    
num = int(input())
number = num
while num != 0:
    if num%2==0:
        stack.append('0')
        num = num // 2
    else:
        stack.append('1')
        num = num // 2
i =0
b =""
while i < len(stack):  
    x = stack.pop()
    b = b + x
    
print('Liczba naturalna: ',number,' Liczba binarna: ',b)
   