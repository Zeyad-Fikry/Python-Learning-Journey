own_books=[]
wish_books = []
own1 = input ("Enter the name of a book you own: ")
own_books.append(own1)
own2 = input ("Enter the name of another book you own (or press 'Enter' to skip): ")
if own2 :
    own_books.append(own2)
    print(f"\nYour Library: {own_books}\n")
else :
    print(f"\nYour Library: {own_books}\n")
#--------------------------------------------------------
wish1 = input ("Enter the name of a book you wish to have in the future: ")
wish_books.append(wish1)
wish2 = input ("Enter the name of another book you wish to have (or press 'Enter' to skip): ")
if wish2 :
    wish_books.append(wish2)
    print(f"\nYour Wishlist: {wish_books}\n")
else :
    print(f"\nYour Wishlist: {wish_books}\n")
#--------------------------------------------------------
to_own = input ("Enter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ")
if to_own in wish_books: # <-- (in)
    own_books.append(to_own)
    wish_books.remove(to_own)
    print (f"\nUpdated Library: {own_books}")
    print (f"Updated Wishlist: {wish_books}\n")
else:
    print (f"\nUpdated Library: {own_books}")
    print (f"Updated Wishlist: {wish_books}\n")
#--------------------------------------------------------
to_don = input ("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip): ")
if to_don in own_books: # <-- (in)
    own_books.remove(to_don)
    print (f"\nFinal Library after Donations: {own_books}\n")
else:
    print (f"\nFinal Library after Donations: {own_books}\n")