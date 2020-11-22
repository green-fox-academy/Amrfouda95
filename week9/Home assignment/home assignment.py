val = input("Command Line Todo application\n ==================\n-l List all the tasks\n-a Adds a new task\n-r Removes a task\n-c Completes a task\n")

if val == "l":
    fr = open('mylist.txt','r')
    test = fr.read()
    print (test)
    fr.close()

elif val == "a":
    userIn = input("please enter your task item\n")
    fr = open('mylist.txt', 'a')
    fr.write("\n" + userIn)
    fr.close()











