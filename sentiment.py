import colorama
from colorama import Fore, Style
from textblob import TextBlob

def show_processing_animation():
    print(f"{Fore.CYAN}Processing your input...")

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        senti = "Positive"
    elif polarity < 0:
        senti = "Negative"
    else:
        senti = "Neutral"

    return polarity, senti

def execute_command(command):
    if command == "reset":
        return show_processing_animation(), "Conversation history cleared!"
    elif command == "history":
        return show_processing_animation(), "Displaying conversation history..."
    elif command == "exit":
        return show_processing_animation(), "Exiting the program..."
    elif command == "help":
        return show_processing_animation(), "Available commands: reset, history, exit, summary, help"
    elif command == "summary":
        return show_processing_animation(), "Displaying conversation summary..."

    else:
        return "I don't understand that."

colorama.init(autoreset=True)
print(f"{Fore.CYAN}Welcome to Sentiment Spy!")
user_name = input(f"{Fore.CYAN}Enter your name:")
print(f"{Fore.CYAN}Hello Agent {user_name}, enter your feelings to analyze them.")
print(f"Commands: {Fore.YELLOW}reset, history, summary, help, exit")
history = []

while True:
    text = input(f"{Fore.GREEN}>>").strip()
    if not text:
        print(f"{Fore.RED}Enter some text")
        continue
    cmd = text.lower()
    if cmd == "exit":
        show_processing_animation()
        print(f"{Fore.BLUE}Exiting.. Farewell, Agent {user_name}")
        break
    if cmd == "reset":
        show_processing_animation()
        history.clear()
        print(f"{Fore.CYAN}Conversation history cleared!")
        continue
    if cmd == "history":
        show_processing_animation()
        if not history:
            print(f"{Fore.YELLOW}History has been reset")
        else:
            for i, (msg, pol, senti) in enumerate(history, 1):
                color = Fore.GREEN if senti == "Positive" else Fore.RED if senti == "Negative" else Fore.YELLOW
                print(f"{i}. {color}{msg}(polarity : {pol: .2f}, {senti})")
        continue
    if cmd == "help":
        show_processing_animation()
        print(f"{Fore.CYAN}Available commands: reset, history, exit, summary, help")
        continue
    if cmd == "summary":
        show_processing_animation()
        if not history:
            print(f"{Fore.YELLOW}No conversation history available.")
        else:
            total = len(history)
            positive = sum(1 for _, _, senti in history if senti == "Positive")
            negative = sum(1 for _, _, senti in history if senti == "Negative")
            neutral = total - positive - negative
            avg_polarity = sum(pol for _, pol, _ in history) / total
            print(f"{Fore.CYAN}Summary Report:")
            print(f"Total messages: {total}")
            print(f"{Fore.GREEN}Positive: {positive}")
            print(f"{Fore.RED}Negative: {negative}")
            print(f"{Fore.YELLOW}Neutral: {neutral}")
            print(f"{Fore.MAGENTA}Average polarity: {avg_polarity:.2f}")
        continue

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    show_processing_animation()
    if polarity > 0:
        senti = "Positive"
    elif polarity < 0:
        senti = "Negative"
    else:
        senti = "Neutral"

    history.append((text, polarity, senti))

    result_color = Fore.GREEN if senti == "Positive" else Fore.RED if senti == "Negative" else Fore.YELLOW
    print(f"{result_color}Sentiment: {senti} (Polarity: {polarity:.2f})")