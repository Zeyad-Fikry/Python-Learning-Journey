items = []
price = []
print ("***** Welcome to iShop calculator *****")
num_of_items = int(input ("How many items are there in your basket today? "))
print ("Let's get to counting them ....")
for i in range (1,num_of_items+1) :
    item = input (f"Please tell me the name of the item number {i} ")
    items.append (item)
    price.append (float(input (f"What is the price of {item}\n$")))
ask_for_see_item = input ("Would You like to see your entire basket item? ").lower ()
if ask_for_see_item == "yes":
    print (items)
ask_for_see_price = input ("Would You like to see how muck it'll cost? ").lower ()
if ask_for_see_price == "yes":
    print ("Buying these item will cost:")
    print (sum(price))