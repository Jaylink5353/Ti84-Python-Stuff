import math

def reflect_point(x, y, axis):
    if axis == 1:   # x-axis
        return x, -y
    elif axis == 2: # y-axis
        return -x, y
    elif axis == 3: # y = x
        return y, x
    elif axis == 4: # y = -x
        return -y, -x
    else:
        return x, y

def translate_point(x, y, a, b):
    return x + a, y + b

def rotate_point(x, y, angle):
    angle = angle % 360
    if angle == 90:
        return -y, x
    elif angle == 180:
        return -x, -y
    elif angle == 270:
        return y, -x
    else:
        # For custom angle support (if desired)
        rad = math.radians(angle)
        xr = x * math.cos(rad) - y * math.sin(rad)
        yr = x * math.sin(rad) + y * math.cos(rad)
        return round(xr, 4), round(yr, 4)

def get_points():
    pts = []
    n = int(input("How many points? "))
    for i in range(n):
        print("Point", i + 1)
        x = float(input(" x: "))
        y = float(input(" y: "))
        pts.append((x, y))
    return pts

def main():
    while True:
        print("\n--- GEOMETRIC TRANSFORMATIONS ---")
        print("1: Reflection")
        print("2: Translation")
        print("3: Rotation")
        print("4: Quit")
        choice = int(input("Choose: "))
        
        if choice == 4:
            print("Goodbye!")
            break

        points = get_points()
        result = []

        if choice == 1:
            print("\nReflect over:")
            print("1: x-axis")
            print("2: y-axis")
            print("3: y = x")
            print("4: y = -x")
            axis = int(input("Choose: "))
            for (x, y) in points:
                result.append(reflect_point(x, y, axis))

        elif choice == 2:
            print("\nEnter translation vector <a, b>")
            a = float(input(" a: "))
            b = float(input(" b: "))
            for (x, y) in points:
                result.append(translate_point(x, y, a, b))

        elif choice == 3:
            print("\nRotate about origin by:")
            print("90, 180, 270 degrees")
            angle = int(input("Angle: "))
            for (x, y) in points:
                result.append(rotate_point(x, y, angle))

        print("\n--- RESULTS ---")
        for i in range(len(points)):
            print("Point", i+1, "→", result[i])

        input("\nPress ENTER to continue...")

main()
