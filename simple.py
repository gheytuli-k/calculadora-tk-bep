def calculate_area(radius):
    area = 3.14 * radius * radius
    return area

def main():
    radius = 5
    area = calculate_area(radius)
    assert area == 75.0, f"Assertion failed: {area} != 75.0" 
    print(f"Area of circle with radius {radius} is {area}")

if __name__ == "__main__":
    main()