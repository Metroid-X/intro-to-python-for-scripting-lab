# Problem 0: Example
#
# This is a practice problem to help you understand how to write code in a 
# provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting
# message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()


# Problem 1: Vowel or consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and 
#   determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user in the above
#   messages.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels. You may need to look up
#   how to use this online.
# - Ensure your code provides feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    char = input("input a SINGLE character\n")
    vowels = ["a","e","i","o","u"]
    consonants = [
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    
    if char.lower() in vowels:
        print(f"the character {char} is a vowel.")
    elif char.lower() in consonants:
        print(f"the character {char} is a consonant.")
    elif char.lower() in numbers:
        print(f"the character {char} is a number.")
    else:
        print(f"the character {char} is a special character.")
        
     

# Call the function
#check_letter()


# Problem 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a
# user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative 
#   numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting
#   age.
# - Print a message indicating whether the user is eligible to vote based on the
#   entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure that you handle any 
#   conversion errors gracefully. You may need to look up how to do this online.
# - Use a conditional statement to check if the age meets the minimum voting age
#   requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    voting_age = 18
    
    while True:
        tested_age = input("Please enter your age: ")
        try:
            if int(tested_age) >= voting_age:
                print("You are elligible to vote.")
                break
            elif int(tested_age) > 0:
                print("You are inelligible to vote.")
                break
            else:
                print("That is not a valid age.")
        except ValueError:
            print("That is not a valid age.")

# Call the function
#check_voting_eligibility()


# Problem 3: Calculate dog years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's
# age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the
#   dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    while True:
        try:
            input_age = float(input("Input a dog's age: "))
            if input_age > 2:
                dog_years = 7*(input_age-2)+20
                break
            elif input_age > 0:
                dog_years = 10*input_age
                break
            else:
                print("That is not a valid age.")
        except ValueError:
            print("That is not a valid age.")
    print(f"The dog's age in dog years is {dog_years}.")

# Call the function
#calculate_dog_years()


# Problem 4: Weather advice
#
# Write a Python script named `weather_advice` that provides clothing advice
# based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle
#   multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    step = 0
    while True:
        if step == 0:
            is_cold = input("Is it cold? (Y/n)\n")
            if (is_cold.lower() == "yes") | (is_cold.lower() == "y"):
                Is_Cold = True
                step+=1
            elif (is_cold.lower() == "no") | (is_cold.lower() == "n"):
                Is_Cold = False
                step+=1
            else:
                print("please only answer with yes/y or no/n.")
        elif step == 1:
            is_rain = input("Is it raining? (Y/n)\n")
            if (is_rain.lower() == "yes") | (is_rain.lower() == "y"):
                Is_Rain = True
                step+=1
            elif (is_rain.lower() == "no") | (is_rain.lower() == "n"):
                Is_Rain = False
                step+=1
            else:
                print("please only answer with yes/y or no/n.")
        elif step == 2:
            if Is_Cold and Is_Rain:
                print("Wear a waterproof coat.")
            elif Is_Cold and not Is_Rain:
                print("Wear a warm coat.")
            elif not Is_Cold and Is_Rain:
                print("Carry an umbrella.")
            elif not Is_Cold and not Is_Rain:
                print("Wear light clothing.")
            break
        
                
                

# Call the function
#weather_advice()


# Problem 5: What's the season?
#
# Write a Python function named `determine_season` that figures out the season
# based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three
#   characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month:
#   "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in
#   <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure you validate the user's input and handle unexpected inputs
#   gracefully.

def determine_season():
    # Your control flow logic goes here
    step = 0
    months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
    
    max_30 = ["apr","jun","sep","nov",]
    
    winter_m = ["Jan","Feb"]
    winter_d = 21
    
    spring_m = ["Apr","May"]
    spring_d = 20
    
    summer_m = ["Jul","Aug"]
    summer_d = 21
    
    autumn_m = ["Oct","Nov"]
    autumn_d = 22
    
    err_msg = "Invalid input."
    
    while True:
        match step:
            case 0:
                month_input = input("Enter the month of the year (Jan - Dec): ").lower()
                if month_input in months:
                    Month = month_input.capitalize()
                    step+=1
                else:
                    print(err_msg)
            case 1:
                day_input = input("Enter the day of the month: ").lower().replace(" ","")
                try:
                    if (int(day_input) < 1) or (Month.lower() in max_30 and int(day_input) > 30) or (Month.lower() == "feb" and int(day_input) > 29) or int(day_input) > 31:
                        print(err_msg)
                    else:
                        if len(day_input) < 2:
                            Day = f"{day_input}"
                        else:
                            Day = day_input
                        step+=1
                except ValueError:
                    print(err_msg)
            case 2:
                if Month in winter_m or (Month == "Dec" and int(Day) >= winter_d) or (Month == "Mar" and int(Day) < spring_d):
                    Season = "Winter"
                elif Month in spring_m or (Month == "Mar" and int(Day) >= spring_d) or (Month == "Jun" and int(Day) < summer_d):
                    Season = "Spring"
                elif Month in summer_m or (Month == "Jun" and int(Day) >= summer_d) or (Month == "Sep" and int(Day) < autumn_d):
                    Season = "Summer"
                elif Month in autumn_m or (Month == "Sep" and int(Day) >= autumn_d) or (Month == "Dec" and int(Day) < winter_d):
                    Season = "Fall"
                step+=1
            case 3:
                print(f"{Month} {Day} is in {Season}.")
                break
                
                
# Call the function
determine_season()
