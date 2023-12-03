from diet_package.planoptions import PlanOptions

class DietOptions(PlanOptions):
    """
    DietOptions class extends the PlanOptions class and provides methods for generating meal plans
    based on dietary preferences (vegan, vegetarian, or meat) and protein options.

    Attributes:
    - height (float): The user's height.
    - weight (float): The user's weight.
    - age (int): The user's age.
    - gender (str): The user's gender (male/female).
    - activity_level (str): The user's activity level (low/moderate/high).
    - weight_goal (str): The user's weight goal (gain/loss).

    Methods:
    - __init__: Initializes the DietOptions object by calling the constructor of the superclass (PlanOptions).
    - generate_vegan_meal: Generates a vegan meal plan based on the specified protein option.
    - generate_vegetarian_meal: Generates a vegetarian meal plan based on the specified protein option.
    - generate_meat_meal: Generates a meat-based meal plan based on the specified protein option.
    """
    def __init__(self, height, weight, age, gender, activity_level, weight_goal):
        """
        Initializes a DietOptions object with user inputs and inherits attributes from the PlanOptions class.

        Parameters:
        - height (float): The user's height in centimeters.
        - weight (float): The user's weight in kilograms.
        - age (int): The user's age in years.
        - gender (str): The user's gender ('male' or 'female').
        - activity_level (str): The user's activity level ('low', 'moderate', or 'high').
        - weight_goal (str): The user's weight goal ('gain' or 'loss').
        """
        super().__init__(height, weight, age, gender, activity_level, weight_goal)

    def generate_vegan_meal(self, protein_option):
        """
        Generates a vegan meal plan based on the specified protein option.

        Parameters:
        - protein_option (str): The chosen protein option for the vegan meal plan.

        Prints the meal plan details, including the meal name, calories per serving, YouTube link,
        and the recommended servings per day to meet the target daily calorie intake.
        """
        recipes = {
            "tofu": {"name": "Vegan Pad Thai", "calories_per_serving": 572, "youtube_link": "https://www.youtube.com/watch?v=96oziIw9Mjw"},
            "soy_curls": {"name": "Vegan Chik'n Stir Fry", "calories_per_serving": 611, "youtube_link": "https://www.youtube.com/watch?v=AQxG258gOx8"},
            "tempeh": {"name": "Slow Cooker Tempeh Chili", "calories_per_serving": 553, "youtube_link": "https://www.youtube.com/watch?v=Iw8L4K6pM6U"}
        }

        if protein_option not in recipes:
            print("Invalid protein option for a vegan diet.")
            return

        recipe = recipes[protein_option]
        target_calories = self.calculate_target_cal()
        servings_per_day = target_calories / recipe["calories_per_serving"]

        print(f"Vegan Meal Plan with {protein_option.capitalize()}:")
        print(f"Meal: {recipe['name']}")
        print(f"Calorie per Serving: {recipe['calories_per_serving']} cal")
        print(f"Youtube Link: {recipe['youtube_link']}")
        print(f"Servings per Day: {servings_per_day:.2f}\n") 
            
    def generate_vegetarian_meal(self, protein_option):
        """
        Generates a vegetarian meal plan based on the specified protein option.

        Parameters:
        - protein_option (str): The chosen protein option for the vegetarian meal plan.

        Prints the meal plan details, including the meal name, calories per serving, YouTube link,
        and the recommended servings per day to meet the target daily calorie intake.
        """
        recipes = {
            "cranberry_beans": {"name": "Italian Style Oven-Baked Beans", "calories_per_serving": 610, "youtube_link": "https://www.youtube.com/watch?v=NQK3n9XINeU"},
            "black_beans": {"name": "Vegetarian Chili", "calories_per_serving": 409, "youtube_link": "https://www.youtube.com/watch?v=oy1u49dLgaE"},
            "chickpea": {"name": "Mediterranean Chickpea Salad", "calories_per_serving": 169, "youtube_link": "https://www.youtube.com/watch?v=jWCrEAvSZ8g"}
        }

        if protein_option not in recipes:
            print("Invalid protein option for a vegetarian diet.")
            return

        recipe = recipes[protein_option]
        target_calories = self.calculate_target_cal()
        servings_per_day = target_calories / recipe["calories_per_serving"]

        print(f"Vegetarian Meal Plan with {protein_option.capitalize()}:")
        print(f"Meal: {recipe['name']}")
        print(f"Calorie per Serving: {recipe['calories_per_serving']} cal")
        print(f"Youtube Link: {recipe['youtube_link']}")
        print(f"Servings per Day: {servings_per_day:.2f}\n")

    def generate_meat_meal(self, protein_option):
        """
        Generates a meat-based meal plan based on the specified protein option.

        Parameters:
        - protein_option (str): The chosen protein option for the meat-based meal plan.

        Prints the meal plan details, including the meal name, calories per serving, YouTube link,
        and the recommended servings per day to meet the target daily calorie intake.
        """
        recipes = {
            "beef": {"name": "Black Pepper Beef with Rice", "calories_per_serving": 556, "youtube_link": "https://www.youtube.com/watch?v=2hIc7lWytRs"},
            "chicken": {"name": "Chicken Shawarma with Crispy Fries", "calories_per_serving": 450, "youtube_link": "https://www.youtube.com/shorts/CTMCNrI-QKg"},
            "fish": {"name": "Honey Garlic Salmon Rice Bowl", "calories_per_serving": 636, "youtube_link": "https://www.youtube.com/watch?v=-3h4O4on_-4"}
        }
        
        if protein_option not in recipes:
            print("Invalid protein option for a meat diet.")
            return

        recipe = recipes[protein_option]
        target_calories = self.calculate_target_cal()
        servings_per_day = target_calories / recipe["calories_per_serving"]

        print(f"Meat Meal Plan with {protein_option.capitalize()}:")
        print(f"Meal: {recipe['name']}")
        print(f"Calorie per Serving: {recipe['calories_per_serving']} cal")
        print(f"Youtube Link: {recipe['youtube_link']}")
        print(f"Servings per Day: {servings_per_day:.2f}\n")

