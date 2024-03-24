def main():
    #Asing the user the question 
    answer = input(" What is the answer to the Great Question of Life, the Universe and Everything? ")
    # Checking either user has provided the right answer 
    if answer == "forty two" or answer =="forty-two" or answer == "42":
        print("Yes")
    # if the answer is not right 
    else: 
        print("No")
    # Calling the main  function 
main()
