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
    root.title('Rock Paper scissor Game.')
    root.resizable(False,False)
    
    canvas = tk.Canvas(root, height=455, width=710,bd=-2)
    canvas.pack()
    
    idea = tk.Frame(root,bg='#48C3F9',bd=4)
    idea.place(relx=.1,rely=.1,relwidth=.8,relheight=.8)

    backgroung_img = ImageTk.PhotoImage(Image.open("Images/2560_1440.png"))
    canvas.create_image(20,20,anchor='center',image=backgroung_img)
    
    frame = tk.Frame(root, bg='black',bd=4)
    frame.place(relx=0.1,rely=.75, relwidth=.8, relheight=.15)

    frame2 = tk.Frame(frame,bg='white',bd=4)
    frame2.place(relwidth=1,relheight=1)

    buttonFrame = tk.Frame(frame2,bg='#48C3F9')
    buttonFrame.place(relwidth=1,relheight=1)

    button = tk.Button(buttonFrame, text='testing 1'.upper(),bg='yellow')
    button.place(relx=0.04,rely=0.25,relwidth=.2,relheight=.5)

    button2 = tk.Button(buttonFrame, text='testing 2'.upper(),bg='yellow')
    button2.place(relx=0.40,rely=0.25,relwidth=.2,relheight=.5)

    button3 = tk.Button(buttonFrame, text='testing 3'.upper(),bg='yellow')
    button3.place(relx=.76,rely=0.25,relwidth=.2,relheight=.5)

    labelFrame = tk.LabelFrame(root,bg='black',fg='white',bd=2,text='Hello World')
    labelFrame.place(relx=.1,rely=.1,relwidth=.8,relheight=.6)

    label = tk.Label(labelFrame, bg='red',fg='red',font=10)
    label.pack(side='top')
    
    labeltime = tk.Label(root, bg='grey',fg='red',font=10)
    labeltime.pack(side='top',fill='x')
    
    root.mainloop()

    
if __name__ == "__main__":
    main()
