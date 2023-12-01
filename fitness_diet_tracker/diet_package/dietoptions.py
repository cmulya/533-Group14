#from planoptions import PlanOptions

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

def main():
    input("Select one of the following Diet Options (Vegan/Vegetarian/Meat): ")
    pass

main()
