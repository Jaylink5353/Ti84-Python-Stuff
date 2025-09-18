import math
def main():
    while True: 
        print("Made by Jaymes")
        # Prompt for coordinates of the first point
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))

        # Prompt for coordinates of the second point
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        # Calculate the distance
        dx = x2 - x1
        dy = y2 - y1
        distance = math.sqrt(dx**2 + dy**2)

        # Display the result
        print("The distance is:", distance)
        choice = input("Type 1 to continue, type 0 to exit: ")
        if choice == "0":
            print("Exit")
            break
    


main()