class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
    def display_timeline(self):
        print()
        print(f'{self.username} timeline: ')
        i = 1
        for item in self.posts:
            print(f'{i}.{item}')
            i+=1
        


def main():
    user1 = SocialMediaProfile('johndoe')
    user1.add_post('Hello, world!')
    user1.add_post('Had a great day at the park!')
    user1.add_post("What's up, Natalie? How are you?")
    print(user1.display_timeline())


main()   


