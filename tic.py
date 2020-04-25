from tkinter import *
import tkinter.messagebox
import os


def Error(msg):
    tkinter.messagebox.showwarning('Game completed',msg)

def Print(txt,msg):
    tkinter.messagebox.showinfo(txt ,msg)

def checkforwin():
    global flags,status
    if(p1['text'] == 'X' and p2['text'] == 'X' and p3['text'] =='X' or
       p1['text'] == 'X' and p4['text'] == 'X' and p7['text'] == 'X' or
       p1['text'] == 'X' and p5['text'] == 'X' and p9['text'] == 'X' or
       p2['text'] == 'X' and p5['text'] == 'X' and p8['text'] =='X' or
       p3['text'] == 'X' and p6['text'] == 'X' and p9['text'] == 'X' or
       p3['text'] == 'X' and p5['text'] == 'X' and p7['text'] == 'X' or
       p4['text'] == 'X' and p5['text'] == 'X' and p6['text'] =='X' or
       p7['text'] == 'X' and p8['text'] == 'X' and p9['text'] == 'X'):
        Print('Game completed',"X is the winner")
        status = True
        restart()
    elif(p1['text'] == 'O' and p2['text'] == 'O' and p3['text'] =='O' or
       p1['text'] == 'O' and p4['text'] == 'O' and p7['text'] == 'O' or
       p1['text'] == 'O' and p5['text'] == 'O' and p9['text'] == 'O' or
       p2['text'] == 'O' and p5['text'] == 'O' and p8['text'] =='O' or
       p3['text'] == 'O' and p6['text'] == 'O' and p9['text'] == 'O' or
       p3['text'] == 'O' and p5['text'] == 'O' and p7['text'] == 'O' or
       p4['text'] == 'O' and p5['text'] == 'O' and p6['text'] =='O' or
       p7['text'] == 'O' and p8['text'] == 'O' and p9['text'] == 'O'):
        Print('Game completed',"O is the winner")
        status = True
        restart()
    elif flags == 9:
        Error("This game is draw")
        status = True
        restart()
        


def btnclick(button,pos):
    global flags,status,player_id
    if status:
        return
    if button['text'] != '':
        return
    if player_id == 'X':
        button['text'] = 'X'
        player_id = 'O'
    else:
        button['text'] = 'O'
        player_id = 'X'
    flags  += 1
    checkforwin()

def restart():
    global flags,status,player_id
    player_id = 'X'
    startbtn['text'] = 'Start Game'
    startbtn['bg'] = 'green'
    status = True
    flags = 0
    p1['text'] = ''
    p2['text'] = ''
    p3['text'] = ''
    p4['text'] = ''
    p5['text'] = ''
    p6['text'] = ''
    p7['text'] = ''
    p8['text'] = ''
    p9['text'] = ''

    
def start():
    global status
    if status==True:
        status = False
        startbtn['text'] = 'End Game'
        startbtn['bg'] = 'red'
    else:
        restart()

if __name__ == '__main__':
        
    player_id = 'X'
    status = True
    flags = 0

    root = Tk()
    root.title('Tic Tac Toe')
    root.minsize(414,500)
    root.maxsize(414,500)
    if os.path.exists(os.path.abspath('Images/icon.png')):
        root.iconphoto(True, PhotoImage(file=os.path.abspath('Images/icon.png')))

    

    p1 = Button(font='Times 20 bold', height=4, width=8,command=lambda :btnclick(p1,0))
    p1.grid(row=0,column=0)
    p2 = Button(font='Times 20 bold', height=4, width=8,command=lambda :btnclick(p2,1))
    p2.grid(row=0,column=1)
    p3 = Button(font='Times 20 bold', height=4, width=8,command=lambda :btnclick(p3,2))
    p3.grid(row=0,column=2)
    p4 = Button(font='Times 20 bold', height=4, width=8,command=lambda :btnclick(p4,3))
    p4.grid(row=1,column=0)
    p5 = Button(font='Times 20 bold', height=4, width=8,command=lambda :btnclick(p5,4))
    p5.grid(row=1,column=1)
    p6 = Button(font='Times 20 bold', height=4, width=8,command=lambda :btnclick(p6,5))
    p6.grid(row=1,column=2)
    p7 = Button(font='Times 20 bold', height=4, width=8,command=lambda :btnclick(p7,6))
    p7.grid(row=2,column=0)
    p8 = Button( font='Times 20 bold',height=4, width=8,command=lambda :btnclick(p8,7))
    p8.grid(row=2,column=1)
    p9 = Button(font='Times 20 bold',height=4, width=8,command=lambda :btnclick(p9,8))
    p9.grid(row=2,column=2)
    startbtn = Button(text='Start Game',fg ='white',bg='green')
    startbtn.configure(command=start)
    startbtn.grid(row=4,column = 1)

    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu,tearoff=0)
    menu.add_cascade(label='File',menu=filemenu)
    filemenu.add_command(label='Exit', command = root.destroy)
    aboutmenu = Menu(menu,tearoff=0)
    menu.add_cascade(label='About',menu = aboutmenu)
    aboutmenu.add_command(label='About',command = lambda: Print('About','This Game is created by Sanjay Developer\n@SanjayDevTech'))

    root.mainloop()
