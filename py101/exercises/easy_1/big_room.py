# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet
measurement_type = input("Would you like to enter the dimensions in meters or feet? (m/f): ").strip().lower()

if measurement_type == 'm':
    print("Enter the length of the room in meters? ")
    length = float(input())

    print("Enter the width of the room in meters? ")
    width = float(input())

    square_meter = length * width

    square_feet = square_meter  * 10.7639

    print(f"The area of the room is {square_meter:.2f} "
      f"square meters ({square_feet:.2f} square feet).")
    
elif measurement_type == 'f':
     print("Enter the length of the room in feet? ")
     length = float(input())

     print("Enter the width of the room in feet? ")
     width = float(input())

     square_feet = length * width

     square_meter = square_feet  / 10.7639

     print(f"The area of the room is {square_feet:.2f} "
     f"square meters ({square_meter:.2f} square feet).")