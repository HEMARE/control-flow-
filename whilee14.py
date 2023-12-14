      

count=0
while count < 3:
    print('Inside loop')
    count = count + 1
else:
    print('Inside else')

for string in "Python Loops":  
    if string == "o" or string == "p" or string == "t":  
         continue  
    print('Current Letter:', string)   