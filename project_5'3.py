all_names = input ("Enter the first and the last name of your friends separated by a comma: ")
names = all_names.split (", ") #* <--  become a list []
for fn_sn in names:
    print (fn_sn.split (" "))  #* <-- each name (First name and second name) become a list and print each name in each loop
print ("Abbreviated Names:")
for fn_sn in names:
    fn_and_sn = fn_sn.split (" ")
    print (fn_and_sn[0][0]+"."+fn_and_sn[1][0]+".")