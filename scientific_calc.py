import math

# Degree-based trig functions
def sin_deg(x):
    return math.sin(math.radians(x))

def cos_deg(x):
    return math.cos(math.radians(x))

def tan_deg(x):
    return math.tan(math.radians(x))

# Allowed functions & constants
allowed_names = {
    "sin": sin_deg,
    "cos": cos_deg,
    "tan": tan_deg,
    "sqrt": math.sqrt,
    "log": math.log10,
    "ln": math.log,
    "pi": math.pi,
    "e": math.e,
    "abs": abs,
    "round": round,
    "pow": pow
}

print("Welcome to Scientific Calculator")
print("Type expressions like: 2 + 3 * sin(30) - sqrt(16) + log(100)")

while True:
    expr = input("\nEnter expression (or 'exit' to quit): ").strip()
    if expr.lower() == "exit":
        print("Goodbye!")
        break
    try:
        result = eval(expr, {"__builtins__": None}, allowed_names)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)