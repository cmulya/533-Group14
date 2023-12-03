#superclass

class warmUp:
    """
    The WarmUp class provides warm-up routines and YouTube links based on different workout plans.

    Attributes:
    - plan (str): The workout plan, which can be "athlete", "strength", or "body weight".

    Methods:
    - athlete_warmup(): Generate a warm-up routine for athletes.
    - strength_warmup(): Generate a warm-up routine for strength training.
    - body_weight_warmup(): Generate a warm-up routine for bodyweight exercises.
    - youtube_links(): Generate YouTube links based on the workout plan.
    - __str__(): Return a formatted string with the warm-up routine and YouTube links.
    """
    def __init__(self, plan):
        """
        Initialize the warmUp class with a specific workout plan.

        Parameters:
        - plan (str): The workout plan, which can be "athlete", "strength", or "body weight".
        """
        self.plan = plan 
    
    def athlete_warmup(self):
        """
        Generate a warm-up routine for athletes.

        Returns:
        - str: A string describing the athlete warm-up routine.
        """
        return f'Seated hamstring stretch (2 repetitions)\nLight jogging (5 mins)\nAcross Body arm stretch (2 repetitions)\nPull-up bar hang (1 minute)'
    
    def strength_warmup(self):
        """
        Generate a warm-up routine for strength training.

        Returns:
        - str: A string describing the strength training warm-up routine.
        """
        return f'Overhead Tricep Stretch (2 repetitions)\nStanding hamstring stretch (2 repetitions)\nSupine Twist Back Stretch (2 repetitions)\nLightweight squats/deadlifts/bench press/curls'
    
    def body_weight_warmup(self):
        """
        Generate a warm-up routine for bodyweight exercises.

        Returns:
        - str: A string describing the bodyweight exercises warm-up routine.
        """
        return f'Cobra Stretch (2 repetitions)\nBent arm wall stretch\nStanding quadriceps stretches (2 repetitions)\nIncline push-ups\nBodyweight squats'
    
    def youtube_links_warmup(self):
        """
        Generate YouTube links based on the workout plan.

        Returns:
        - str: YouTube links for warm-up exercises corresponding to the workout plan.
        """
        if self.plan == "athlete":
            seated_hamstring_stretch = "https://www.youtube.com/watch?v=HFPbNaMzW3M"
            across_body_arm_stretch = "https://www.youtube.com/watch?v=-1K0m5ywRcY"
            return f'{seated_hamstring_stretch}\n{across_body_arm_stretch}'
        if self.plan == "strength":
            overhead_tricep_stretch = "https://www.youtube.com/watch?v=Uvk1Y8O1_yM"
            standing_hamstring_stretch = "https://www.youtube.com/watch?v=LVY692zJK0A"
            supine_twist_back_stretch = "https://www.youtube.com/watch?v=mNdJti7ZwKI"
            return f'{overhead_tricep_stretch}\n{standing_hamstring_stretch}\n{supine_twist_back_stretch}'
        if self.plan == "body weight":
            cobra_stretch = "https://www.youtube.com/watch?v=JDcdhTuycOI"
            bent_arm_wall_stretch = "https://www.youtube.com/watch?v=3MuMu3Q4r68"
            standing_quadriceps_stretch = "https://www.youtube.com/watch?v=g4v_QK893eI"
            return f'{cobra_stretch}\n{bent_arm_wall_stretch}\n{standing_quadriceps_stretch}'
    
    def __str__(self):
        """
        Return a formatted string with the warm-up routine and YouTube links.

        Returns:
        - str: A formatted string with the warm-up routine and YouTube links.
        """
        if self.plan == "athlete":
            return f'{self.athlete_warmup()}\n\nHere are the warm-up guides: \n{self.youtube_links_warmup()}'
        if self.plan == "strength":
            return f'{self.strength_warmup()}\n\nHere are the warm-up guides: \n{self.youtube_links_warmup()}'
        if self.plan == "body weight":
            return f'{self.body_weight_warmup()}\n\nHere are the warm-up guides: \n{self.youtube_links_warmup()}'
