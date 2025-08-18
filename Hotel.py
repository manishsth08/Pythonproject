# define the menu of the restaurant

menu = {
    'Pizza':40,
    'Coffee':25,
    'Burger':80,
    'Salad':70,
    'Pasta':50,
    }

#Greet

print('Welcome to Python Restaurant')
print('Pizza: Rs40\nCoffee: Rs25\nBurger: Rs80\nSalad: Rs70\nPasta: Rs50')

order_total=0

item_1 = input("Enter the name of item you want to order=")
if item_1 in menu:
   print("Your order has been placed")
else:
    print(f"Sorry,{item_1} is not available.Please enter from the menu selection")
