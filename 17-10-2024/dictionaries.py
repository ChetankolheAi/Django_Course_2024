temp ={33:{"Name":"Chetan","Div":"B","City":"Jalgaon"}, 3: "Ghaynasham"}
print(temp[33])


# #to access the values at random position
print(temp.get(33))



# #it return all the values from the dictionary in list
print(temp.values())



#Logic to print the keys and values from the dictionari 
for i in temp:
    print(i , temp[i])
    
    
    
#another methods
for x,y in temp.items():
    print(x,y)
    
    
    
#Dictionaries copy
copy = temp.copy()
print(copy)
  
#access the item from nested dictionaries
print(temp[33]["Name"])

#remove the values of given key
temp.pop(3)
print(temp)