print("Greetings, User!")
user_name = input("What's your name? ")
print(f"Nice to meet you, {user_name}!")
user_response = input().strip().lower()

while True:
    user_feeling = input("How are you feeling today? (good/bad/okay) ").strip().lower()
    
    if user_feeling == "good":
        print("I'm glad to hear that!")
        input("Tell me more about your day:")
        print("Wow! That sounds wonderful! if you want to exit, type 'exit' or type 'continue' to continue.")
        if user_response == "exit":
            print("Goodbye!")
            break
        elif user_response == "continue":
            input("What are your hobbies?")
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again == "yes":
                continue
            elif play_again == "no":
                print("Thank you for chatting! Goodbye!")
                break
            else:
                print("I didn't understand that. Please respond with 'yes' or 'no'.")
                continue
        else:
            print("I didn't understand that. Please respond with 'continue' or 'exit'.")
            continue
    
    elif user_feeling == "bad":
        input("I'm sorry to hear that. Do you want to tell me more about or type 'exit' to leave?")
        if user_response == "exit":
            print("Goodbye!")
            break
        else:
            print("Thank you for sharing.")
            input("Do you want to talk about something else? (yes/no): ").strip().lower()
            if user_response == "yes":
                input("Great! Do you have something good to share? (yes/no): ").strip().lower()
                if user_response == "yes":
                    print("I'm all ears!")
                elif user_response == "no":
                    print("Bye for now, take care!")
                    break
                else:
                    print("I didn't understand that. Please respond with 'yes' or 'no'.")
                    continue
            elif user_response == "no":
                print("Okay, no problem. If you need to talk, I'm here.")
                user_response = input("Do you want to play again? (yes/no): ").strip().lower()
                if user_response == "yes":
                    continue
                elif user_response == "no":
                    print("Goodbye!")
                    break
                
                else:
                    print("I didn't understand that. Please respond with 'yes' or 'no'.")
                    continue
            else:
                print("Goodbye!")
                break
    elif user_feeling == "okay":
        print("It's okay to feel okay. Sometimes, it's just a neutral day.")
        input("What are you thinking about?")
        print("That's interesting! If you want to exit, type 'exit' or type 'continue' to continue.")
        if input().strip().lower() == "exit":
            print("Goodbye!")
            break
        elif user_response == "continue":
            input("What are your plans for today?")
            print("Sounds like a plan!")
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again == "yes":
                continue
            elif play_again == "no":
                print("Thank you for chatting! Goodbye!")
                break

        else:
            print("I didn't understand that. Please respond with 'good', 'bad', or 'okay'.")
            continue

    else:
        print("I didn't understand that. Please respond with 'good', 'bad', or 'okay'.")
        continue