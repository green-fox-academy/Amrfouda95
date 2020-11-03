b = int(input("Enter number of boys: "))

g = int(input("Enter number of girls: "))
if (b == g) and (b+g > 20):
   print("The party is exellent!")
elif (b != g) and (b+g > 20):
    print("Quit cool part!")
elif (b+g < 20):
    print("Average party...")
elif (g == 0):
    print("cock fest")