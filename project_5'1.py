tasks = input ("Enter the tasks for today separated by commas: ").split(", ")
Done_Tasks = []
Ongoing_Tasks = []
for task in tasks:
    print(f"\n{task}\n")
    ask_for_con = input (f"Did you finish {task}? (yes/no): ").lower()
    if ask_for_con == "yes":
        print("Nice Job")
        Done_Tasks.append(task)
    else :
        print("Try not to put it off")
        Ongoing_Tasks.append(task)
    print ("------")
ask_for_see_progress = input ("Do you want to see your today's progress?(yes, no)")
if ask_for_see_progress == "yes":
    print("\n          ********** Done Tasks **********\n")
    print(Done_Tasks)
    print("\n          ********** Done Tasks **********\n")
    print(Ongoing_Tasks)