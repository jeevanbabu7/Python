from random import randint

print("______Menu______")
n = int(input("Enter 1 to start" ))
while(n):
    k = input("Do you want to roll y/n")
    if(k.lower()!='y'):
        break
    print("Generated value = ",randint(1,6))