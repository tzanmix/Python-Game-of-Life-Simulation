#Τζανάτος Μιχαήλ
#up1066574

from tkinter import *

class Game_of_Life():
    
    def __init__(self,root):
        root.title("Game of Life")
        self.frame1=Frame(root)
        self.frame1.grid(row=0,column=0)
        self.btn=[[0 for x in range(40)] for x in range(30)]
        self.mylist=[[0 for i in range(40)] for j in range(30)]
        self.cell_status=[["nekro" for i in range(40)] for j in range(30)]
        for x in range(30):
            for y in range(40):
                self.btn[x][y] = Button(self.frame1,width=3, command= lambda x1=x,y1=y: self.color_change(x1,y1),background="blue")    #μπλε κύτταρο=νεκρό/κόκκινο=ζωντανό
                self.btn[x][y].grid(row=x,column=y)        
        self.frame2=Frame(root)
        self.frame2.grid(row=31,column=0)
        self.frame3=Frame(root)
        self.frame3.grid(row=32,column=0)
        self.startbutton=Button(self.frame2, command= self.game_start, text="ΕΠΟΜΕΝΟ", font= "Arial 20", background="lime").grid(row=31,column=20)
        self.clearbutton=Button(self.frame3, command= self.clear, text="ΚΑΘΑΡΙΣΜΟΣ", font="Arial 20", background="red").grid(row=32,column=20)

        
    def color_change(self,x,y):
        self.btn[x][y].config(bg="red")
        self.mylist[x][y]=1
        self.cell_status[x][y]="zwntano"

        
    def game_start(self):
        #οι κανονισμοί του παιχνιδιού:
        #κάθε κύτταρο με λιγότερους από δύο γείτονες πεθαίνει
        #κάθε κύτταρο με 4 ή παραπάνω γείτονες πεθαίνει
        #κάθε κύτταρο με 2 ή 3 γείτονες επιβιώνει
        #κάθε νεκρό κύτταρο με 3 γείτονες ζωντανεύει
        for i in range(30):
            for j in range(40):
                if count_neighbours(i,j)==3 and self.mylist[i][j]==0:          #νεκρό κύτταρο με 3 ζωντανούς γείτονες=> ζωντανό
                    self.mylist[i][j]=1
                elif count_neighbours(i,j)>3 and self.mylist[i][j]==1:         #4 ή παραπάνω γείτονες=θάνατος
                    self.mylist[i][j]=0
                elif count_neighbours(i,j)<2 and self.mylist[i][j]==1:      #λιγότεροι από 2 γείτονες=θάνατος
                    self.mylist[i][j]=0
                elif (count_neighbours(i,j)==2 or count_neighbours(i,j)==3) and self.mylist[i][j]==1:    #2 ή 3 γείτονες=>επιβίωση
                    pass
        self.next_phase()
        

    def next_phase(self):
        for i in range(30):
            for j in range(40):
                if self.mylist[i][j]==1:
                    self.btn[i][j].config(bg="red")
                else:
                    self.btn[i][j].config(bg="blue")
        for i in range(30):
            for j in range(40):
                if self.mylist[i][j]==1:
                    self.cell_status[i][j]="zwntano"
                else:
                    self.cell_status[i][j]="nekro"


    def clear(self):
        for i in range(30):
            for j in range(40):
                self.btn[i][j].config(bg="blue")
                self.mylist[i][j]=0
                self.cell_status[i][j]="nekro"


                
                
#Η συνάρτηση για την καταμέτρηση των γειτόνων
def count_neighbours(x,y):
    s=0
    for j in range(-1,2):
        try:
            if game.cell_status[x-1][y+j]=="zwntano":
                s=s+1
        except IndexError: pass
    for j in range(-1,2):
        try:
            if game.cell_status[x+1][y+j]=="zwntano":
                s=s+1
        except IndexError: pass
    try:
        if game.cell_status[x][y-1]=="zwntano":
            s=s+1
    except IndexError: pass
    try:
        if game.cell_status[x][y+1]=="zwntano":
            s=s+1
    except IndexError: pass
    return s


#main
root=Tk()
game=Game_of_Life(root)
root.mainloop()
