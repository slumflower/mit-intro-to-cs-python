#wordlist and helper code not included below


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    user_input = ""
    
    for char in secretWord:
        if char in lettersGuessed:
            user_input += char
        else:
            user_input += " _ "
    return user_input



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...  
    import string
    lettersLeft = string.ascii_lowercase
    
    for char in lettersGuessed:
        lettersLeft = lettersLeft.replace(char, '')
    return lettersLeft
  
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...


    guesses = 8
    lettersGuessed = []
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord),'letters long.')
    print("-------------")
    
    
    while (guesses != 0):
        
        print("You have ", str(guesses),"guesses left.")
        print("Available letters: ", getAvailableLetters(lettersGuessed))
        
        char = input("Please guess a letter: ")
        char = char.lower()
        
        if char in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
            
        elif char in secretWord:
            lettersGuessed.append(char)
            print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
        
        else: 
            guesses -= 1
            lettersGuessed.append(char)
            print("Oops! That letter is not in my word: ",getGuessedWord(secretWord, lettersGuessed))
    
        print("-------------")
        
        if isWordGuessed(secretWord, lettersGuessed) == True : 
            print('Congratulations, you won!')
            break

    
    if guesses == 0:  
        print("Sorry, you ran out of guesses. The word was ", secretWord,".")
       
       


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
