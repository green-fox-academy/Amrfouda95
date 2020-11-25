val = input("Command Line Todo application\n ==================\n-l List all the tasks\n-a Adds a new task\n-r Removes a task\n-c Completes a task\n")

import os

if val == "l":
    file_size = os.path.getsize('mylist.txt')
    if file_size == 0:
        print("No todos today :)")

    else :
        text_file = open("mylist.txt", "r")
        lines = text_file.readlines()
        i = 1
        for line in lines:
            print(str(i) + ". " + line)
            i = i + 1


elif val == "a":
    userIn = input("please enter your task item\n")
    fr = open('mylist.txt', 'a')
    fr.write("\n" + userIn)
    fr.close()

elif val == "r":
    userIn = input("please enter the line number you want to remove\n")
    try:
        kb = int(userIn)
        fr = open('mylist.txt', 'r')
        lines = fr.readlines()
        del lines[kb-1]
        print (lines)

        fr = open('mylist.txt', 'w')
        for item in lines:
            fr.write("%s" % item)
        fr.close()

    except ValueError:
        print("Unable to remove: no task number provided")














