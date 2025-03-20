experssion = input("experssion: ")

x , y , z = experssion.split()

x = float(x)
z = float(z)

if y == "+":
    print(x + z)

elif y == "*":
    print(x * z)

elif y == "-":
    print(x - z)

elif y == "/":
    print(x / z)
