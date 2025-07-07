# Write your solution here
# limit = int(input("Limit: "))
# while True:
#     num = 1
#     num2 = 2
#     num = num+num2
#     num2 +=1
#     print(num)
#     if limit <= num:
#         break Trash code btw 
num = 1
numsum = 0
lim = int(input("Limit: "))
while lim > numsum:
    numsum = numsum + num
    num+= 1
    if numsum >= lim:
        print(numsum)
