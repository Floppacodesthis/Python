import tkinter as tk
from tkinter import ttk, messagebox
from main import Calculator
import math

class CalculatorApp:
    def __init__(self, root):
        self.calc = Calculator()
        self.root = root
        self.root.title("Windows 11 Style Calculator")
        self.root.geometry("450x600")
        self.root.configure(bg="#1e1e1e")

        self.modes = ["Standard", "Scientific", "Geometry", "Profit/Loss", "Time Zone", "Length", "Weight", "Speed"]
        self.current_mode = tk.StringVar(value=self.modes[0])

        self.setup_ui()

    def setup_ui(self):
        sidebar = tk.Frame(self.root, bg="#2d2d2d", width=130)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        for mode in self.modes:
            b = tk.Button(sidebar, text=mode, bg="#2d2d2d", fg="white", font=("Segoe UI", 10, "bold"), bd=0,
                         activebackground="#0078D7", activeforeground="white",
                         command=lambda m=mode: self.switch_mode(m))
            b.pack(fill=tk.X, pady=2)

        self.main_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.display = tk.Label(self.main_frame, text="0", anchor="e", bg="#1e1e1e", fg="white",
                                font=("Segoe UI", 28), height=2)
        self.display.pack(fill=tk.X)

        self.panel_frame = tk.Frame(self.main_frame, bg="#1e1e1e")
        self.panel_frame.pack(fill=tk.BOTH, expand=True)

        self.create_panels()
        self.switch_mode(self.current_mode.get())

    def create_panels(self):
        self.panels = {}

        self.panels["Standard"] = self.create_standard_panel()
        self.panels["Scientific"] = self.create_scientific_panel()
        self.panels["Geometry"] = self.create_geometry_panel()
        self.panels["Profit/Loss"] = self.create_profit_panel()
        self.panels["Time Zone"] = self.create_time_panel()
        self.panels["Length"] = self.create_conversion_panel("Length", ["m", "km", "mi"])
        self.panels["Weight"] = self.create_conversion_panel("Weight", ["g", "kg", "lb"])
        self.panels["Speed"] = self.create_conversion_panel("Speed", ["m/s", "km/h", "mph"])

    def switch_mode(self, mode):
        self.current_mode.set(mode)
        for panel in self.panels.values():
            panel.pack_forget()
        self.panels[mode].pack(fill=tk.BOTH, expand=True)
        self.display.config(text="0")

    def create_standard_panel(self):
        return self.create_button_grid([
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "×"],
            ["C", "0", "=", "÷"]
        ], self.handle_standard_click)

    def create_scientific_panel(self):
        return self.create_button_grid([
            ["sin", "cos", "tan", "log"],
            ["exp", "^", "√", "π"],
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "×"],
            ["C", "0", "=", "÷"]
        ], self.handle_scientific_click)

    def create_geometry_panel(self):
        frame = tk.Frame(self.panel_frame, bg="#1e1e1e")
        ttk.Label(frame, text="Length:").pack(pady=5)
        self.len1 = tk.Entry(frame)
        self.len1.pack()
        ttk.Label(frame, text="Width:").pack(pady=5)
        self.len2 = tk.Entry(frame)
        self.len2.pack()
        ttk.Button(frame, text="Area", command=self.show_area).pack(pady=10)
        ttk.Button(frame, text="Hypotenuse", command=self.show_hypot).pack(pady=10)
        return frame

    def create_profit_panel(self):
        frame = tk.Frame(self.panel_frame, bg="#1e1e1e")
        ttk.Label(frame, text="Profit / Loss:").pack(pady=5)
        self.profit1 = tk.Entry(frame)
        self.profit1.pack()
        ttk.Label(frame, text="Base Price:").pack(pady=5)
        self.profit2 = tk.Entry(frame)
        self.profit2.pack()
        ttk.Button(frame, text="% Profit", command=self.show_profit).pack(pady=10)
        ttk.Button(frame, text="% Loss", command=self.show_loss).pack(pady=10)
        return frame

    def create_time_panel(self):
        frame = tk.Frame(self.panel_frame, bg="#1e1e1e")
        ttk.Label(frame, text="Start Longitude:").pack(pady=5)
        self.lon1 = tk.Entry(frame)
        self.lon1.pack()
        ttk.Label(frame, text="End Longitude:").pack(pady=5)
        self.lon2 = tk.Entry(frame)
        self.lon2.pack()
        ttk.Label(frame, text="Direction (East/West):").pack(pady=5)
        self.lon_dir = tk.Entry(frame)
        self.lon_dir.pack()
        ttk.Button(frame, text="Calculate", command=self.show_time_diff).pack(pady=10)
        return frame

    def create_conversion_panel(self, mode, units):
        frame = tk.Frame(self.panel_frame, bg="#1e1e1e")
        self.conv_input = tk.Entry(frame)
        self.conv_input.pack(pady=10)
        self.conv_from = ttk.Combobox(frame, values=units)
        self.conv_from.set(units[0])
        self.conv_from.pack()
        self.conv_to = ttk.Combobox(frame, values=units)
        self.conv_to.set(units[1])
        self.conv_to.pack()
        ttk.Button(frame, text="Convert", command=lambda: self.convert_units(mode)).pack(pady=10)
        return frame

    def create_button_grid(self, rows, command):
        frame = tk.Frame(self.panel_frame, bg="#1e1e1e")
        for r, row in enumerate(rows):
            for c, label in enumerate(row):
                b = tk.Button(frame, text=label, font=("Segoe UI", 16), width=4, height=2, bg="#333333", fg="white",
                             activebackground="#555555", command=lambda l=label: command(l))
                b.grid(row=r, column=c, padx=3, pady=3)
        return frame

    def handle_standard_click(self, label):
        current = self.display.cget("text")
        if label == "C":
            self.display.config(text="0")
        elif label == "=":
            try:
                expression = current.replace("×", "*").replace("÷", "/")
                result = eval(expression)
                self.display.config(text=str(round(result, 5)))
            except:
                self.display.config(text="Error")
        else:
            self.display.config(text=current + label if current != "0" else label)

    def handle_scientific_click(self, label):
        try:
            current = self.display.cget("text")
            if label in ["sin", "cos", "tan", "log", "exp", "√"]:
                value = float(current)
                if label == "√": result = math.sqrt(value)
                elif label == "log": result = math.log10(value)
                elif label == "exp": result = math.exp(value)
                else: result = getattr(math, label)(math.radians(value))
                self.display.config(text=str(round(result, 5)))
            elif label == "π":
                self.display.config(text=str(math.pi))
            elif label == "^":
                self.display.config(text=current + "**")
            else:
                self.handle_standard_click(label)
        except:
            self.display.config(text="Error")

    def show_area(self):
        try:
            l = float(self.len1.get())
            w = float(self.len2.get())
            area = self.calc.area(l, w)
            self.display.config(text=str(area))
        except: self.display.config(text="Error")

    def show_hypot(self):
        try:
            l = float(self.len1.get())
            w = float(self.len2.get())
            result = math.hypot(l, w)
            self.display.config(text=str(round(result, 3)))
        except: self.display.config(text="Error")

    def show_profit(self):
        try:
            p = float(self.profit1.get())
            bp = float(self.profit2.get())
            result = self.calc.percent_profit(p, bp)
            self.display.config(text=str(round(result, 2)) + "%")
        except: self.display.config(text="Error")

    def show_loss(self):
        try:
            l = float(self.profit1.get())
            bp = float(self.profit2.get())
            result = self.calc.percent_loss(l, bp)
            self.display.config(text=str(round(result, 2)) + "%")
        except: self.display.config(text="Error")

    def show_time_diff(self):
        try:
            a = float(self.lon1.get())
            b = float(self.lon2.get())
            d = self.lon_dir.get().strip()
            result = self.calc.time_by_longitude(a, b, d)
            self.display.config(text=f"{result} hrs")
        except: self.display.config(text="Error")

    def convert_units(self, mode):
        try:
            val = float(self.conv_input.get())
            u_from = self.conv_from.get()
            u_to = self.conv_to.get()

            factors = {
                "Length": {"m": 1, "km": 1000, "mi": 1609.34},
                "Weight": {"g": 1, "kg": 1000, "lb": 453.592},
                "Speed": {"m/s": 1, "km/h": 0.27778, "mph": 0.44704}
            }
            base = val * factors[mode][u_from]
            converted = base / factors[mode][u_to]
            self.display.config(text=str(round(converted, 4)))
        except: self.display.config(text="Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
