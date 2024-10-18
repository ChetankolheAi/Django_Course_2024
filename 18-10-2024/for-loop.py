fruits = ["banana","mango"]

# j = 0
# for i in fruits:
#     if(i=="banana"):
#         x=i.capitalize()
#         fruits[j]=x
#     j=j+1;
# print(fruits)

# for i in fruits:
#     if(i=="mango"):
#         x=i.capitalize()
#         fruits[fruits.index("mango")]=x
# print(fruits)

# for i in fruits:
#     if(i=="mango"):
#         break
# else:
#     print("Chetan")


#for loop for string
for i in fruits:
    if(i=="banana"):
        for j in i:
            print(j)