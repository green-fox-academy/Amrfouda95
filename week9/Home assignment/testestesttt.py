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
    userIn = int(input("please enter the line number you want to remove\n"))
    def removeLine(userIn, mylist):
        f = open(mylist, "r+")
        d = f.readlines()
        f.seek(0)
        for i in range(len(d)):
            if i > userIn:
                f.write(d[i].replace(d[i].split(",")[0], str(i - 1)))
            elif i != userIn:
                f.write(d[i])
        f.truncate()
        f.close()








 #   a_file = open("mylist.txt", "r")
 #   lines = a_file.readlines()
 #   a_file.close()

   # new_file = open("mylist.txt", "w")
   # for line in lines:
    #    if line.strip("\n") != "line2":
      #      new_file.write(line)
  #  new_file.close()







 #   with open("mylist.txt", "r") as infile:
      #  lines =infile.readlines()
 #   with open("mylist.txt", "w") as outfile:
     #   for line in enumerate(lines):
       #     if  != 5:
     #           outfile.write(line)
  #  outfile.close()




    #fr = open('mylist.txt', 'a')
  #  lines = fr.readlines()
   # for line in lines:
     #   if line.strip("\n") != "nickname_to_delete":
       #     fr.write(line)
 #   fr.close()
