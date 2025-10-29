import math

# --- Safe import for PC testing (mock ti_plotlib) ---
try:
    import ti_plotlib as plt
except ImportError:
    import matplotlib.pyplot as plt
    class _MockPlot:
        def __init__(self):
            self.zoom = 10
        def cls(self): plt.clf()
        def window(self, xmin, xmax, ymin, ymax): plt.axis([xmin, xmax, ymin, ymax])
        def axes(self, on): pass
        def grid(self, x, y, color): plt.grid(True)
        def color(self, r, g, b): plt.gca().set_prop_cycle(None)
        def plot(self, x, y, s): plt.plot(x, y, 'o-')
        def line(self, x1, y1, x2, y2): plt.plot([x1, x2], [y1, y2], 'gray')
        def text(self, x, y, s): plt.text(x, y, s)
        def show_plot(self): plt.show()
    plt = _MockPlot()

# ======== TRANSFORMATION FUNCTIONS ========

def reflect_point(x, y, mode, k=0):
    # axis modes: 1:x-axis, 2:y-axis, 3:y=x, 4:y=-x, 5:x=k, 6:y=k
    if mode == 1:  # x-axis
        return x, -y
    elif mode == 2:  # y-axis
        return -x, y
    elif mode == 3:  # y = x
        return y, x
    elif mode == 4:  # y = -x
        return -y, -x
    elif mode == 5:  # x = k
        return 2 * k - x, y
    elif mode == 6:  # y = k
        return x, 2 * k - y
    return x, y

def translate_point(x, y, a, b):
    return x + a, y + b

def rotate_point(x, y, angle, about=(0, 0)):
    ox, oy = about
    x -= ox
    y -= oy
    rad = math.radians(angle % 360)
    xr = x * math.cos(rad) - y * math.sin(rad)
    yr = x * math.sin(rad) + y * math.cos(rad)
    return round(xr + ox, 4), round(yr + oy, 4)

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

def auto_window(points, margin=2):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    xmin, xmax = min(xs)-margin, max(xs)+margin
    ymin, ymax = min(ys)-margin, max(ys)+margin
    return xmin, xmax, ymin, ymax

def plot_shapes(orig_pts, new_pts):
    zoom = 1.0
    while True:
        plt.cls()
        all_pts = orig_pts + new_pts
        xmin, xmax, ymin, ymax = auto_window(all_pts)
        xmid = (xmax + xmin)/2
        ymid = (ymax + ymin)/2
        width = (xmax - xmin)/2 * zoom
        height = (ymax - ymin)/2 * zoom
        plt.window(xmid - width, xmid + width, ymid - height, ymid + height)
        plt.axes("on")
        plt.grid(1, 1, "gray")

        # Preimage (blue)
        ox = [p[0] for p in orig_pts] + [orig_pts[0][0]]
        oy = [p[1] for p in orig_pts] + [orig_pts[0][1]]
        plt.color(0, 0, 255)
        plt.plot(ox, oy, "o")

        # Image (red)
        nx = [p[0] for p in new_pts] + [new_pts[0][0]]
        ny = [p[1] for p in new_pts] + [new_pts[0][1]]
        plt.color(255, 0, 0)
        plt.plot(nx, ny, "o")

        plt.show_plot()
        print("\nOptions:")
        print("[+] zoom in | [-] zoom out")
        print("[t] trace points | [b] table view | [Enter] exit graph")
        z = input(">").strip().lower()
        if z == "+":
            zoom = zoom / 1.5
        elif z == "-":
            zoom = zoom * 1.5
        elif z == "t":
            trace_points(orig_pts, new_pts)
        elif z == "b":
            show_table(orig_pts, new_pts)
        else:
            break

# ======== TRACE MODE ========

def trace_points(orig, new):
    i = 0
    n = len(orig)
    while True:
        print("\nTrace mode:")
        print("Preimage " + str(i+1) + ": " + str(orig[i]))
        print("Image    " + str(i+1) + ": " + str(new[i]))
        cmd = input("[n] next | [p] previous | [Enter] exit: ").lower().strip()
        if cmd == "n":
            i = (i + 1) % n
        elif cmd == "p":
            i = (i - 1) % n
        else:
            break

# ======== TABLE MODE ========

def show_table(orig, new):
    print("\n#   Preimage (x, y)       Image (x, y)")
    print("------------------------------------------")
    for i in range(len(orig)):
        o = orig[i]
        n = new[i]
        line = str(i+1) + "  (" + str(round(o[0],2)) + ", " + str(round(o[1],2)) + ")  ->  (" + str(round(n[0],2)) + ", " + str(round(n[1],2)) + ")"
        print(line)
    input("\nPress ENTER to return...")

# ======== OPERATION HANDLERS ========

def transform(points):
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
        print("5: x = k")
        print("6: y = k")
        mode = int(input("Choose: "))
        k = 0
        if mode == 5 or mode == 6:
            k = float(input("Enter k value: "))
        for pt in points:
            x, y = pt
            result.append(reflect_point(x, y, mode, k))

    elif choice == 2:
        print("\nEnter translation vector <a, b>")
        a = float(input(" a: "))
        b = float(input(" b: "))
        for pt in points:
            x, y = pt
            result.append(translate_point(x, y, a, b))

    elif choice == 3:
        angle = float(input("\nEnter rotation angle (degrees): "))
        aboutx = float(input("Rotate about x: "))
        abouty = float(input("Rotate about y: "))
        for pt in points:
            x, y = pt
            result.append(rotate_point(x, y, angle, (aboutx, abouty)))

    return result

# ======== MODES ========

def numeric_mode():
    points = get_points()
    result = transform(points)
    print("\n--- RESULTS ---")
    for i in range(len(points)):
        print("Point " + str(i+1) + ": " + str(points[i]) + " -> " + str(result[i]))
    input("\nPress ENTER to continue...")

def graph_mode():
    points = get_points()
    result = transform(points)
    plot_shapes(points, result)

# ======== MAIN MENU ========

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
