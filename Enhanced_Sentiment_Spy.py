import colorama
from colorama import Fore, Style
from textblob import TextBlob
import time
colorama.init()

def get_valid_name():
    return input(f"{Fore.RED} No blanks for filling the name. If you wish to be anonymous, press ENTER Key : {Style.RESET_ALL}")
    

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

def analyze_sentiment(start=1):
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment = "Positive"
        color = Fore.GREEN
        emoji = "👍"
    elif polarity < -0.25:
        sentiment = "Negative"
        color = Fore.RED
        emoji =  "👎"
    else:
        sentiment = "Neutral"
        color = Fore.YELLOW
        emoji = "😭"
    return polarity, sentiment, color, emoji

user_name = input
def execute_command(user_input):
    
    
    if user_input.lower()== "reset":
        conversation_history.clear()
        print(f"{Fore.GREEN}Conversation History Cleared")
        return
        
    
    elif user_input.lower() == "history":
            if not conversation_history:
                    print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
            else:
                    print(f"{Fore.CYAN} Conversation History:{Style.RESET_ALL}")
                    for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                    
                        if sentiment_type == "Positive":
                            color = Fore.GREEN
                            emoji = "😊"
                        elif sentiment_type == "Negative":
                            color = Fore.RED
                            emoji = "😞"
                        else:
                            color = Fore.YELLOW
                            emoji = "😭"
        
                        print(f"{idx}. {color}{emoji} {text} "
                            f"Polarity: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}")
            return
        
    if user_input.lower() == "help":
        print(f"{Fore.CYAN}Exit for exiting Sentiment Spy, getting a generated summary and getting saved into a file.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Help for these instructions{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Summary for viewing your sentiment counts{Style.RESET_ALL}")
        print(f"{Fore.CYAN}History for viewing all inputs you entered{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Reset for clearing the history of a conversation{Style.RESET_ALL}")
        return

    if user_input.lower() == "summary":
        if not conversation_history:
            print(f"{Fore.BLUE}Summary : Unavailable{Style.RESET_ALL}")
            return
        else:
            print(f"{Fore.BLUE}Summary :{Style.RESET_ALL}")
            positive = sum(1 for _, _,  sentiment in conversation_history if sentiment == "Positive")
            negative = sum(1 for _, _, sentiment in conversation_history if sentiment == "Negative")
            neutral = sum(1 for _, _, sentiment in conversation_history if sentiment == "Neutral")
            print(f"{Fore.GREEN}Positive : {positive}{Style.RESET_ALL}")
            print(f"{Fore.RED}Negative : {negative}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Neutral : {neutral}{Style.RESET_ALL}")
            return
 
    if user_input.lower()== "exit":
        while True:
            if not conversation_history:
                print(f"{Fore.CYAN}Summary : Unavailable{Style.RESET_ALL}")
                return
            else:
                print(f"{Fore.BLUE}Summary :{Style.RESET_ALL}")
                positive = sum(1 for _, _,  sentiment in conversation_history if sentiment == "Positive")
                negative = sum(1 for _, _, sentiment in conversation_history if sentiment == "Negative")
                neutral = sum(1 for _, _, sentiment in conversation_history if sentiment == "Neutral")
                print(f"{Fore.GREEN}Positive : {positive}{Style.RESET_ALL}")
                print(f"{Fore.RED}Negative : {negative}{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Neutral : {neutral}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}Saved to {user_name}_Exit_Summary.txt")
                return
           
print(f"{Fore.MAGENTA} 🕵️🕵️🕵️🕵️🕵️🕵️  Welcome to Sentiment Spy!  🕵️🕵️🕵️🕵️🕵️🕵️ {Style.RESET_ALL}")
user_name = input(f"{Fore.RED}Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = get_valid_name() or 'unknown'
conversation_history = []
print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a Sentence and I will analyze your sentences with TextBlob and show you the sentiment i.e. Positive, Negative, or Neutral. ")
print(f"Type {Fore.MAGENTA}reset{Fore.CYAN}, {Fore.RED}history{Fore.CYAN}, {Fore.YELLOW}exit{Fore.CYAN} to quit, {Fore.GREEN}help{Fore.CYAN} for assistance, or {Fore.BLUE}summary{Fore.CYAN} to view a summary.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.WHITE}>>>{Style.RESET_ALL}")
    if not user_input:
            print(f"{Fore.RED}Enter valid command or text{Style.RESET_ALL}")
            continue

    if user_input == "history":

        execute_command(user_input)
        continue

    if user_input == "summary":
        execute_command(user_input)
        continue

    if user_input == "reset":
        execute_command(user_input)
        continue

    if user_input == "help":
        execute_command(user_input)
        continue

    if user_input == "exit":
        execute_command(user_input)
        break

    show_processing_animations()
    analysis = analyze_sentiment(user_input)
    polarity, sentiment_type, color, emoji = analysis
    conversation_history.append((user_input, polarity, sentiment_type))
    print(f"{color}{emoji} {sentiment_type} sentiment detected! "
            f"Polarity: {polarity:.3f}")
    continue
    