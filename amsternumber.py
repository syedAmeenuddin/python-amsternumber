

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello worl")
num = 1
print(num % 10)
print(num//10)
# for i in range(10):
#     num = i
#     i +=1
#     print('from here i {}'.format(i))
#     n=len(str(i))
#     result=0
#     while i<=0:
#         i=i%10
#         result= result+i**n        # print(result)
#     if(num == result):
#         print(num)
print('here')
for i in range(1000):
    num = i
    i += 1
    n = len(str(i))
    result = 0
    print(result)
    while i != 0:
        print(i)
        i = i % 10
        result = result+i**n
        i = num//10

    if num == result:
        print(result)
