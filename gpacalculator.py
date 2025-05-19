def calculate_gpa(total_points, total_units):
    if total_units == 0:
        return 0
    gpa = total_points / total_units
    return round(gpa, 2)

def main():
    total_points = 62
    total_units = 14

    gpa = calculate_gpa(total_points, total_units)
    print("Total Grade Points:", total_points)
    print("Total Credit Units:", total_units)
    print("GPA:", gpa)

# Run the program
if __name__ == "__main__":
    main()
