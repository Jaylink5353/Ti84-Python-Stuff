import math
import ti_plotlib as plt

# ======== TRANSFORMATION FUNCTIONS ========

def reflect_point(x, y, mode, k):
    # axis modes: 1:x-axis, 2:y-axis, 3:y=x, 4:y=-x, 5:x=k, 6:y=k
    if mode == 1:
        return x, -y
    elif mode == 2:
        return -x, y
    elif mode == 3:
        return y, x
    elif mode == 4:
        return -y, -x
    elif mode == 5:
        return 2*k - x, y
    elif mode == 6:
        return x, 2*k - y
    else:
        return x, y

def translate_point(x, y, a, b):
    return x + a, y + b

def rotate_point(x, y, angle, aboutx, abouty):
    rad = math.radians(angle % 360)
    x = x - aboutx
    y = y - abouty
    xr = x * math.cos(rad) - y * math.sin(rad)
    yr = x * math.sin(rad) + y * math.cos(rad)
    return round(xr + aboutx, 2), round(yr + abouty, 2)

# ======== INPUT ========

def get_points():
    pts = []
    n = int(input("How many points? "))
    for i in range(n):
        print("Point", i + 1)
        x = float(input(" x: "))
        y = float(input(" y: "))
        pts.append((x, y))
    return pts

# ======== TABLE DISPLAY ========

def show_table(orig, new):
    print("")
    print("#   Preimage (x,y)     Image (x,y)")
    print("----------------------------------")
    for i in range(len(orig)):
        ox = orig[i][0]
        oy = orig[i][1]
        nx = new[i][0]
        ny = new[i][1]
        print(str(i+1) + "  (" + str(ox) + "," + str(oy) + ") -> (" + str(nx) + "," + str(ny) + ")")
    input("Enter to continue")

# ======== GRAPHING ========

def auto_window(points, margin):
    xs = []
    ys = []
    for p in points:
        xs.append(p[0])
        ys.append(p[1])
    xmin = min(xs) - margin
    xmax = max(xs) + margin
    ymin = min(ys) - margin
    ymax = max(ys) + margin
    return xmin, xmax, ymin, ymax

def draw_shape(points, r, g, b):
    plt.color(r, g, b)
    n = len(points)
    for i in range(n):
        x1 = points[i][0]
        y1 = points[i][1]
        x2 = points[(i + 1) % n][0]
        y2 = points[(i + 1) % n][1]
        plt.line(x1, y1, x2, y2)
    for p in points:
        plt.plot(p[0], p[1], "o")

def plot_shapes(orig, new):
    zoom = 1.0
    while True:
        plt.cls()
        all_pts = orig + new
        xmin, xmax, ymin, ymax = auto_window(all_pts, 2)
        xmid = (xmax + xmin) / 2
        ymid = (ymax + ymin) / 2
        width = (xmax - xmin) / 2 * zoom
        height = (ymax - ymin) / 2 * zoom
        plt.window(xmid - width, xmid + width, ymid - height, ymid + height)
        plt.axes("on")
        plt.grid()

        draw_shape(orig, 0, 0, 255)
        draw_shape(new, 255, 0, 0)

        plt.show_plot()
        print("")
        print("[+] zoom in, [-] zoom out")
        print("[t] table, [Enter] exit")
        z = input(">").strip().lower()
        if z == "+":
            zoom = zoom / 1.5
        elif z == "-":
            zoom = zoom * 1.5
        elif z == "t":
            show_table(orig, new)
        else:
            break

# ======== MAIN TRANSFORM FUNCTION ========

def transform(points):
    print("")
    print("--- Choose Transformation ---")
    print("1: Reflection")
    print("2: Translation")
    print("3: Rotation")
    choice = int(input("Choose: "))
    result = []

    if choice == 1:
        print("")
        print("Reflect over:")
        print("1:x-axis  2:y-axis  3:y=x  4:y=-x  5:x=k  6:y=k")
        mode = int(input("Choose: "))
        k = 0
        if mode == 5 or mode == 6:
            k = float(input("Enter k: "))
        for p in points:
            result.append(reflect_point(p[0], p[1], mode, k))

    elif choice == 2:
        a = float(input("Translate x by: "))
        b = float(input("Translate y by: "))
        for p in points:
            result.append(translate_point(p[0], p[1], a, b))

    elif choice == 3:
        angle = float(input("Rotation angle: "))
        aboutx = float(input("About x: "))
        abouty = float(input("About y: "))
        for p in points:
            result.append(rotate_point(p[0], p[1], angle, aboutx, abouty))

    return result

# ======== MODES ========

def numeric_mode():
    pts = get_points()
    new_pts = transform(pts)
    show_table(pts, new_pts)

def graph_mode():
    pts = get_points()
    new_pts = transform(pts)
    plot_shapes(pts, new_pts)

# ======== MAIN MENU ========

def main():
    plt.cls()
    while True:
        print("")
        print("=== GEOMETRIC TRANSFORMATIONS ===")
        print("1: Coordinate Mode")
        print("2: Graphing Mode")
        print("3: Quit")
        c = input("Choose: ").strip()
        if c == "1":
            numeric_mode()
        elif c == "2":
            graph_mode()
        elif c == "3":
            break
        else:
            print("Invalid")

main()
