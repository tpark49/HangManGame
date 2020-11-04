# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    for i in secret_word: 
        if i in letters_guessed: 
            continue
        else: 
            return False 
    return True 


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    answer = ""
    for i in secret_word: 
        if i in letters_guessed: 
            answer+=i
        else: 
            answer+="_"
    return answer



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    list_word = list(string.ascii_lowercase)
    for i in letters_guessed: 
        if i in list_word: 
            list_word.remove(i)
        else: 
            continue 
    return "".join(list_word)
    
    
    

def hangman(secret_word):
    
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
   '''

    guesses = 6
    warning = 3
    letters_guessed = []
    guessed_before = False
    
    print("Welcome to hangman. You will have 6 guesses to guess the correct word....Good luck")
    print("The secret word has " + str(len(secret_word)) + " letters")
    
    
    while guesses >0: 
        word_sofar = get_guessed_word(secret_word, letters_guessed)
        #get input from user 
        user_input = input("Please enter your guess?")
        
        if len(user_input)<2:
            #check if user guessed this word before
            if user_input in letters_guessed:
                guessed_before = True 
                if warning == 1:
                    print("you've run out of warnings, we will deduct a guess")
                    guesses -=1
                else: 
                    warning-=1
            else:
                guessed_before = False 
        else: 
            if user_input == secret_word: 
                print("Congrats, you won!")
                return 
            else: 
                guesses-=1
            
        
        #add new guess to letters_gussed list 
        letters_guessed.append(user_input)
    
        
        #check if user got the correct word 
        if is_word_guessed(secret_word, letters_guessed): 
            print("congratulations you won!")
            return 
        else:
            #check if user is asking for hint 
            if user_input == "*":
                pass
            else: 
                guesses -=1
        
        
        
        #if it hasn't been guessed, is it correct? 
        word_sofar = get_guessed_word(secret_word, letters_guessed)
        if guessed_before:
            print("the letter has been guessed before: " + str(word_sofar))
        else: 
            if user_input in secret_word:
                print("Good job! You've guessed: " + str(word_sofar))
                print("you have this many guesses left: " + str(guesses))
            else: 
                print("try again! You've guessed: " + str(word_sofar))
                print("you have this many guesses left: " + str(guesses))
                
                
        #give hint if * was entered 
        hint = []
        if user_input == "*":
            wordlist = load_words()
            for i in wordlist: 
                if len(secret_word) == len(i) and match_with_gaps(word_sofar, i):
                    hint.append(i)
            print(hint)
    
                
    print("Sorry you have lost...!")
    print("The word was..." + secret_word)
    return 
                
        
        #if correct, check if the game is over 
        
        
        #if not over, then reflect new secret_word & add to letters_gussed
        
        
        
        #if not correct, add to letters_gusssed, then subtract # of guesses 
        
    
    
    
    # When you've completed your hangman function, scroll down to the bottom
    # of the file and uncomment the first two lines to test
    #(hint: you might want to pick your own
    # secret_word while you're doing your own testing)
    
    
    # -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in range(len(my_word)):
        if my_word[i] == "_" or my_word[i] == other_word[i]:
            continue 
        else: 
            return False 
    return True 



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
        
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
