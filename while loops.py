#While Loops

#Display numbers from 1 to 10
counter = 1     #control Variable
while counter <= 10:  #condition
    print(counter, end = " ")
    counter += 1 # change 

print("\n\n")
#pin number verification

pin = int(input("Enter your pin number: "))
while pin != 1234:
    print("Incorrect pin")
    pin = int(input("Enter the correct pin: "))

print("access granted")
