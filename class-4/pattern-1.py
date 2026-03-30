'''
Pattern-3:
* * * * *
*       *
*       *
*       *
*       *
*       *
* * * * *
'''

# print("* * * * *")
# print("*       *")
# print("*       *")
# print("*       *")
# print("* * * * *")

'''
Nested loop -> একটা লুপের ভিতরে আরেকটা লুপ
Outer loop -> বাইরের লুপ -> লাইন যতগুলো ততবার রান হবে -> 7
Inner loop -> ভিতরের লুপ -> স্টার প্রিন্ট করা
Pattern = পানি হয়ে যাবে
'''

i = 1
while i < 8:
    j = 1
    while j < 6:
        print("*", end="")
        j = j + 1
    print("")
    i = i + 1