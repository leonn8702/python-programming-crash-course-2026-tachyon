'''
Even or Odd -> জোড় নাকি বিজোড় 
'''
x = int(input("Enter a number: "))
print(type(x))

if x % 2 == 0:
    print("Even")
if x % 2 != 0:
    print("Odd")