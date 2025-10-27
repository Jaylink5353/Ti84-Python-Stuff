import math
import ti_plotlib as plt

# ======== TRANSFORMATION FUNCTIONS ========

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

# ======== GRAPHING ========

def plot_points(orig_pts, new_pts):
    plt.cls()
    plt.window(-10, 10, -10, 10)
    plt.axes("on")
    plt.grid(1, 1, "gray")

    # Plot original points (blue)
    ox = [p[0] for p in orig_pts]
    oy = [p[1] for p in orig_pts]
    plt.color(0, 0, 255)
    plt.plot(ox, oy, "o")

    # Plot transformed points (red)
    nx = [p[0] for p in new_pts]
    ny = [p[1] for p in new_pts]
    plt.color(255, 0, 0)
    plt.plot(nx, ny, "o")

    # Optionally connect corresponding points
    plt.color(128, 128, 128)
    for i in range(len(orig_pts)):
        plt.line(ox[i], oy[i], nx[i], ny[i])

    plt.show_plot()
    input("\nPress ENTER to continue...")

# ======== MAIN MENUS ========

def numeric_mode():
    points = get_points()
    result = []

    print("\n--- Choose Transformation ---")
    print("1: Reflection")
    print("2: Translation")
    print("3: Rotation")
    choice = int(input("Choose: "))

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

def graph_mode():
    points = get_points()
    print("\n--- Choose Transformation ---")
    print("1: Reflection")
    print("2: Translation")
    print("3: Rotation")
    choice = int(input("Choose: "))

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

    plot_points(points, result)

# ======== PROGRAM ENTRY ========

def main():
    while True:
        print("\n=== GEOMETRIC TRANSFORMATIONS ===")
        print("1: Coordinate Mode")
        print("2: Graphing Mode")
        print("3: Quit")
        choice = int(input("Choose: "))

        if choice == 1:
            numeric_mode()
        elif choice == 2:
            graph_mode()
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()
