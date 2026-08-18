def operators(num1,num2):
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
    print(num1/num2)
    print(num1%num2)
    print(num1//num2)
    print(num1**num2)

operators(10,2)

def assignmentOperator():
    x=2
    print(x&3)


assignmentOperator()

'''walrus Operator'''
def walrusOperator(number):
    if (count :=len(number))>3:
        print(1)
    else:
        print(0)
walrusOperator([1,2,3,4,5,6,7,8,9,0])

'''
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
'''
'''
Operator |	Description	Example	
is 	     |  Returns True if both variables are the same object	x is y	
is not	 |  Returns True if both variables are not the same object	x is not y
'''
print("---------------")
def identityOperator():
    x=[1,3]
    y=[1,3]
    if x is y:
        print(1)
    if x is not y:
        print(2)
    else:
        print(3)

identityOperator()