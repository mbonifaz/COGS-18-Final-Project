import random
from random import randint
from fractions import Fraction 

correct_response = ['Correct! You got it!', 'YOU ROCK!', 'Awesome!', "You're a math wiz!"]
wrong_response = ['Not quite. Keep Practicing!', 'Incorrect, Try again!', "Wrong but you'll get the hang of it!"]

def input_check():
    """This function is used to ensure that the user's input is within the range of options provided."""
    
    while True:
        try:
            #the user input given must be an integer for the game to continue
            user_input = int(input(''))
         
            if user_input < 1:
                raise ValueError('This is not an option choice. Please try again.')  
            elif user_input > 7:
                raise ValueError('This is not an option choice. Please try again.')
            else:
                return user_input
                break
        #this ValueError ensures that if a user inputs any letter of the alpha or a symbol, the print statement below will repeat until they input a correct option.
        except ValueError:
            print('This is not an option choice. Please try again.')
            continue
    
        
def game_options():
    """ This function is used to ask the user which type of math problems they would like to practice."""
    print('1 - addition')
    print('2 - subtraction')
    print('3 - multiplication')
    print('4 - division')
    print('5 - squares')
    print('6 - square root')
    print('7 - Exit Game.')

    #user_input is equal to input check because we want to make sure what the user is inputting will allow the game to continue. 
    user_input = input_check()
      
    if user_input == 1:
        addition()
    elif user_input == 2:
        subtraction()
    elif user_input == 3: 
        multiplication()
    elif user_input == 4: 
        division()
    elif user_input == 5: 
        squares()
    elif user_input == 6: 
        square_root()
    elif user_input == 7: 
        return None 

    
def game_intro():
    """This function is used to introduce the Math Game, provide the instructions, and start the game"""
    
    print('WELCOME TO MATH PRACTICE!')
    print('Practice your mental math abilities, use a paper and pencil if you need, and maybe try to improve your speed!')
    print('Which would you like to start with?')
    game_options()
    
         
def play_game():
    """This function is used to continue asking the user which topic they want to practice, and then providing them with the options"""
    print('Choose your next topic.')
    game_options()
    

def addition():
    """Assigns variables number_1 and number_2 to a random number, creates an addition problem and asks user for correct answer."""

    number_1 = randint(0,100)
    number_2 = randint(0,100)
    
    print('What is ' + str(number_1) + '+' + str(number_2) + '?') 
    print('Please enter ONLY a whole number or decimal.')

    user_input = input(" ")
    
    if int(float(user_input)) == number_1 + number_2:
        print(random.choice(correct_response))
        play_game()
    else:
        print(random.choice(wrong_response))
        print('The answer is ' + str(number_1 + number_2) + '.')
        play_game()
            
    
def subtraction():
    """Assigns variables number_1 and number_2 to a random number, creates a subtraction problem and asks user for correct answer."""

    number_1 = randint(0,100)
    number_2 = randint(0,100)
    
    print('What is ' + str(number_1) + '-' + str(number_2) + '?')
    print('Please enter ONLY a whole number or decimal.')

    user_input = input(" ")
    
    if int(float(user_input)) == number_1 - number_2:
        print(random.choice(correct_response))
        play_game()
    else:
        print(random.choice(wrong_response))
        print('The answer is ' + str(number_1 - number_2) + '.')
        play_game()
     
        
def multiplication():
    """Assigns variables number_1 and number_2 to a random number, creates a multiplication problem and asks user for correct answer."""

    number_1 = randint(0,100)
    number_2 = randint(0,100)
    
    print('What is ' + str(number_1) + 'x' + str(number_2) + '?')
    print('Please enter ONLY a whole number or decimal.')
   
    user_input = input(' ')
    if int(float(user_input)) == number_1*number_2:
        print(random.choice(correct_response))
        play_game()
    else:
        print(random.choice(wrong_response))
        print('The answer is ' + str(number_1 * number_2) + '.')
        play_game()
    

def division(): 
    """Assigns variables number_1 and number_2 to a random number, creates a division problem and asks user for correct answer."""

    number_1 = randint(0,20)
    number_2 = randint(0,20)
    
    print('What is ' + str(number_1) + '/' + str(number_2) + '?')
    print('Please enter ONLY a whole number or decimal.')

    user_input = input(' ')
    
    if int(float(Fraction(user_input))) == number_1 / number_2:
        print(random.choice(correct_response))
        play_game()
    else:
        print(random.choice(wrong_response))
        print('The answer is ' + str(number_1 / number_2) + '.')
        play_game()
        
        
def squares():
    """Assigns variables number_1 to a random number and asks user for correct answer for the square of a number."""

    number_1 = randint(0,25)
    
    print('What is the square of ' + str(number_1) + '?')
    print('Please enter ONLY a whole number or decimal.')

    user_input = input(' ')
    
    if int(float(user_input)) == number_1 **2:
        print(random.choice(correct_response))
        play_game()
    else:
        print(random.choice(wrong_response))
        print('The answer is ' + str(number_1**2) + '.')
        play_game()

        
def square_root():
    """Assigns variables number_1 to a random number and asks user for correct answer for the square root of a number."""

    number_1 = randint(0,49)
    
    print('What is the square root of '+ str(number_1) + '?')
    print('Please enter ONLY a whole number or decimal.')

    user_input = input(' ')
    
    #if statement conditional states that a user input that is equal to the answer of the square root of the random integer, the answer is correct.
    if int(float(user_input)) == number_1**(1/2):
        print(random.choice(correct_response))
        play_game()
    else:
        print(random.choice(wrong_response))
        print('The answer is ' + str(number_1**(1/2)) + '.')
        play_game()

