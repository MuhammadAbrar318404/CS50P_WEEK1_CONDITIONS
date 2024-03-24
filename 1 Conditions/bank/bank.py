def main():
    #Asking the user for the greetings
    greeting = input("Greetings: ")
    # Checking either user greeted with word starts with h and it is not hello
    if greeting.startswith("H") and "Hello" not in greeting:
        print("$20")
    #checking either the greeting have hello
    elif "Hello" in greeting:
        print("$0")
    #All other conditions 
    else:
        print("$100")
    # Calling the main  function
main()
