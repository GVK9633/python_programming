
l1=[10,20,50,60,80,'nit']

#####

for i in l1:
    print(i)

# enumerater    
for i in enumerate(l1):
    print(i)
  
print(all(l1)); 
print(any(l1));  

numbers=[3,7,10,15]
print(all(num >0 for num in numbers))
print(any(num >10 for num in numbers))

  