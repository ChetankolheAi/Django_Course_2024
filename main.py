a ="chetAn kolhe"
print("Chetan" in a)#return true if yes and false if no

#print the string in column
for i in a:
    print(i)
    
    
#return the length of the string
print(len(a))

#return the last element of the string # this method is called negative Indexing
print(a[-1])


#This Return the string with Uppercase
print(a.upper())


#this returns the stirng with Lower
print(a.lower())


#Convert the first character of sting to upper case
print(a.capitalize())

#use to remove the white spaces from the  beginning or the end:
print(a.strip())

#This replace the substring in the main string
print(a.replace("h" , "H"))

#it devide the string on the basis of string given split function
print(a.split(" "))

#F-string
x = f"My name is {a}"
print(x)


#return  true if the string contain only spaces no character at allS
print(a.isspace())


#return true if the all the character are numeric in the string
#isnumeric also allowes " % ", "---"Character as well where as is digit not
print("一".isnumeric()) 
print("²".isnumeric()) 


#return true if all the character are digit in the string
print(a.isdigit())

#return true if all the charaxter are alphabet in the string
print(a.isalpha())

#it make first character of every word in the string in Upper case
print(a.title())