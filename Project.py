"""
File name: index.py
Description: This code will play the game rock_paper_scissor with you.\
        The user will have to provide the right input by typing Rock or Paper or scissors. \
        The computer will choose Rock or Paper or Scissor randomly and print out the result \
        whether you won or you loss.
"""
### All packages that were used.
from random import randint
### The code
def main():
    print(computerChoice())
### A function for Computer's choice
def computerChoice():
    x = randint(0,2)
    pick = ['Rock','Paper','scissor']
    return pick[x]

### User's input
def userChioce():
    pass
### output result
def result():
    pass
if __name__ == "__main__":
    main()
