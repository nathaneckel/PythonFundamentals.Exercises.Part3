#Helper Functions
#Function: Language Selector Prompt
def pick_language():
    selected_language = int(input("Hola, Bonjour, Hello!  Please pick a language:\n" + "For Spanish press 1. \n" + "For French Press 2 \n" +"For English Press 3."))
    return(selected_language)

#Function: Asking for name using chosen language

def name_prompt(selected_language):
    if(selected_language == 3):
        name = input("What is your name?")
        return name
    elif(selected_language == 1):
        name = input("Como se llama?")
        return name
    elif (selected_language == 2):
        name = input("Comment vous appelez-vous?")
        return name
    else:
        print("Please try again, I'm sorry but I didn't understand your selection")

#Function Greet - takes name from what_is_your_name and prints that variable with a greeting

def greeting(name, selected_language):
    if (selected_language == 3):
        print("Hello " + name + "!")
    elif (selected_language == 1):
        print("Hola " + name + "!")
    elif (selected_language == 2):
        print("Bonjour " + name + "!")
    else:
        print("Please try again, I'm sorry but I didn't understand your selection")
    return

#Function: MAIN - This Calls All the Helpers In Order
def main():
    selected_language = pick_language()
    name = name_prompt(selected_language)
    greeting(name, selected_language)

main()
