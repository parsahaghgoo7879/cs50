x = input("What is the Answer of  the Great Question of Life, the Universe, and Everything? ").lower().strip()

if x == ("42"):
    print("yes")

elif x == ("forty two"):
    print("yes")

elif x == ("forty_two"):
    print("yes")

else:
    print("no")