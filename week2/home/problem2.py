print("The value inputted by the user should be 7 or more characters long and should have an odd number of characters")
text=input("The old string: ")
num= int((len(text))/2)-1
print("Middle 3 characters: ", text[num:num+3])
text1= text[num:num+3]
print ("The new string: "+text[:num]+text1.upper()+text[num+3:])