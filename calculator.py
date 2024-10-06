class Calculator:
    def add(self, x, y):
        if not isinstance(x, int) and not isinstance(x, float):
            if not x.replace('.', '', 1).isnumeric():
                raise TypeError
            x = float(x)
        if not isinstance(y, int) and not isinstance(y, float):
            if not y.replace('.', '', 1).isnumeric():
                raise TypeError
            y = float(y)                 
        return x + y
    def subtract(self, x, y):
        # Check if x is a valid int or float, or if it's a valid string representation of a number (including negatives)
        if not isinstance(x, (int, float)):
            # Check if x is a valid numeric string
            if x[0] == '-' and x[1:].replace('.', '', 1).isdigit():  # Check for negative numbers
                x = float(x)
            elif x.replace('.', '', 1).isdigit():  # Check for positive numbers
                x = float(x)
            else:
                raise TypeError("Invalid type for x")
        
        # Check if y is a valid int or float, or if it's a valid string representation of a number (including negatives)
        if not isinstance(y, (int, float)):
            # Check if y is a valid numeric string
            if y[0] == '-' and y[1:].replace('.', '', 1).isdigit():  # Check for negati0ve numbers
                y = float(y)
            elif y.replace('.', '', 1).isdigit():  # Check for positive numbers
                y = float(y)
            else:
                raise TypeError("Invalid type for y")
        
        return x - y
    def multiply(self, x, y):
        if not isinstance(x, (int, float)):
            if x[0] == '-' and x[1:].replace('.', '', 1).isdigit():
                x = float(x)
            elif x.replace('.', '', 1).isdigit():
                x = float(x)
            else:
                raise TypeError("Invalid type for x")

        if not isinstance(y, (int, float)):
            if y[0] == '-' and y[1:].replace('.', '', 1).isdigit():
                y = float(y)
            elif y.replace('.', '', 1).isdigit():
                y = float(y)
            else:
                raise TypeError("Invalid type for y")

        return x * y

    def divide(self, x, y):
        if not isinstance(x, (int, float)):
            if x[0] == '-' and x[1:].replace('.', '', 1).isdigit():
                x = float(x)
            elif x.replace('.', '', 1).isdigit():
                x = float(x)
            else:
                raise TypeError("Invalid type for x")

        if not isinstance(y, (int, float)):
            if y[0] == '-' and y[1:].replace('.', '', 1).isdigit():
                y = float(y)
            elif y.replace('.', '', 1).isdigit():
                y = float(y)
            else:
                raise TypeError("Invalid type for y")
        
        if y == 0:
            raise ValueError("Cannot divide by zero")

        return x / y