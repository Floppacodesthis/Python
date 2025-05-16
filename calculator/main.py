import math

class Calculator:
    def time_by_longitude(self, start, end, direction):
        try:
            if direction.lower() == 'east':
                answer = end - start
            elif direction.lower() == 'west':
                answer = start - end
            else:
                return 'Invalid direction. Input East or West'
            time_difference = answer / 15
            return round(time_difference, 2)
        except ValueError:
            return "ValueError"

    def percent_profit(self, profit, bp):
        try:
            result = (profit / bp) * 100
            return round(result, 2)
        except ZeroDivisionError:
            return "ZeroDivisionError"

    def percent_loss(self, loss, bp):
        try:
            result = (loss / bp) * 100
            return round(result, 2)
        except ZeroDivisionError:
            return "ZeroDivisionError"

    def square(self, x):
        return x * x

    def square_root(self, x):
        try:
            if x < 0:
                return "ValueError"
            return math.sqrt(x)
        except ValueError:
            return "ValueError"

    def circumference(self, diameter):
        return round(math.pi * diameter, 5)

    def area(self, length, width):
        return round(length * width, 5)

    def rat_area(self, base, height):
        return round(0.5 * base * height, 5)

    def get_hypotenuse(self, base, height):
        return round(math.hypot(base, height), 5)

    def add(self, a, b):
        return round(a + b, 5)

    def subtract(self, a, b):
        return round(a - b, 5)

    def multiply(self, a, b):
        return round(a * b, 5)

    def divide(self, a, b):
        try:
            return round(a / b, 5)
        except ZeroDivisionError:
            return "ZeroDivisionError"

    def scientific_operation(self, operation, value):
        try:
            if operation == 'sin':
                return round(math.sin(math.radians(value)), 5)
            elif operation == 'cos':
                return round(math.cos(math.radians(value)), 5)
            elif operation == 'tan':
                return round(math.tan(math.radians(value)), 5)
            elif operation == 'log':
                return round(math.log10(value), 5)
            elif operation == 'ln':
                return round(math.log(value), 5)
            elif operation == 'exp':
                return round(math.exp(value), 5)
            elif operation == 'sqrt':
                return round(math.sqrt(value), 5)
            elif operation == 'factorial':
                return math.factorial(int(value))
            elif operation == 'pi':
                return round(math.pi, 5)
            elif operation == 'e':
                return round(math.e, 5)
            else:
                return "Invalid operation"
        except (ValueError, OverflowError):
            return "MathError"

    def convert_units(self, mode, value, from_unit, to_unit):
        try:
            value = float(value)
            units = {
                'Length': {'m': 1, 'km': 1000, 'mi': 1609.34},
                'Weight': {'g': 1, 'kg': 1000, 'lb': 453.592},
                'Speed': {'m/s': 1, 'km/h': 0.27778, 'mph': 0.44704}
            }
            if mode not in units:
                return "Invalid mode"
            if from_unit not in units[mode] or to_unit not in units[mode]:
                return "Invalid unit"
            base = value * units[mode][from_unit]
            converted = base / units[mode][to_unit]
            return round(converted, 5)
        except (ValueError, KeyError):
            return "ConversionError"