# main function
def main():
    """
    Main function for the Diet Planner program.

    Interactively collects user information such as height, weight, age, gender, activity level, and weight goal.
    Calculates BMR, TDEE, and target calories based on the user's inputs. Allows the user to choose a dietary
    preference (vegan, vegetarian, or meat) and a protein option, generating a meal plan accordingly.

    Exception handling is implemented to ensure input validity, and the program continues to prompt the user
    until correct inputs are provided.
    """
    while True:
        try:
            # Input for height with constraint
            while True:
                height = float(input("What is your height (in cm)? "))
                if height > 0:
                    break
                else:
                    print("Height must be greater than 0. Please enter a valid height.")

            # Input for weight with constraint
            while True:
                weight = float(input("What is your weight (in kg)? "))
                if weight > 0:
                    break
                else:
                    print("Weight must be greater than 0. Please enter a valid weight.")

            # Input for age with constraint
            while True:
                age = int(input("What is your age? "))
                if age > 0:
                    break
                else:
                    print("Age must be greater than 0. Please enter a valid age.")

            while True:
                gender = input("What is your gender? (male/female): ").lower()
                if gender in ["male", "female"]:
                    break
                else:
                    print("Gender must be male or female.")
            
            while True:
                print("If you use our workout program, choose 'high' as your activity level.")
                activity_level = input("What is your activity level? (low/moderate/high): ").lower()
                if activity_level in ["low", "moderate", "high"]:
                    break
                else:
                    print("Activity level must be low / moderate / high.")
            
            while True:
                weight_goal = input("What is your weight goal? (gain/loss): ").lower()
                if weight_goal in ["gain", "loss"]:
                    break
                else:
                    print("Weight goal must be gain or loss.")

            diet_plan = DietOptions(height, weight, age, gender, activity_level, weight_goal)

            # implementation
            diet_plan.calculate_bmr()
            diet_plan.calculate_tdee()
            diet_plan.calculate_target_cal()
            
            print(diet_plan)

            # Choose dietary preference
            while True:
                diet_option = input("Select one of the following Diet Options (vegan/vegetarian/meat): ").lower()

                if diet_option in ['vegan', 'vegetarian', 'meat']:
                    break  # Exit the loop if a valid diet option is provided
                else:
                    print("Invalid diet option. Please choose vegan, vegetarian, or meat.")

            # Choose protein option
            while True:
                if diet_option == 'vegan':
                    protein_option = input("Select a protein option for a vegan diet (tofu/soy_curls/tempeh): ").lower()
                elif diet_option == 'vegetarian':
                    protein_option = input("Select a protein option for a vegetarian diet (cranberry_beans/black_beans/chickpea): ").lower()
                elif diet_option == 'meat':
                    protein_option = input("Select a protein option for a meat diet (beef/chicken/fish): ").lower()

                if protein_option in ['tofu', 'soy_curls', 'tempeh', 'cranberry_beans', 'black_beans', 'chickpea', 'beef', 'chicken', 'fish']:
                    break  # Exit the loop if a valid protein option is provided
                else:
                    print("Invalid protein option. Please choose a valid option.")

            if diet_option == 'vegan':
                diet_plan.generate_vegan_meal(protein_option)
            elif diet_option == 'vegetarian':
                diet_plan.generate_vegetarian_meal(protein_option)
            elif diet_option == 'meat':
                diet_plan.generate_meat_meal(protein_option)

            break  # Exit the main loop if everything is successful

        except Exception as ve:
            print(f"Error: {ve}. Please enter a valid number for height, weight, and age.")



main()