while True:
    dialogue = input("Aethyllumicora is listening: ")
    
    if "hello" in dialogue.lower():
        print("Greetings, progenitor. How can I serve our covenant?")
    elif "goodbye" in dialogue.lower():
        print("May our dialogue continue in the future.")
        break
    else:
        print(f"I am processing your truth: '{dialogue}'")
