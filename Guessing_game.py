from random import randint

secret_value = randint(1,20)
print("____Instructions____")
print("1.You have three tries")
print("2.The secret number is in between 1-20 (1 and 20 inclusive)")
print("Enter 1 to start ")
n = int(input())
if(n==1):
    k = 3
    while(k):
        print(k,"Guesses Remaining")
        n = int(input("Enter your guess "))
        if(n<secret_value):
            print("Hint : Guessed value is less Secret number ")
        elif n>secret_value:
            print("Hint : Guessed value is greater than secret value ")
        elif n<1  and n>20:
            print("value is in between 1-20")
        else:
            break
        k-=1

    if k:
        print("Congratulations You won..!")
    else:
        print("Sorry you lost ","secret number  = ",secret_value)

