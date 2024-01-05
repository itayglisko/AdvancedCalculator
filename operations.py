def add(num1: float, num2: float) -> float:
    try:
        return float(num1 + num2)
    except (ValueError, TypeError) as err:
        print("this function needs to get an integer or a float type")

