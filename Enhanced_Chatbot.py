print("Hello! I am Verity. I know everything, What's your name? : ")
name = input()
print(f"Nice to meet you, {name}!")
print("How are you feeling today? (good/bad) : ")
mood = input().lower()
if mood == "good":
    print("I'm glad to hear that!")
    print("What are your hobbies? :")
    hobbies = input().lower()
    print(f"Interesting! {hobbies} sounds like a fun activity.")
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon.")
    print("If you don't mind, can you tell me your hobbies if your mood is at ease? (yes/no) :")
    mood = input().lower()
    if mood == "yes":
        print("What are your hobbies? :")
        hobbies = input().lower()
        print(f"Interesting! {hobbies} sounds like a fun activity.")
    elif mood == "no":
        print("That's okay. We can talk about something else.")
else:
    print("I see. Sometimes it's hard to put feelings into words.")
    print("Are you interested in sharing your hobbies? (yes/no) :")
    if mood == "yes":
        print("What are your hobbies? :")
        hobbies = input().lower()
        print(f"Interesting! {hobbies} sounds like a fun activity.")
    elif mood == "no":
                print("That's okay. We can talk about something else.")
print(f"It was nice chatting with you {name}. Goodbye!")