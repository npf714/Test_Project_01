A = 41
B = 40
C = 45
D = input("Hello, would you like to play a game? ")
if D == "Yes":
    print("Okay lets get started")
else:
    print("Maybe next time")



Guess = 1
E = int(input("Please enter a number between 1 - 50: "))
if E < 40:
    print("Please enter a number between 1 and 50 only. ") 
    int(input('Please choose again: '))
    Guess += 1
    while (E < 40) or (E > 45):
        print("That is not the correct number.")
        E = int(input("Please try again: "))
        Guess += 1
        while E == 40 or E == 45:
            print("Your guess is within 5 digits of the correct number.")
            E = int(input("Please try again. "))
            Guess += 1
if E == 41:
    print("You guessed the correct number. Congratulations!")
    Guess += 1
else:
    print("Your out of chances. ")
print(f"It took you exacly {Guess} attempts to guess correctly.")
    
        
print("Hello")











        
             
    
             

