# superclass
class PlanOptions:
    """
    PlanOptions Class represents a plan for calculating Basal Metabolic Rate (BMR), Total Daily Energy Expenditure (TDEE),
    and target calorie intake per day based on user inputs for height, weight, age, gender, activity level, and weight goal.

    Attributes:
    - height (float): The user's height in centimeters.
    - weight (float): The user's weight in kilograms.
    - age (int): The user's age in years.
    - gender (str): The user's gender ('male' or 'female').
    - activity_level (str): The user's activity level ('low', 'moderate', or 'high').
    - weight_goal (str): The user's weight goal ('gain' or 'loss').

    Methods:
    - __init__: Initializes the PlanOptions object with user inputs.
    - calculate_bmr: Calculates the Basal Metabolic Rate based on the Harris-Benedict equation for men and women.
    - calculate_tdee: Calculates the Total Daily Energy Expenditure based on the BMR and activity level.
    - calculate_target_cal: Calculates the target calorie intake per day based on the weight goal.
    - __str__: Overrides the default string representation to display calculated results.

    Note: This class is designed to be inherited by specialized diet planning classes.
    """
    def __init__(self, height, weight, age, gender, activity_level, weight_goal):
        """
        Initializes a PlanOptions object with user inputs.

        Parameters:
        - height (float): The user's height in centimeters.
        - weight (float): The user's weight in kilograms.
        - age (int): The user's age in years.
        - gender (str): The user's gender ('male' or 'female').
        - activity_level (str): The user's activity level ('low', 'moderate', or 'high').
        - weight_goal (str): The user's weight goal ('gain' or 'loss').
        """
        self.height = height
        self.weight = weight
        self.age = age
        self.gender = gender
        self.activity_level = activity_level
        self.weight_goal = weight_goal
        
    def calculate_bmr(self):
        """
        Calculates the Basal Metabolic Rate (BMR) based on the Harris-Benedict equation.

        Returns:
        - bmr (float): The calculated BMR in calories per day.
        """
        if self.gender.lower() == 'female':
            # BMR for women
            self.bmr = 655.1 + (9.563 * self.weight) + (1.850 * self.height) - (4.676 * self.age)
        elif self.gender.lower() == 'male':
            # BMR for men
            self.bmr = 66.47 + (13.75 * self.weight) + (5.003 * self.height) - (6.755 * self.age)
        else:
            print("Invalid gender input. BMI calculation not possible.")
            return None

        return self.bmr
    
    def calculate_tdee(self):
        """
        Calculates the Total Daily Energy Expenditure (TDEE) based on the BMR and activity level.

        Returns:
        - tdee (float): The calculated TDEE in calories per day.
        """
        if self.bmr is not None:
            if self.activity_level.lower() == 'low':
                self.tdee = self.bmr * 1.2
            elif self.activity_level.lower() == 'moderate':
                self.tdee = self.bmr * 1.55
            elif self.activity_level.lower() == 'high':
                self.tdee = self.bmr * 1.9
            else:
                print("Invalid activity level input. TDEE calculation not possible.")
                return None

            return self.tdee
    
    def calculate_target_cal(self):
        """
        Calculates the target calorie intake per day based on the weight goal.

        Returns:
        - target_cal (float): The calculated target calorie intake in calories per day.
        """
        if self.tdee is not None:
            if self.weight_goal.lower() == 'gain':
                self.target_cal = self.tdee * 1.1
            elif self.weight_goal.lower() == 'loss':
                self.target_cal = self.tdee * 0.9
            else:
                print("Invalid weight goal input. Target calories calculation not possible.")
                return None
            
            return self.target_cal
           
    
    def __str__(self):
        """
        Overrides the default string representation to display calculated results.

        Returns:
        - result_str (str): A formatted string displaying BMR, TDEE, and target calories.
        """
        result_str = ""
        if self.bmr is not None:
            result_str += f"BMR: {self.bmr:.2f}\n"
        if self.tdee is not None:
            result_str += f"TDEE: {self.tdee:.2f} calories per day\n"  
        if self.target_cal is not None:
            result_str += f"Target calories: {self.target_cal:.2f} calories per day\n"
        return result_str