"""
File name: project.py
Auther: AbdulRazaq 
ID: 4020018
Coded by: VSCode
Description: This code will play with you the well known game rock_paper_scissor.\
        The user will have to provide the right input by pressing the images that indicates Rock or Paper or scissors. \
        The computer will choose Rock or Paper or Scissor randomly and print out the result \
        whether you won or you loss. \
        This project was requested University of Prince Muqrin. 
"""
### All packages that were used.
from random import randint
import tkinter as tk
from PIL import Image,ImageTk
### The code that needs to be run.
def main():
    ### start the function to run everything.
    guiFunction()

### A function for Computer's choice.
def computerChoice():
    x =   randint(0,2)
    pick = ['rock','paper','scissor']
    return pick[x]

### Processing code.
def process(hereMe,cpu):
    if hereMe == cpu:
        return('tie!'.title())
    elif hereMe == 'rock' and cpu == 'scissor':
        return('You win!!  {} SMASHES {}'.format(hereMe,cpu))
    elif hereMe == 'rock' and cpu == 'paper':
        return( 'You lose...  {} COVERS {}'.format(cpu,hereMe))    

    elif hereMe == 'paper' and cpu == 'rock':
        return('You win!!  {} COVERS {}'.format(hereMe,cpu))
    elif hereMe == 'paper' and cpu == 'scissor':
        return('You lose...  {} CUT {}'.format(cpu,hereMe))

    elif hereMe == 'scissor' and cpu == 'paper':
        return('You win!!  {} CUT {}'.format(hereMe,cpu))
    elif hereMe == 'scissor' and cpu =='rock':
        return('You lose...  {} SMASHES {}\n'.format(cpu,hereMe))
    else:
        return("That is not a valid play. Check the spelling!\n")

### Graphical User Interface
def guiFunction():
    root = tk.Tk() # call the function Tkinter.
    root.title('Rock Paper scissor Game.') # Title of the window.
    root.resizable(False,False) # To make the window unresizable.
    # Sreate a background with given height and width.
    canvas = tk.Canvas(root, height=455, width=710,bd=-2)
    canvas.pack()
    
    idea = tk.Frame(root,bg='#48C3F9',bd=4)
    idea.place(relx=.1,rely=.1,relwidth=.8,relheight=.8)
    # Set a backround image.
    backgroung_img = ImageTk.PhotoImage(Image.open("Images/2560_1440.png"))
    canvas.create_image(20,20,anchor='center',image=backgroung_img)
    # Set a frame inside the image.
    frame = tk.Frame(root, bg='#003F5A',bd=4)
    frame.place(relx=0.1,rely=.75, relwidth=.8, relheight=.15)
    
    frame2 = tk.Frame(frame,bg='white',bd=4)
    frame2.place(relwidth=1,relheight=1)
    # Set a buttons frame.
    buttonFrame = tk.Frame(frame2,bg='#48C3F9')
    buttonFrame.place(relwidth=1,relheight=1)
    # Create three separate bottoms with images on each, \
    # the user will have to press to confirm hes choice.
    rockImg = ImageTk.PhotoImage(file='images/rock.jpg')
    rockButton = tk.Button(buttonFrame, image=rockImg,bg='white',bd=-2,command=lambda:userChioce('rock'))
    rockButton.place(relx=0.15,rely=0.10,relwidth=.12,relheight=.8)

    paperImg = ImageTk.PhotoImage(file='images/paper.jpg')
    paperButton = tk.Button(buttonFrame, image=paperImg,bd=-2,bg='white',command=lambda:userChioce('paper'))
    paperButton.place(relx=.44,rely=0.10,relwidth=.12,relheight=.8)

    scissorImg = ImageTk.PhotoImage(file='images/scissor.jpg')
    scissorButton = tk.Button(buttonFrame, relief="flat",image=scissorImg,bg='white', bd=-1,command=lambda:userChioce('scissor'))
    scissorButton.place(relx=.73,rely=0.10,relwidth=.12,relheight=.8)
    # set a result screen 
    labelFrame = tk.LabelFrame(root, relief='ridge',bg='#003F5A',fg='white',bd=4,font='Helvetica 8 bold',text='Welcome to my game!')
    labelFrame.place(relx=.1,rely=.1,relwidth=.8,relheight=.65)
    # ask the user to pick from each button
    askL = tk.Label(labelFrame, bg='#003F5A',bd=-2,fg='white',font='Helvetica 12 bold',text='Choose: \nRock\t    \t   Paper \t\t      Scissor')
    askL.pack(side='bottom')
    
