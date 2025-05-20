import random

data = [
    {"name": "Cristiano Ronaldo", "follower_count": 652_000_000, "description": "Portuguese footballer, widely regarded as one of the greatest of all time"},
    {"name": "Lionel Messi", "follower_count": 505_000_000, "description": "Argentinian footballer, known for his incredible dribbling and playmaking skills"},
    {"name": "Selena Gomez", "follower_count": 421_000_000, "description": "American actress and singer, former Disney star turned global pop icon"},
    {"name": "Dwayne Johnson", "follower_count": 394_000_000, "description": "Hollywood actor and former WWE wrestler, known as 'The Rock'"},
    {"name": "Kylie Jenner", "follower_count": 394_000_000, "description": "Media personality and businesswoman, founder of Kylie Cosmetics"},
    {"name": "Ariana Grande", "follower_count": 376_000_000, "description": "Singer and actress, famous for her powerful vocals and pop hits"},
    {"name": "Kim Kardashian", "follower_count": 357_000_000, "description": "Media personality and entrepreneur, known for her influence in fashion and beauty"},
    {"name": "Beyoncé", "follower_count": 312_000_000, "description": "Singer and performer, celebrated for her vocal talent and stage presence"},
    {"name": "Virat Kohli", "follower_count": 271_000_000, "description": "Indian cricketer, former captain of the national team and a batting powerhouse"},
    {"name": "Jennifer Lopez", "follower_count": 249_000_000, "description": "Singer, actress, and dancer, known for her versatility in entertainment"},
    {"name": "Neymar Jr.", "follower_count": 229_000_000, "description": "Brazilian footballer, famous for his flair and technical skills"},
    {"name": "Nicki Minaj", "follower_count": 226_000_000, "description": "Rapper and singer, known for her unique style and lyrical prowess"},
    {"name": "Zendaya", "follower_count": 179_000_000, "description": "Actress and singer, acclaimed for her roles in film and television"},
    {"name": "Kevin Hart", "follower_count": 177_000_000, "description": "Comedian and actor, known for his stand-up performances and movies"},
    {"name": "LeBron James", "follower_count": 159_000_000, "description": "Basketball player, considered one of the greatest in NBA history"}
]

def start_game():
    print("Welcome to Higher or Lower game!")
    
    game_over = False
    score = 0
    while not game_over:
        option_a = random.choice(data)
        option_b = random.choice(data)

        while option_a == option_b:
            option_b = random.choice(data)

        followers_option_a = option_a.get("follower_count")
        followers_option_b = option_b.get("follower_count")

        player_guess = input(f"Who has more followers: option A: {option_a.get("name")} or option B: {option_b.get("name")}?: ")
        if player_guess == "A" and followers_option_a > followers_option_b:
            score += 1
            print(f"Your new score is: {score}, {option_a.get("name")} has more followers than {option_b.get("name")} ")
        elif player_guess == "B" and followers_option_b > followers_option_a:
            score += 1
            print(f"Your new score is: {score}, {option_b.get("name")} has more followers than {option_a.get("name")} ")
        else:
            print(f"You lose, your final score is: {score}")
            game_over = True

start_game()

