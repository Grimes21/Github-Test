# This will be a hangman game
import random
# secret work the player is trying to guess

mylist = ['blue', 'joint', 'alummunium', 'kettle']

secretword = random.choice(mylist)

lettersguessed = ''

#Thenumber of turns before the player loses
failurecount = 6


#Looptill player has made too many failed attempts
#Will break when they succeed instead

while failurecount > 0:
    
    
    #Get Letter
    guess = input('Enter a letter: ')
    
    if guess in secretword:
        print('Correct! There is one or more', guess, 'in the secret word')
    else:
        failurecount -= 1
        print('Incorrect, There are no', guess, 'in the secret word.', failurecount, 'turn(s) left.')
        
    #Maintain list of all letters guessed
    
    lettersguessed = lettersguessed + guess 
    
    wronglettercount = 0
    
    
    for letter in secretword:
        if letter in lettersguessed:
            print(f'{letter}', end=' ')
        else:
            print('_', end=' ')
            wronglettercount += 1
            
    if wronglettercount == 0:
        print(f'Congradulations! The secret word was: {secretword}. You won!')
        again = input('Would you like to go again')
        if again == 'no':
            break

else:
    print('Sorry, your a moron and you lost, the secret word was', secretword)
    
test = secretword*2