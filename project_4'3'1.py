print ("Welcome to place the rabbit\n")
felid = [["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]]
print (f"{felid[0]}\n{felid[1]}\n{felid[2]}")
print ("Where should the rabbit go?🐇")
place = input("Please choose a row and a column ")
row = int(place[0])-1
col = int(place[1])-1
felid[row] [col] = "🐇"
print("\n Success ....\n")
print (f"{felid[0]}\n{felid[1]}\n{felid[2]}")