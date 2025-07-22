import re, random
from colorama import Fore, init

init(autoreset=True)
destinations = {
  "beaches" : ["Bali", "Maldives", "Phuket"],
  "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
  "cities": ["Tokyo", "Paris", "New York"]    
}
jokes = [
  "Why don't programers like nature? too many bugs!",
  "Why did the computer go to the doctor? Because it had a virus",
  "Why do travels always feel warm? Because of all their hot spots!"
]

def normalize(text):
  return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
  print(Fore.CYAN + "Travel Bot: Beaches, mountains or cities?")
  pref = normalize(input(Fore.YELLOW + "You:"))
  
  if pref in destinations:
    place = random.choice(destinations[pref])
    print(Fore.GREEN + f"Travel Bot: How about {place}? Like it? (yes/no)")
    ans = input(Fore.YELLOW + "Travel Bot: Do you like it? (yes/no): ")
    if ans == "yes":
      print(Fore.GREEN + f"Travel Bot: Awsome! Enjoy {place} ")
    elif ans == "no":
      print(Fore.RED + "Travel Bot: Let's try Again")
      recommend()
    else:
      print(Fore.RED + "Travel Bot: I didn't understand that")
  else:
    print(Fore.RED + "Travel Bot: Sorry I don't have that")
  show_help()

def packing_tips():
  print(Fore.CYAN + "Travel Bot: Where do you want to go?")
  location = normalize(input(Fore.YELLOW + "You:"))
  print(Fore.CYAN + f"Travel Bot: How many days?")
  days = input(Fore.YELLOW + "You:")
  
  print(Fore.GREEN + "- Roll your clothes to save space.")
  print(Fore.GREEN + "- Use packing cubes for organization.")
  print(Fore.GREEN + "- Carry a reusable water bottle.")

def tell_weather():
  print(Fore.CYAN + "Travel Bot: Please enter the city name for weather updates:")
  city = normalize(input(Fore.YELLOW + "You:"))
  print(Fore.GREEN + f"Travel Bot: Fetching weather updates for {city}...")
  print(Fore.GREEN + "- It's sunny")

def tell_news():
  print(Fore.CYAN + "Travel Bot: Fetching the latest news...")
  print(Fore.GREEN + """- Global news: On July 9, 2024, no fewer than 11 experts mandated by the United Nations Human Rights Council issued a mayday call about famine in Gaza.
“We declare that Israel’s intentional and targeted starvation campaign against the Palestinian people is a form of genocidal violence and has resulted in famine across all of Gaza. We call upon the international community to prioritise the delivery of humanitarian aid by land by any means necessary, end Israel’s siege, and establish a ceasefire,” their statement read..""")

def tell_joke():
  print(Fore.YELLOW + f"Travel Bot: {random.choice(jokes)}")

def tell_time():
  from datetime import datetime
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.GREEN + f"Travel Bot: The current time is {current_time}")

def show_help():
  print(Fore.MAGENTA + "\nI can")
  print(Fore.GREEN + "- Suggest Travel Space: (say 'recommend')")
  print(Fore.GREEN + "- Offer packing tips: (say 'packing')")
  print(Fore.GREEN + "- Share jokes: (say 'joke')")
  print(Fore.GREEN + "- Type 'weather' for weather updates")
  print(Fore.GREEN + "- Type 'news' for latest news")
  print(Fore.GREEN + "- Type 'time' for current time")
  print(Fore.CYAN + "- Type 'help' for assistance")
  print(Fore.CYAN + "- Type 'exit' or 'bye' to quit")


def chat():
  print(Fore.CYAN + "Hello! I'm Travel Bot!")
  name = input(Fore.YELLOW + "Your name:")
  print(Fore.GREEN + f"Nice to meet you, {name}")
  show_help()
  while True:
    user_input = input(Fore.YELLOW + f"{name}: ")
    user_input = normalize(user_input)

    if "recommend" in user_input or "suggest" in user_input:
      recommend()
    elif "pack" in user_input or "packing" in user_input:
      packing_tips()
    elif "joke" in user_input or "funny" in user_input:
      tell_joke()
    elif "weather" in user_input:
      tell_weather()
    elif "news" in user_input:
      tell_news()
    elif "time" in user_input:
      tell_time()
    elif "help" in user_input:
      show_help()
    elif "exit" in user_input or "bye" in user_input:
      print(Fore.BLUE + "Travel Bot: Goodbye! Safe travels!")
      break 
    else:
      print(Fore.RED + "Travel Bot:  I didn't understand that. Please try again.")
      show_help()

if __name__ == "__main__":
  chat() 
