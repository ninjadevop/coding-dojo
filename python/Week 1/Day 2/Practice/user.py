class User:
    def __init__(
        self,
        first_name,
        last_name,
        email,
        age,
        is_rewards_member=False,
        gold_card_points=0,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

        # Have this method print all of the users' details on separate lines.

    def display_info(
        self,
    ):
        print(f" {self.first_name} {self.last_name} {self.email} {self.age}")

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_point(self, amount):
        self.gold_card_points -= amount


adam = User("adam", "doma", "a.a@gmail.com", 18)
adam.display_info()
