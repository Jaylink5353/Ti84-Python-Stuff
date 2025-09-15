import math

def find_midpoint(x1, y1, x2, y2):
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    return mx, my

def calculate_length(endpoint_x, endpoint_y, midpoint_x, midpoint_y):
    dx = endpoint_x - midpoint_x
    dy = endpoint_y - midpoint_y
    half_length = math.sqrt(dx**2 + dy**2)
    return 2 * half_length

def find_missing_endpoint(mid_x, mid_y, known_x, known_y):
    missing_x = 2 * mid_x - known_x
    missing_y = 2 * mid_y - known_y
    return missing_x, missing_y

def main():
    while True:
        print("Midpoint Toolkit by Jamez x ChatGPT")
        print("1: Midpoint from endpoints")
        print("2: Length from endpoint + midpoint")
        print("3: Missing endpoint from midpoint + known")
        print("4: Exit")
        choice = input("Choose (1/2/3/4): ")

        if choice == "1":
            x1 = float(input("x1: "))
            y1 = float(input("y1: "))
            x2 = float(input("x2: "))
            y2 = float(input("y2: "))
            mx, my = find_midpoint(x1, y1, x2, y2)
            print("Midpoint:", mx, my)

        elif choice == "2":
            ex = float(input("Endpoint x: "))
            ey = float(input("Endpoint y: "))
            mx = float(input("Midpoint x: "))
            my = float(input("Midpoint y: "))
            length = calculate_length(ex, ey, mx, my)
            print("Total length:", length)

        elif choice == "3":
            mx = float(input("Midpoint x: "))
            my = float(input("Midpoint y: "))
            kx = float(input("Known endpoint x: "))
            ky = float(input("Known endpoint y: "))
            missing_x, missing_y = find_missing_endpoint(mx, my, kx, ky)
            print("Missing endpoint:", missing_x, missing_y)

        elif choice == "4":
            print("Exiting Geometry Toolkit. See you next time!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

main()