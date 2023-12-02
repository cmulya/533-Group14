# from planoptions import PlanOptions
from diet_package.planoptions import PlanOptions

class DietOptions(PlanOptions):
    def __init__(self, height, weight, age, gender, activity_level, weight_goal):
        super().__init__(height, weight, age, gender, activity_level, weight_goal)

    def generate_vegan_meal(self, protein_option):
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
    try:
        height = float(input("What is your height? "))
        weight = float(input("What is your weight? "))
        age = int(input("What is your age? "))
        gender = input("What is your gender? (male/female)").lower()
        activity_level = input("What is your activity level? (low/moderate/high)").lower()
        weight_goal = input("What is your weight goal? (gain/loss)").lower()

        diet_plan = DietOptions(height, weight, age, gender, activity_level, weight_goal)

        # implementation
        diet_plan.calculate_bmr()
        diet_plan.calculate_tdee()
        diet_plan.calculate_target_cal()
        
        print(diet_plan)

        # Choose dietary preference
        diet_option = input("Select one of the following Diet Options (vegan/vegetarian/meat): ").lower()

        if diet_option == 'vegan':
            protein_option = input("Select a protein option for a vegan diet (tofu/soy_curls/tempeh): ").lower()
            diet_plan.generate_vegan_meal(protein_option)
        elif diet_option == 'vegetarian':
            protein_option = input("Select a protein option for a vegetarian diet (cranberry_beans/black_beans/chickpea): ").lower()
            diet_plan.generate_vegetarian_meal(protein_option)
        elif diet_option == 'meat':
            protein_option = input("Select a protein option for a meat diet (beef/chicken/fish): ").lower()
            diet_plan.generate_meat_meal(protein_option)
        else:
            print("Invalid diet option. Please choose vegan, vegetarian, or meat.")


    except ValueError as ve:
        print(f"Error: {ve}. Please enter a valid number for height, weight, and age.")


# if __name__ == "__main__":
b = main()
