print ("Welcome to place the rabbit\n")
list1 = ["🌿","🌿","🌿"]
list2 = ["🌿","🌿","🌿"]
list3 = ["🌿","🌿","🌿"]
print (list1)
print (list2)
print (list3)
print ("Where should the rabbit go?🐇")
place = input("Please choose a row and a column ")
pla1 = int(place [0])
pla2 = int(place [1])
if pla1 == 1:
    if pla2 == 1:
        list1.remove("🌿")
        list1.insert(0,"🐇")
    elif pla2 == 2:
        list1.remove("🌿")
        list1.insert(1,"🐇")
    elif pla2 == 3:
        list1.remove("🌿")
        list1.insert(2,"🐇")
    else:
        print ("wrong number")
elif pla1 == 2:
    if pla2 == 1:
        list2.remove("🌿")
        list2.insert(0,"🐇")
    elif pla2 == 2:
        list2.remove("🌿")
        list2.insert(1,"🐇")
    elif pla2 == 3:
        list2.remove("🌿")
        list2.insert(2,"🐇")
    else:
        print ("wrong number")
elif pla1 == 3:
    if pla2 == 1:
        list3.remove("🌿")
        list3.insert(0,"🐇")
    elif pla2 == 2:
        list3.remove("🌿")
        list3.insert(1,"🐇")
    elif pla2 == 3:
        list3.remove("🌿")
        list3.insert(2,"🐇")
    else:
        print ("wrong number")
else:
    print ("wrong number")
print("\n Success ....\n")
print (list1)
print (list2)
print (list3)