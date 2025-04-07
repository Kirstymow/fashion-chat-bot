import random
import time

class FashionMoodBot:
    def __init__(self):
        self.sassy_responses = [
            # Mood reactions
            "Oh honey, you’re feeling '{mood}'? Let me fix that with {genre} music and {color} style.",
            "The audacity of your '{mood}' mood... don’t worry, {genre} and {color} will save you.",
            "Not you being '{mood}'... anyway, here’s {genre} and {color} to slay.",
            
            # Style reactions
            "If you're '{mood}', you should wear {color} and listen to {genre}. That'll turn things around.",
            "Honey, you look '{mood}', so you need {color} and {genre} to complete the vibe.",
            
            # Quiz reactions
            "Oh, you picked '{genre}'? Now let me tell you, your '{mood}' mood needs {color}.",
            "This quiz confirms it: you’re '{mood}' today, so wear {color} and listen to {genre}. No regrets."
        ]
        
        self.mood_art = {
            'happy': """
            🌈✨
            (◕‿◕✿)  
            ╰(＾3＾)╯  
            SUNSHINE MODE  
            """,
            'sad': """
            🌧️･ﾟ･  
            (╥_╥)  
            ＿|￣|○  
            *plays Adele*  
            """,
            'angry': """
            💢⚡  
            (╬ Ò﹏Ó)  
            ┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻  
            CHILL. NOW.  
            """,
            'chill': """
            🛋️  
            ( ˘ω˘ )☕  
            ～(つˆДˆ)つ｡☆  
            VIBING AT -10 SPEED  
            """,
            'energetic': """
            ⚡🌟  
            (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧  
            ┗(＾0＾)┓  
            RED BULL MODE  
            """,
            'romantic': """
            🌹🌙  
            (´∀｀)♡  
            ～(^з^)-☆  
            HEARTS IN EYES  
            """
        }

    def greet_user(self):
        greetings = [
            "Hey, how are you doing today, darling?",
            "Hey, what’s up? How’s your mood?",
            "Oh, hey there! What’s the vibe today?",
            "Well, well, well, look who’s here. How are you feeling?",
            "Hi! How’s everything going today?",
            "Hey girl! What’s your vibe today?",
            "Hey slaybot, ready for some fun?"
        ]
        
        # Prompt for user greeting
        user_greeting = input("Say something: ").lower()

        # Check if the user greeting matches any common greetings
        if any(greet in user_greeting for greet in ["hi", "hey", "hey girl", "hey slaybot"]):
            return random.choice(greetings)
        else:
            return "Well, well, well... someone's a bit formal today."

    def get_fashion_advice(self, mood, genre, color):
        # Sassy response based on mood, genre, and color
        response = random.choice(self.sassy_responses)
        return response.format(mood=mood, genre=genre, color=color)

    def get_mood_art(self, mood):
        # Get the mood art for different moods
        return self.mood_art.get(mood, "I don't know that mood!")

    def analyze_style(self, mood):
        style_map = {
            'happy': {'color': 'bright yellow', 'accessory': 'hoop earrings'},
            'sad': {'color': 'soft lavender', 'accessory': 'a cozy scarf'},
            'angry': {'color': 'fire red', 'accessory': 'leather jacket'},
            'chill': {'color': 'sage green', 'accessory': 'oversized hoodie'},
            'energetic': {'color': 'neon pink', 'accessory': 'sneakers'},
            'romantic': {'color': 'deep rose', 'accessory': 'silver necklace'}
        }
        style = style_map.get(mood, {'color': 'black', 'accessory': 'sunglasses'})
        
        print(f"\n✨ **STYLE DIAGNOSIS** ✨")
        print(f"Your {mood} mood demands:")
        print(f"- Color: {style['color'].upper()}")
        print(f"- Must-have: {style['accessory'].upper()}")
        print(f"- Music genre: {random.choice(self.mood_art[mood]).upper()}")
        print("\nNow go manifest this look, or don’t. I’m a bot, not a cop.")

    def ask_quiz(self):
        # A simple quiz to find the user's mood
        print("\nLet's take a quick quiz to figure out your mood and style!")
        time.sleep(1)
        
        # Ask questions and get answers
        mood_answer = input("How are you feeling today? (happy, sad, angry, chill, energetic, romantic): ").lower()
        genre_answer = input("What music genre do you feel like listening to? (pop, rock, r&b, electronic, indie): ").lower()
        color_answer = input("What's your favorite color today?: ").lower()

        # Return the answers for the rest of the process
        return mood_answer, genre_answer, color_answer

    def chat(self):
        # Greet the user
        greeting = self.greet_user()
        print(greeting)
        
        # Ask the quiz questions to get the mood and preferences
        user_mood, user_genre, user_color = self.ask_quiz()

        # Display mood art based on user mood
        mood_art = self.get_mood_art(user_mood)
        print(f"\nMood Art: {mood_art}\n")

        # Get fashion advice based on mood, genre, and color
        fashion_advice = self.get_fashion_advice(user_mood, user_genre, user_color)
        print(f"\nFashion Advice: {fashion_advice}\n")

        # Analyze style based on the mood
        self.analyze_style(user_mood)

def run():
    bot = FashionMoodBot()
    bot.chat()

if __name__ == "__main__":
    run()
