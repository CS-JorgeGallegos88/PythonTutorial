class User:
    #Init is the class constructor, self would be "this"
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0 #default initialization
        self.following = 0

    def print_name(self):
        print(self.user_id, self.user_name)

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User(user_id="001", user_name="Joey")
user2 = User(user_id="002", user_name="Chandler")
user1.follow(user2)
print(user1.following)


