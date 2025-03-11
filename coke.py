[[]]
amount_due = 50

while amount_due > 0:
    print(f"Amount Dou: {amount_due}")

    payment = input("insert coin: ")

    payment = int(payment)
    
    if payment in [25,10,5]:
    
        amount_due -= payment
    

    else:
        continue
print(f"Change Owde: {abs(amount_due)}")