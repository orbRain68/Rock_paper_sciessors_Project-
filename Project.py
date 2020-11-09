"""
File name: index.py
Description: This code will play the game rock_paper_scissor with you.\
        The user will have to provide the right input by typing Rock or Paper or scissors. \
        The computer will choose Rock or Paper or Scissor randomly and print out the result \
        whether you won or you loss.
"""
### All packages that were used.
from random import randint
import tkinter as tk
### The code that needs to be run.
def main():

    guiFunction()

### A function for Computer's choice
def computerChoice():
    x =   randint(0,2)
    pick = ['rock','paper','scissor']
    return pick[x]

### User's pick
def userChioce():
    userInput = str(input("Enter (rock or paper or scissor): "))
    return userInput
### Processing results
def process(hereMe,cpu):
    if hereMe == cpu:
        return('tie!'.title())
    elif hereMe == 'rock' and cpu == 'scissor':
        return('you won!! CPU chooses ({})\n'.format(cpu))
    elif hereMe == 'rock' and cpu == 'paper':
        return( 'you lose\n')    

    elif hereMe == 'paper' and cpu == 'rock':
        return('you won!! CPU chooses ({})\n'.format(cpu))
    elif hereMe == 'paper' and cpu == 'scissor':
        return('You lose\n')

    elif hereMe == 'scissor' and cpu == 'paper':
        return('you won!! CPU chooses ({})\n'.format(cpu))
    elif hereMe == 'scissor' and cpu =='rock':
        return('you lose\n')
    else:
        return("That is not a valid play. Check the spelling!\n")
def guiFunction():
    root = tk.Tk()

    button = tk.Button(root,text='testing tes')

    button.pack()
    root.mainloop()
if __name__ == "__main__":
    main()
