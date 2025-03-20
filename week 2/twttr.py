

word = input("input: ")
 vowels = ["a","e","i","u","o"]
 
 for i in word:
     if i.lower() in vowels:
         word = word.replace(i,"")
         
print("output:",word)