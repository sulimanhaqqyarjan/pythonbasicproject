#FACTORIAL
print('factorial')
def fact(n):
    if(n>=1):
        return  n*fact(n-1)
    else:
        result=1
        return result
#n=(int(input("Enter any number to find it's factorial ")))
#print(fact(n))




#PERMUTATION
print('Permutation')
def fact(n):
    if(n>=1):
        return  n*fact(n-1)
    else:
        result=1
        return result
#n=(int(input("Enter any number to find it's Permutation ")))
#r=int(input('Enter your selected number '))

#print(fact(n)/fact(n-r))





#COMBINATION
print('combination')
def fact(n):
    if(n>=1):
        return  n*fact(n-1)
        #if(r>=1):
            #return r*fact(r-1)
    else:
        result=1
        return result
n=(int(input("Enter any number to find it's Combination ")))
r=int(input('Enter your selected number '))
formula=fact(n)/(fact(n-r)*fact(r))
print(formula)

print('r fact is ',fact(r))