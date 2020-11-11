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
from PIL import Image,ImageTk
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
        return( 'you lose... CPU chooses ({})\n'.format(cpu))    

    elif hereMe == 'paper' and cpu == 'rock':
        return('you won!! CPU chooses ({})\n'.format(cpu))
    elif hereMe == 'paper' and cpu == 'scissor':
        return('You lose... CPU chooses ({})\n'.format(cpu))

    elif hereMe == 'scissor' and cpu == 'paper':
        return('you won!! CPU chooses ({})\n'.format(cpu))
    elif hereMe == 'scissor' and cpu =='rock':
        return('you lose... CPU chooses ({})\n'.format(cpu))
    else:
        return("That is not a valid play. Check the spelling!\n")
### Graphical User Interface
def guiFunction():
    root = tk.Tk()

    canvas = tk.Canvas(root, height=455, width=710)
    canvas.pack()
    
    backgroung_img = ImageTk.PhotoImage(Image.open("2560_1440.png"))
    canvas.create_image(20,20,anchor='center',image=backgroung_img)
    
    frame = tk.Frame(root, bg='black',bd=4)
    frame.place(relx=0.1,rely=.75, relwidth=.8, relheight=.15)

    frame2 = tk.Frame(frame,bg='white',bd=4)
    frame2.place(relwidth=1,relheight=1)

    frame3 = tk.Frame(frame2,bg='#48C3F9')
    frame3.place(relwidth=1,relheight=1)

    button = tk.Button(frame3, text='testing 1'.upper(),bg='yellow')
    button.place(relx=0.04,rely=0.25,relwidth=.2,relheight=.5)

    button2 = tk.Button(frame3, text='testing 2'.upper(),bg='yellow')
    button2.place(relx=0.40,rely=0.25,relwidth=.2,relheight=.5)

    button3 = tk.Button(frame3, text='testing 3'.upper(),bg='yellow')
    button3.place(relx=.76,rely=0.25,relwidth=.2,relheight=.5)

    #entry = tk.Entry(frame, fg='red',font=10)
    #entry.pack(side='TOP')

    root.mainloop()

    
if __name__ == "__main__":
    main()
