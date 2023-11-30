#generate workout exercises

class WorkOut:
    def __init__(self, time, plan):
        self.time = time
        self.plan = plan 
    def generate_intensity_plan(self):
        if self.time > 0 and self.time <= 30:
            return f'3 sets of push press until failure\n3 sets of half squat jumps until failure\n3 sets of pull ups until failure\nAtleast 1 minute of rest between each set is recommended'
        if self.time > 30 and self.time <= 45:
            return f'4 sets of push press until failure\n4 sets of half squat jumps until failure\n4 sets of pull ups until failure\nAtleast 1.5 minute of rest between each set is recommended'
        if self.time > 45 and self.time <=60:
            return f'5 sets of push press until failure\n5 sets of half squat jumps until failure\n5 sets of pull ups until failure\nAtleast 1.5 minute of rest between each set is recommended'
    def generate_powerlifting_plan(self):
        if self.time > 0 and self.time <= 30:
            return f'2 sets of bench press until failure\n2 sets of barbell squats until failure\n2 sets of deadlifts until failure\nAtleast 2 minute of rest between each set is recommended'
        if self.time > 30 and self.time <= 45:
            return f'3 sets of bench press until failure\n3 sets of barbell squats until failure\n3 sets of deadlifts until failure\nAtleast 2 minute of rest between each set is recommended'
        if self.time > 45 and self.time <=60:
            return f'4 sets of bench press until failure\n4 sets of barbell squats until failure\n4 sets of deadlifts until failure\nAtleast 2.5 minute of rest between each set is recommended'
    def generate_calisthenics_plan(self):
        if self.time > 0 and self.time <= 30:
            return f'3 sets of push ups until failure\n3 sets of pistol squats until failure\n3 sets of pull ups until failure\nAtleast 1 minute of rest between each set is recommended'
        if self.time > 30 and self.time <= 45:
            return f'4 sets of push ups until failure\n4 sets of pistol squats until failure\n4 sets of pull ups until failure\nAtleast 1.5 minute of rest between each set is recommended'
        if self.time > 45 and self.time <=60:
            return f'5 sets of push ups until failure\n5 sets of pistol squats until failure\n5 sets of pull ups until failure\nAtleast 1.5 minute of rest between each set is recommended'
    def youtube_links(self):
        if self.plan == "athlete":
            push_press = "https://www.youtube.com/watch?v=iaBVSJm78ko"
            squat_jumps = "https://www.youtube.com/watch?v=YGGq0AE5Uyc"
            pull_ups = "https://www.youtube.com/watch?v=XB_7En-zf_M"
            return f'{push_press}\n{squat_jumps}\n{pull_ups}'
        if self.plan == "strength":
            bench_press = "https://www.youtube.com/shorts/EdDqD4aKwxM"
            barbell_squats = "https://www.youtube.com/shorts/gslEzVggur8"
            deadlifts = "https://www.youtube.com/shorts/McCDaAsSeRc"
            return f'{bench_press}\n{barbell_squats}\n{deadlifts}'
        if self.plan == "body weight":
            push_ups = "https://www.youtube.com/watch?v=IODxDxX7oi4"
            pistol_squats = "https://www.youtube.com/shorts/5R3wjhmjhgU"
            pull_ups = "https://www.youtube.com/watch?v=XB_7En-zf_M"
            return f'{push_press}\n{squat_jumps}\n{pull_ups}'
    def __str__(self):
        if self.plan == "athlete":
            return f'{self.generate_intensity_plan()}\n\nHere are the guides: \n{self.youtube_links()}'
        if self.plan == "strength":
            return f'{self.generate_powerlifting_plan()}\n\nHere are the guides: \n{self.youtube_links()}'
        if self.plan == "body weight":
            return f'{self.generate_calisthenics_plan()}\n\nHere are the guides: \n{self.youtube_links()}'

def main():
    fitness_preference = input("Select a workout plan (athlete/strength/body weight): ")
    fitness_time = int(input("How long do you want to train for (min): "))
    myplan = WorkOut(fitness_time, fitness_preference)
    print(f'\nHere is your workout plan:\n{myplan}')

main()
