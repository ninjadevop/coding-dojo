class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"first_name: {self.first_name}")
        print(f"last_name: {self.last_name}")
        print(f"email: {self.email}")
        print(f"age: {self.age}")
        print(f"is_rewards_member: {self.is_rewards_member}")
        print(f"gold_card_points: {self.gold_card_points}")
        print("******************************************************************")

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        if self.email:
            print("User already a member")
            return False
        else:
            return True

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("you dont have enought money")
            return
        self.gold_card_points -= amount


my_user = User("khaled", "hannachi", "khaled @ gmail.com", 33)
my_user.display_info().enroll().spend_points(1000)