### User's pick.
    def userChioce(kk):
        CPU = computerChoice() # call the computerChoice function and assign it for one result only.
        # Hide the buttons after choosing one image.
        rockButton.place_forget()
        paperButton.place_forget()
        scissorButton.place_forget()
        # Hide the Ask label(the one that asks you to choose).
        askL.pack_forget()
        # set a text on top of the frame
        labelFrame['text'] = 'Processing....'.upper()
        # To show what you've picked.
        chos = tk.Label(labelFrame,bg='#003F5A',font='Helvetica 12 bold',fg='white',text='You Choose:')
        chos.place(relx=0.15,rely=.23,relheight=.2,relwidth=.2)
        if kk == 'rock':
            userLabel= tk.Label(labelFrame, bg='grey',fg='white',font='Helvetica 16 bold',text=kk.capitalize(), relief='groove')
            userLabel.place(relx=0.15,rely=.48,relheight=.2,relwidth=.2)
        elif kk == 'paper':
            userLabel= tk.Label(labelFrame, bg='grey',fg='white',font='Helvetica 16 bold',text=kk.capitalize(), relief='groove')
            userLabel.place(relx=0.15,rely=.48,relheight=.2,relwidth=.2)
        elif kk == 'scissor':
            userLabel= tk.Label(labelFrame, bg='grey',fg='white',font='Helvetica 16 bold',text=kk.capitalize(), relief='groove')
            userLabel.place(relx=0.15,rely=.48,relheight=.2,relwidth=.2)
        
        # Show the play button right after you pick.
        playBtn = tk.Button(labelFrame,text='Play',command=lambda:commandBtn(),bg='#48C3F9')
        playBtn.place(relx=.5,rely=.95,relwidth=.1,relheight=0.1,anchor='s')
        # This will create a button call Reset and calls the resetDel function
        resetBtn = tk.Button(buttonFrame,text='Reset All',command=lambda:resetDel(),state='disable')
        resetBtn.place(relx=0.44,rely=0.10,relwidth=.12,relheight=.8)

        # When the play button is pressed this function will run.
        def commandBtn():
            global resultLabel, chos2, comLabel
            playBtn.destroy()
            chos2 = tk.Label(labelFrame,bg='#003F5A',font='Helvetica 12 bold',fg='white',text='CPU\'s Choice:')
            chos2.place(relx=0.65,rely=.23,relheight=.2,relwidth=.2)

            comLabel = tk.Label(labelFrame, bg='grey',fg='white',font='Helvetica 16 bold',text=CPU.capitalize(),relief='groove')
            comLabel.place(relx=0.65,rely=.48,relheight=.2,relwidth=.2)
            
            # This will disply the results by calling the process function and provide to argument.
            resultLabel = tk.Label(labelFrame, bg='#003F5A',fg='white',text=process(kk,CPU),font='Helvetica 18 bold')
            resultLabel.place(anchor='n',relx=0.5,rely=0.05)
            # When pressing play button, reset button will become active.
            resetBtn['state'] = 'normal'
            
        
        # This was purposely for resetting every thing; and start form the biginning.
        def resetDel():
            labelFrame['text'] = 'Wanna Play Again?'
            askL.pack(side='bottom')
            resultLabel.destroy()
            resetBtn.place_forget()
            userLabel.destroy()
            chos.destroy()
            chos2.destroy()
            comLabel.destroy()
            rockButton.place(relx=0.15,rely=0.10,relwidth=.12,relheight=.8)
            paperButton.place(relx=.44,rely=0.10,relwidth=.12,relheight=.8)
            scissorButton.place(relx=.73,rely=0.10,relwidth=.12,relheight=.8)

    # Time disply label (not complated)
    #labeltime = tk.Label(root, bg='grey',fg='red',font=10)
    #labeltime.pack(side='bottom',fill='x')
    
    root.mainloop()

    
if __name__ == "__main__":
    main()
