#PERMUTATION
print('Permutation')
def fact(n):
    if(n>=1):
        return  n*fact(n-1)
    else:
        result=1
        return result
n=(int(input("Enter any number to find it's Permutation ")))
r=int(input('Enter your selected number '))

print(fact(n)/fact(n-r))
