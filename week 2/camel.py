
from week 2.camel import camel

camel = input("camelcase: ")

for i in camel:
    if i.isupper():
        camel = camel.replace(i,"_"+i.lower())
        print(camel)
         