import sys
import os


def mainMenu():
    while True:
        print("Command Line Todo application\n ==================\n-l List all the tasks\n-a Adds a new task\n-r Removes a task\n-c Completes a task\n")

        val1 = input()

        if val1 == "-l":
            displayList()
        elif val1 == "-a":
            val2 = input()
            addItem(val2)
        elif val1 == "-r":
            val2 = int(input())
            removeItem(val2)
        elif val1 == "-c":
            val2 = int(input())
            checkItem(val2)
        else:
            print("Unsupported argument.")


def displayList():
    file_size = os.path.getsize('shitlist.txt')
    if file_size == 0:
        print("No todos today :)")

    else:
        text_file = open("shitlist.txt", "r")
        lines = text_file.readlines()
        i = 0
        for line in lines:
            print(str(i) + ". " + "[ ] " + line)
            i = i + 1


def addItem(val2):
    #    userIn = input("please enter your task item\n")
    fr = open('shitlist.txt', 'a')
    fr.write("\n" + val2)
    fr.close()


def removeItem(val2):
    #  userIn = input("please enter the line number you want to remove\n")
    try:
        kb = val2
        fr = open('shitlist.txt', 'r')
        lines = fr.readlines()
        del lines[kb - 1]
        print(lines)

        fr = open('shitlist.txt', 'w')
        for item in lines:
            fr.write("%s" % item)
        fr.close()

    except ValueError:
        kb = val2
        fr = open('shitlist.txt', 'r')
        lines = fr.readlines()
        lines[kb - 1] = "teez"
        print(lines)
        print("Unable to remove: no task number provided")


mainMenu()