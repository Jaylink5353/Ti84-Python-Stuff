import math
import ti_plotlib as plt

# ======== TRANSFORMATION FUNCTIONS ========

def reflect_point(x, y, mode, k=0):
    # axis modes: 1:x-axis, 2:y-axis, 3:y=x, 4:y=-x, 5:x=k, 6:y=k
    if mode == 1: return x, -y
    if mode == 2: return -x, y
    if mode == 3: return y, x
    if mode == 4: return -y, -x
    if mode == 5: return 2*k - x, y
    if mode == 6: return x, 2*k - y
    return x, y

def translate_point(x, y, a, b):
    return x + a, y + b

def rotate_point(x, y, angle, aboutx, abouty):
    rad = math.radians(angle % 360)
    x -= aboutx
    y -= abouty
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
    print("\n#   Preimage (x, y)       Image (x, y)")
    print("------------------------------------")
    for i in range(len(orig)):
        ox, oy = orig[i]
        nx, ny = new[i]
        print(f"{i+1:<2} ({ox:>5.2f},{oy:>5.2f}) → ({nx:>5.2f},{ny:>5.2f})")
    input("\nPress ENTER...")

# ======== GRAPHING ========

def auto_window(points, margin=2):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    xmin, xmax = min(xs)-margin, max(xs)+margin
    ymin, ymax = min(ys)-margin, max(ys)+margin
    return xmin, xmax, ymin, ymax

def draw_shape(points, color):
    plt.color(*color)
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i+1) % len(points)]
        plt.line(x1, y1, x2, y2)
    for (x, y) in points:
        plt.plot(x, y, "o")

def plot_shapes(orig, new):
    zoom = 1.0
    while True:
        plt.cls()
        all_pts = orig + new
        xmin, xmax, ymin, ymax = auto_window(all_pts)
        xmid = (xmax + xmin)/2
        ymid = (ymax + ymin)/2
        width = (xmax - xmin)/2 * zoom
        height = (ymax - ymin)/2 * zoom
        plt.window(xmid - width, xmid + width, ymid - height, ymid + height)
        plt.axes("on")
        plt.grid(1, 1, "gray")

        draw_shape(orig, (0, 0, 255))
        draw_shape(new, (255, 0, 0))

        plt.show_plot()
        print("\n[+] zoom in | [-] zoom out | [t] table | [Enter] exit")
        z = input(">").strip().lower()
        if z == "+": zoom /= 1.5
        elif z == "-": zoom *= 1.5
        elif z == "t": show_table(orig, new)
        else: break

# ======== MAIN TRANSFORM FUNCTION ========

def transform(points):
    print("\n--- Choose Transformation ---")
    print("1: Reflection")
    print("2: Translation")
    print("3: Rotation")
    choice = int(input("Choose: "))
    result = []

    if choice == 1:
        print("\nReflect over:")
        print("1:x-axis  2:y-axis  3:y=x  4:y=-x  5:x=k  6:y=k")
        mode = int(input("Choose: "))
        k = 0
        if mode in [5, 6]:
            k = float(input("Enter k: "))
        for (x, y) in points:
            result.append(reflect_point(x, y, mode, k))

    elif choice == 2:
        a = float(input("Translate x by: "))
        b = float(input("Translate y by: "))
        for (x, y) in points:
            result.append(translate_point(x, y, a, b))

    elif choice == 3:
        angle = float(input("Rotation angle: "))
        aboutx = float(input("About x: "))
        abouty = float(input("About y: "))
        for (x, y) in points:
            result.append(rotate_point(x, y, angle, aboutx, abouty))

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
    while True:
        print("\n=== GEOMETRIC TRANSFORMATIONS ===")
        print("1: Coordinate Mode")
        print("2: Graphing Mode")
        print("3: Quit")
        c = input("Choose: ").strip()
        if c == "1": numeric_mode()
        elif c == "2": graph_mode()
        elif c == "3": break
        else: print("Invalid")

main()
