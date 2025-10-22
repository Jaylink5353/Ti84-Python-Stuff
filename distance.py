import math

def simplify_sqrt(n):
    """Simplify the square root of n (return a, b such that sqrt(n) = a√b)."""
    a = 1
    b = n
    i = 2
    while i * i <= b:
        while b % (i * i) == 0:
            b //= i * i
            a *= i
        i += 1
    return a, b

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
        squared_distance = dx**2 + dy**2
        distance = math.sqrt(squared_distance)

        # Simplify the radical
        a, b = simplify_sqrt(int(squared_distance))

        print("\nResults:")
        if b == 1:
            print(f"Exact distance: {a}")
        else:
            print(f"Exact distance: {a}√{b}")
        print(f"Decimal distance: {distance}\n")

        choice = input("Type 1 to continue, type 0 to exit: ")
        if choice == "0":
            print("Exit")
            break

main()
