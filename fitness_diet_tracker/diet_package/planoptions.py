#superclass
from diet_package.planoptions import PlanOptions

class PlanOptions:
    def __init__(self, height, weight, age, gender, activity_level, weight_goal):
        self.height = height
        self.weight = weight
        self.age = age
        self.gender = gender
        self.activity_level = activity_level
        self.weight_goal = weight_goal
        
    def calculate_bmr(self):
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
        #calculate target calorie intake per day based on weight goal
        #if 'gain', then the target calorie intake = self.tdee * 110%
        #if 'loss', then the target calorie intake = self.tdee * 90%
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
        result_str = ""
       
        if self.bmr is not None:
            result_str += f"BMR: {self.bmr:.2f}\n"

        if self.tdee is not None:
            result_str += f"TDEE: {self.tdee:.2f} calories per day\n"
            
        if self.target_cal is not None:
            result_str += f"Target calories: {self.target_cal:.2f} calories per day\n"

        return result_str