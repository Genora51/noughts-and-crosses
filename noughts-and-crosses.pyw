#SETUP
from tkinter import *
wins = ["000102","101112","202122","001020","011121","021222","001122","021120"]
n = "x"
won = False
window = Tk()
window.resizable(0,0)
fr = Frame(window)
fr.pack()
w = Label(fr, text="Noughts And Crosses")
btn = []
num = 1
#important functions
def shift(seq):
    l = seq[1:]
    l.append(seq[0])
    return l
def pg():
    row_frame = Frame(fr)
    row_frame.pack(side="top")
    playag = bt(row_frame, text="Play Again")
    playag.config(command=playag.play)
    playag.pack()
def playagain():
    global fr
    global won
    global n
    global w
    global btn
    global num
    num = 1
    window.geometry("200x200")
    fr.destroy()
    won = False
    n = "x"
    fr = Frame(window)
    fr.pack()
    BoardValue = ["-","-","-","-","-","-","-","-","-"]
    w = Label(fr, text="Noughts And Crosses")
    w.pack()
    btn = []
    for i, b in enumerate(BoardValue):
        if i%3 == 0:
            row_frame = Frame(fr)
            row_frame.pack(side="top")
        btn.append(bt(row_frame, text=b, relief=GROOVE, width=4,height=2))
        btn[i].config(command=btn[i].x)
        btn[i].nam(str(i//3)+str(i%3))
        btn[i].pack(side="left")

#AI CLASS
class AI:
    def checkNear(self):
        global btn
        global wins
        for j in wins:
            n1 = (int(j[0])*3) + int(j[1])
            n2 = (int(j[2])*3) + int(j[3])
            n3 = (int(j[4])*3) + int(j[5])
            btns = [btn[n1],btn[n2],btn[n3]]
            for i in range(3):
                if (btns[0].gt() == btns[1].gt()) and (btns[2].gt() == "-") and (btns[1].gt() != "-"):
                    return btns[2].nams
                    break
                btns = shift(btns)
                
    def firstmove(self):
        global btn
        if btn[4].cget('state') == 'normal':
            return "11"
        else:
            return "00"

    def order(self):
        global btn
        for x in [1,3,5,7,0,2,6,8,4]:
                if btn[x].cget('state') == 'normal':
                    return str(x//3)+str(x%3)
    
    def diag(self):
        global btn
        ps = {
            '00': [[1,3],[2,3],[1,6]],
            '02': [[1,5],[2,5],[2,8]],
            '20': [[3,7],[3,8],[0,7]],
            '22': [[5,7],[2,7],[5,6]]
            }
        for a in ps:
            for b in ps[a]:
                if btn[b[0]].gt() == btn[b[1]].gt() and btn[b[0]].gt() == "X":
                    if btn[(int(a[0])*3) + int(a[1])].cget('state') == 'normal':
                        return a
        
    def move(self,n):
        global btn
        if n == 1:
            return self.firstmove()
        else:
            ms = []
            c = self.checkNear()
            ms.append(c)
            if n <= 3:
                d = self.diag()
                ms.append(d)
            o = self.order()
            ms.append(o)
            return next(x for x in ms if x != None)
#END AI CLASS

ai = AI() #defining game AI for 1-player game
#switch functions
def switch1():
    global ai
    global n
    global num
    global btn
    if n == "x":
        for i in btn:
            i.config(command=i.o)
        n = "o"
        try:
            mov = ai.move(num)
            num += 1
            but = (int(mov[0])*3) + int(mov[1])
            btn[but].invoke()
        except:
            None
    else:
        for i in btn:
            i.config(command=i.x)
        n = "x"
def switch2():
    global n
    if n == "x":
        for i in btn:
            i.config(command=i.o)
        n = "o"
    else:
        for i in btn:
            i.config(command=i.x)
        n = "x"
switch = switch2
#more functions
def checkEqual(iterator):
    try:
        return all('disabled' == rest.cget('state') for rest in iterator)
    except StopIteration:
        return True
def chw():
    global btn
    global won
    global w
    for j in wins:
        n1 = (int(j[0])*3) + int(j[1])
        n2 = (int(j[2])*3) + int(j[3])
        n3 = (int(j[4])*3) + int(j[5])
        btns = [btn[n1],btn[n2],btn[n3]]
        if (btns[0].gt() == btns[1].gt()) and (btns[2].gt() == btns[1].gt()) and (btns[0].gt() != "-") and won == False:
            for a in btns:
                a.config(bg="red", disabledforeground="white")
            win = "Noughts and Crosses - %s wins!" %(btns[0].gt())
            won = True
            w.config(text=win)
            for x in btn:
                x.config(state="disabled")
            pg()
    if checkEqual(btn) and not(won):
        w.config(text="Noughts and Crosses - It's a draw!")
        pg()
#modified button class
class bt(Button):
    def p1(self):
        global switch
        switch = switch1
        playagain()
    def p2(self):
        global switch
        switch = switch2
        playagain()
    def play(self):
        playagain()
    def gt(self):
        return self.cget('text')
    def nam(self,nam):
        self.nams = nam
    def x(self):
        self.config(text="X",state="disabled")
        chw()
        switch()
    def o(self):
        self.config(text="O",state="disabled")
        switch()
        chw()
#setup window
BoardValue = ["-","-","-","-","-","-","-","-","-"]
window.title("Noughts And Crosses")
window.geometry("200x100")
w.pack()
#setup gamemode choice
play1 = bt(fr,text="1-player")
play2 = bt(fr,text="2-player")
play1.config(command=play1.p1)
play2.config(command=play1.p2)
play1.pack(fill=X)
play2.pack(fill=X)
window.mainloop()
