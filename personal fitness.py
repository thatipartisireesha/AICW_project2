steps = 0
workout_minutes = 0
calories = 0.0

def add_steps():
    global steps, calories
    s = int(input("Enter steps walked today: "))
    steps += s
    calories += s * 0.04
    print("Steps added successfully!")

def add_workout():
    global workout_minutes, calories
    m = int(input("Enter workout time in minutes: "))
    workout_minutes += m
    calories += m * 5
    print("Workout added successfully!")

def show_summary():
    print("\n------ DAILY FITNESS SUMMARY ------")
    print("Total Steps Walked      :", steps)
    print("Workout Time (minutes) :", workout_minutes)
    print("Calories Burned        :", round(calories, 2))
    print("-----------------------------------\n")

# Menu-driven program
while True:
    print("=== PERSONAL FITNESS TRACKER ===")
    print("1. Add Steps")
    print("2. Add Workout Time")
    print("3. View Daily Summary")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_steps()
    elif choice == 2:
        add_workout()
    elif choice == 3:
        show_summary()
    elif choice == 4:
        print("Stay fit! 💪 Exiting program.")
        break
    else:
        print("Invalid choice! Try again.")
