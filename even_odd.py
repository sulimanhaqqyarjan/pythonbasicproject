n=int(input('Enter a number : '))

while(n<50):

    if n%2==0:
        print(f'{n}  is even number  ')
    else:
        print(f'{n} is odd number  ')
    n = int(input('Enter a number : '))

if n>50:
    print(f'{n} you enter  something wrong')