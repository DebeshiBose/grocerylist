Greetings = '''Dear <|NAME|>,
Welcome in Virtual Mart. 
We are glad that you are here!
Have a great day ahead!
'''
name = input("Enter Your Name\n")
Greetings = Greetings.replace("<|NAME|>", name)
print(Greetings)

Items = {
    "FLour": {"Ashirwad" : 35, "Ganesh" : 50, "Forture" : 65},
    "Sugar": {"Bajaj" : 55, "Tata" : 74, "SugarFree": 46},
    "Oil": {'Fortune' : 46, "Suffola" : 60, "Emami" : 27}
}
print("Options are ", Items.values())

grocery_history = []
stop = False

while not stop:
    name = input("item_name:\n")
    quantity = input("Quantity purchased:\n")
    cost = ("Cost per item: Ashirwad-35\n Ganesh- 50 \n Fortune- 65 \n Bajaj-55 \n Tata- 74 \n SugarFree-46\n Fortune- 36 \n Suffolla- 60 \n Emami-27")
    print(cost)
    Cost= input("Cost of item :\n")

    grocery_item = {"item_name": name,"quantity": int(quantity), "Cost":float(Cost) }
    print(grocery_item)
    grocery_history.append(grocery_item)

    response = input("would you like to enter another item?\nType 'Y' for continue or 'N' to quit:\n")

    if response == 'N' :
        stop = True

grand_total = 0

for item in grocery_history:
    item_total = item['quantity'] * item['Cost']
    grand_total += item_total
    print("%d %s @ ₹%f ₹%f" %(item['quantity'], item['item_name'], item['Cost'], item_total)) #2 "f" because cost and item total can be in float.

    item_total = 0

print("Grand Total: ₹%f" % grand_total)
print('-------------------------------------------------')
Exit='''Thank you for shopping with us!
We hope to see you again'''
print(Exit)