#Let's build robot Barista!

print("Hello, welcome to NetworkChuck Coffee!!!")

name = input("What is your name?\n")
if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you evil?\n")
    deeds = int(input("How many good deeds have you done today\n"))
    if evil_status == "Yes" and deeds < 4:
        print("You're not welcome here " + name + "!")
        exit()
else:
    print("Hello " + name + ", thank you so much for coming in today!!\n")
menu = "Black Coffee, Espresso, Latte, Cappuccino, Frappuccino"
print(name + ", what would you like from our menu today? Here is what we are serving:\n" + menu)
order = input()
if order == "Frappuccino":
    price = 13
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    price = 9
elif order == "Cappuccino":
    price = 10
else:
    print("Sorry, we don't have that here.")
    exit()
quantity = input("How many would you like?\n")
total = price * int(quantity)
print("Thank you. Your total price is " + str(total) + "$")
