import sys
import os

print(sys.argv)
def mainMenu():
    while True:
        print(
            "Command Line Todo application\n ==================\n-l List all the tasks\n-a Adds a new task\n-r Removes a task\n-c Completes a task\n")

        s = input()
        l = s.split(' ')

        if l[0] == "-l":
            displayList()
        elif l[0] == "-a":
            addItem(l[1])
        elif l[0] == "-r":
            removeItem(l[1])
        elif l[0] == "-c":
            checkItem(l[1])
        else:
            print("Unsupported argument.")


def displayList():
    file_size = os.path.getsize('mylist.txt')
    if file_size == 0:
        print("No todos today :)")

    else:
        text_file = open("mylist.txt", "r")
        lines = text_file.readlines()
        i = 1
        for line in lines:
            print(str(i) + ". " + line)
            i = i + 1


def addItem(val2):

    fr = open('mylist.txt', 'a')
    fr.write("\n" + val2)
    fr.close()


def removeItem(val2):

    try:
        kb = int(val2)
        fr = open('mylist.txt', 'r')
        lines = fr.readlines()
        del lines[kb - 1]
        print(lines)

        fr = open('mylist.txt', 'w')
        for item in lines:
            fr.write("%s" % item)
        fr.close()

    except ValueError:
        print("Unable to remove: no task number provided")


def checkItem(val2):
    kb = val2
    fr = open('mylist.txt', 'r')
    lines = fr.readlines()
    lines[int(kb) - 1] = "[*]" + lines[int(kb) - 1] + "\n"
    print(lines)

    fr = open('mylist.txt', 'w')
    for item in lines:
        fr.write("%s" % item)
    fr.close()


mainMenu()