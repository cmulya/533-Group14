# FitFuel - Fitness Diet Tracker Package
The fitness_diet_tracker package aims to provide a comprehensive solution for users looking to manage both their workout routines and dietary plans effectively. The subpackages and modules within the package offer specialized functionality for creating tailored workout plans and generating meal options based on individual preferences and goals.

## Project Structure
```
fitness_diet_tracker/
├── __init__.py
├── workout_plan/
│   ├── __init__.py
│   ├── warmup.py
│   └── workout.py
└── diet_package/
    ├── __init__.py
    ├── planoptions.py
    └── dietoptions.py
```

## Subpackage 1: workout_plan
### Module 1: warmup.py
Class 1: warmUp (superclass)
- athlete_warmup: Performs a warm-up routine for athletes, including jogging, jumping jacks, and stretches. Provides a list of warm-up exercises and YouTube video instruction links.
- strength_warmup: Executes a warm-up routine for strength training, involving light weight curls, shoulder press, body weight squats, and stretches. Provides a list of warm-up exercises and YouTube video instruction links.
- body_weight_warmup: Conducts a warm-up routine for bodyweight exercises, featuring incline push-ups, bodyweight squats, and stretches. Provides a list of warm-up exercises and YouTube video instruction links.

### Module 2: workout.py
Class 2: WorkOut (inherits from warmUp)
- generate_intensity_plan: Generates a workout plan based on intensity, providing the plan and YouTube video instruction links based on the workout duration.
- generate_powerlifting_plan: Generates a powerlifting workout plan, providing the plan and YouTube video instruction links based on the workout duration.
- generate_calisthenics_plan: Generates a calisthenics workout plan, providing the plan and YouTube video instruction links based on the workout duration.

## Subpackage 2: diet_package
### Module 1: planoptions.py
Class 1: PlanOptions (superclass)
- calculate_bmi: Calculates BMI for males and females.
- calculate_tdee: Calculates total daily energy expenditure by multiplying the calculated BMI with the activity level multiplier.
- calculate_target_cal: Adjusts the necessary calories based on the user's chosen weight goal (gain/loss).

### Module 2: dietoptions.py
Class 2: DietOptions (inherits from PlanOptions)
- generate_vegan_meal: Generates a meal plan based on a vegan diet, including meal name, calorie per serving, YouTube link, and serving calculations to meet the target calories.
  - Protein Option 1 (tofu): Vegan Pad Thai
  - Protein Option 2 (soy curls): Vegan Chik'n Stir Fry
  - Protein Option 3 (tempeh): Slow Cooker Tempeh Chilli
- generate_vegetarian_meal: Generates a meal plan based on a vegetarian diet, providing meal details and serving calculations similar to the vegan meal options.
  - Protein Option 1 (cranberry beans): Italian Style Oven-Baked Beans
  - Protein Option 2 (black beans): Vegetarian Chilli
  - Protein Option 3 (chickpea): Mediterranean Chickpea Salad
- generate_meat_meal: Generates a meal plan based on a meat diet, offering meal details and serving calculations similar to the vegan and vegetarian meal options.
  - Protein Option 1 (beef): Black Pepper Beef with Rice
  - Protein Option 2 (chicken): Chicken Shawarma with Crispy Fries
  - Protein Option 3 (fish): Honey Garlic Salmon Rice Bowl

