# a = 9
# if(a%2==0):
#     print("Even")
# else:
#     print("Odd")

# arr=[1,3,4,5,6,67]
# target = [0]
# for i in arr:
#     if i in target:
#         print("Number Present")
#         break
# else:
#     print("Number not Present")


a = int(input("Enter the Rollno Of student"))
if (a<=10):
    print("A Division")
elif(a>10 and a<=20):
    print("B Division")
elif(a>20 and a<=30):
    print("C Division")
else:
    print("Invalid Rollno")
    
if a in range(0,10):
    print("Successs")