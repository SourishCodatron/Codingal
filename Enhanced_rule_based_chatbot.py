import re, random
import time
from datetime import datetime
from zoneinfo import ZoneInfo
from colorama import Fore, init
init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

weather = [
    "The weather is sunny, with 40℃ with AQI reported as very bad",
    "The weather is rainy, with 28℃ with AQI reported as moderate",
    "The weather is windy, with 36℃ with AQI reported as very very bad"
]

news = [
    "Lionesses squad boost — Ella Toone and Aggie Beever‑Jones return ahead of the World Cup play‑off",
    "Ukraine–Russia conflict escalates — Ukraine launched 1,441 drones into Russia overnight, according to Moscow, marking one of the largest drone attacks of the war",
    "Odisha and Andhra Pradesh have shut schools and begun evacuations as Cyclone Akvan intensifies over the Bay of Bengal"
]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def get_valid_name():
    return input(f"{Fore.RED} No blanks for filling the name. If you wish to be anonymous, press ENTER Key : ")

def show_processing_animations():
    print("25%")
    time.sleep(0.25)
    print("50%")
    time.sleep(0.25)
    print("75%")
    time.sleep(0.25)
    print("100%, Completed")
    time.sleep(0.25)
    return 

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You : ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
        recommend()

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")

def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.GREEN + "- Tell weather report  (say 'weather')")
    print(Fore.GREEN + "- Report news (say 'news')")
    print(Fore.GREEN + "- Tell the time around the world (say 'time')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

def weather_reports():
    show_processing_animations()
    print(Fore.YELLOW + f"TravelBot: {random.choice(weather)}")

def news_report():
    print(Fore.YELLOW + f"TravelBot: {random.choice(news)}")

def Time_report():
    print(f"{Fore.CYAN}TravelBot: UTC, Riyadh or New York")
    preference = input(Fore.YELLOW + "You: ")

    if preference == "UTC":
            utc = datetime.now(ZoneInfo("UTC"))
            print(f"Utc Time: {utc}")
            return
    elif preference == "Riyadh":
            ry_tz = datetime.now(ZoneInfo("Asia/Riyadh"))
            print(f"Riyadh time: {ry_tz}")
            return
    elif preference == "New York":
            ny_tz = datetime.now(ZoneInfo("America/New_York"))
            print(f"New york Time: {ny_tz}")
            return
    else:
            print(Fore.RED + "TravelBot: Does not exist")
    Time_report()

def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? : ")
    if not name:
        name = get_valid_name() or "unknown"
    conversation_history = []
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()
    
    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()

        elif "joke" in user_input or "funny" in user_input:
            tell_joke()

        elif "help" in user_input:
            show_help()

        elif "weather" in user_input or "report1" in user_input:
            weather_reports()

        elif "news" in user_input or "report2" in user_input:
            news_report()

        elif "time" in user_input:
            Time_report()

        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break

        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")
        continue
chat()