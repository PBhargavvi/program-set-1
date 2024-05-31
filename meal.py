time = input("Enter the time in 24-hour format (HH:MM): ").strip()
hours, minutes = map(int, time.split(":"))

hours_float = hours + minutes / 60.0

if 7.0 <= hours_float <= 8.0:
    print("It's breakfast time.")
elif 12.0 <= hours_float <= 13.0:
    print("It's lunch time.")
elif 18.0 <= hours_float <= 19.0:
    print("It's dinner time.")