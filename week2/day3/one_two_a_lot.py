num = int(input("Enter a number: "))
if (num <= 0):
   print("{0} is not enough".format(num))
elif (num == 1):
    print("{0} is one".format(num))
elif (num == 2):
    print("{0} is two".format(num))
else:
   print("{0} is a lot".format(num))