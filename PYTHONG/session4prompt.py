class FavoriteAnimal:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print(f"Physical Characteristics of my Favorite Animal: Arm Length: {self.arm_length} feet Leg Length: {self.leg_length} feet")
        print(f"Number of Eyes: {self.num_eyes} Has Tail: {'Yes' if self.has_tail else 'No'} Is Furry: {'Yes' if self.is_furry else 'No'}")

def main():
    my_favorite_animal = FavoriteAnimal(5, 4, 2, True, True)
    my_favorite_animal.describe()
if __name__=="__main__":
    main()