#generate workout exercises
#superclass

class warmUp:
    def __init__(self, plan):
        self.plan = plan 
    def athlete_warmup(self):
        return f'Seated hamstring stretch (2 repetitions)\nLight jogging (5 mins)\nAcross Body arm strech (2 repetitions)\nPull up bar hang(1 minute)'
    def strength_warmup(self):
        return f'Overhead Tricep Stretch (2 repetitions)\nStanding hamstring strech (2 repetitions)\nSupine Twist Back Stretch (2 repetitions)\nlight weight squats/deadlifts/benchpress'
    def body_weight_warmup(self):
        return f'Cobra Strech (2 repetitions)\nBent arm wall stretch\nStanding quadriceps strecthes (2 repetitions)\nincline push ups\nbodyweight squats'
    def youtube_links(self):
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
        if self.plan == "athlete":
            return f'{self.athlete_warmup()}\n\nHere are the warmup guides: \n{self.youtube_links()}'
        if self.plan == "strength":
            return f'{self.strength_warmup()}\n\nHere are the warmup guides: \n{self.youtube_links()}'
        if self.plan == "body weight":
            return f'{self.body_weight_warmup()}\n\nHere are the warmup guides: \n{self.youtube_links()}'