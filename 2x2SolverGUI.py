import solver
import tkinter as tk


class GUI:
    def __init__(self):
        self.solve = solver.Solver()
        self.shuffled = self.solve.shuffled
        self.solve.find_solution()
        self.route = self.solve.route
        self.route.pop(0)
        self.totalMoves = len(self.route)
        self.movesLeft = str(len(self.route))
        self.moveCount = None
        self.root = None
        self.colors = {'w': 'white', 'b': 'blue', 'o': 'orange', 'g': 'green', 'r': 'red', 'y': 'yellow'}
        self.count = 0
        self.points = {0: 'white', 1: 'white', 2: 'white', 3: 'white', 4: 'red', 5: 'red', 6: 'red', 7: 'red',
                       8: 'green', 9: 'green', 10: 'green', 11: 'green', 12: 'orange', 13: 'orange', 14: 'orange',
                       15: 'orange', 16: 'blue', 17: 'blue', 18: 'blue', 19: 'blue', 20: 'yellow', 21: 'yellow',
                       22: 'yellow', 23: 'yellow'}
        self.shuffle()
        self.display()
        # ######################################3

    def display(self):

        root = tk.Tk()
        canvas = tk.Canvas(root, height=1000, width=1000)
        canvas.pack()
        back = tk.Frame(root, bg='#4d5b70')
        back.place(relheight=1, relwidth=1)

        frame = tk.Frame(back)
        frame.place(relx=.025, rely=.025, relheight=.95, relwidth=.95)

        Next = tk.Button(frame, text="Next Step to Solution", bg='#4d5b70', fg='white', font=40,
                         command=lambda: self.next())
        Next.place(relx=.1, rely=.025, relwidth=.8, relheight=.15)

        blueCubeFrame = tk.Frame(frame, bg='blue', highlightbackground="black", highlightthickness=3)
        blueCubeFrame.place(relx=.1, rely=.4, relheight=.2, relwidth=.2)

        _16 = tk.Frame(blueCubeFrame, bg=self.points[16], highlightbackground="black", highlightthickness=2)
        _16.place(relx=0, rely=0, relheight=.5, relwidth=.5)
        _17 = tk.Frame(blueCubeFrame, bg=self.points[17], highlightbackground="black", highlightthickness=2)
        _17.place(relx=.5, rely=0, relheight=.5, relwidth=.5)
        _18 = tk.Frame(blueCubeFrame, bg=self.points[18], highlightbackground="black", highlightthickness=2)
        _18.place(relx=.5, rely=.5, relheight=.5, relwidth=.5)
        _19 = tk.Frame(blueCubeFrame, bg=self.points[19], highlightbackground="black", highlightthickness=2)
        _19.place(relx=0, rely=0.5, relheight=.5, relwidth=.5)

        whiteCubeFrame = tk.Frame(frame, bg='white', highlightbackground="black", highlightthickness=3)
        whiteCubeFrame.place(relx=.3, rely=.4, relheight=.2, relwidth=.2)

        _0 = tk.Frame(whiteCubeFrame, bg=self.points[0], highlightbackground="black", highlightthickness=2)
        _0.place(relx=0, rely=0, relheight=.5, relwidth=.5)
        _1 = tk.Frame(whiteCubeFrame, bg=self.points[1], highlightbackground="black", highlightthickness=2)
        _1.place(relx=0.5, rely=0, relheight=.5, relwidth=.5)
        _2 = tk.Frame(whiteCubeFrame, bg=self.points[2], highlightbackground="black", highlightthickness=2)
        _2.place(relx=0.5, rely=0.5, relheight=.5, relwidth=.5)
        _3 = tk.Frame(whiteCubeFrame, bg=self.points[3], highlightbackground="black", highlightthickness=2)
        _3.place(relx=0, rely=0.5, relheight=.5, relwidth=.5)

        greenCubeFrame = tk.Frame(frame, bg='green', highlightbackground="black", highlightthickness=3)
        greenCubeFrame.place(relx=.5, rely=.4, relheight=.2, relwidth=.2)

        _8 = tk.Frame(greenCubeFrame, bg=self.points[8], highlightbackground="black", highlightthickness=2)
        _8.place(relx=0, rely=0, relheight=.5, relwidth=.5)
        _9 = tk.Frame(greenCubeFrame, bg=self.points[9], highlightbackground="black", highlightthickness=2)
        _9.place(relx=0.5, rely=0, relheight=.5, relwidth=.5)
        _10 = tk.Frame(greenCubeFrame, bg=self.points[10], highlightbackground="black", highlightthickness=2)
        _10.place(relx=0.5, rely=0.5, relheight=.5, relwidth=.5)
        _11 = tk.Frame(greenCubeFrame, bg=self.points[11], highlightbackground="black", highlightthickness=2)
        _11.place(relx=0, rely=0.5, relheight=.5, relwidth=.5)

        yellowCubeFrame = tk.Frame(frame, bg='yellow', highlightbackground="black", highlightthickness=3)
        yellowCubeFrame.place(relx=.7, rely=.4, relheight=.2, relwidth=.2)

        _20 = tk.Frame(yellowCubeFrame, bg=self.points[20], highlightbackground="black", highlightthickness=2)
        _20.place(relx=0, rely=0, relheight=.5, relwidth=.5)
        _21 = tk.Frame(yellowCubeFrame, bg=self.points[21], highlightbackground="black", highlightthickness=2)
        _21.place(relx=0.5, rely=0, relheight=.5, relwidth=.5)
        _22 = tk.Frame(yellowCubeFrame, bg=self.points[22], highlightbackground="black", highlightthickness=2)
        _22.place(relx=0.5, rely=0.5, relheight=.5, relwidth=.5)
        _23 = tk.Frame(yellowCubeFrame, bg=self.points[23], highlightbackground="black", highlightthickness=2)
        _23.place(relx=0, rely=0.5, relheight=.5, relwidth=.5)

        redCubeFrame = tk.Frame(frame, bg='red', highlightbackground="black", highlightthickness=3)
        redCubeFrame.place(relx=.3, rely=.2, relheight=.2, relwidth=.2)

        _4 = tk.Frame(redCubeFrame, bg=self.points[4], highlightbackground="black", highlightthickness=2)
        _4.place(relx=0, rely=0, relheight=.5, relwidth=.5)
        _5 = tk.Frame(redCubeFrame, bg=self.points[5], highlightbackground="black", highlightthickness=2)
        _5.place(relx=0.5, rely=0, relheight=.5, relwidth=.5)
        _6 = tk.Frame(redCubeFrame, bg=self.points[6], highlightbackground="black", highlightthickness=2)
        _6.place(relx=0.5, rely=0.5, relheight=.5, relwidth=.5)
        _7 = tk.Frame(redCubeFrame, bg=self.points[7], highlightbackground="black", highlightthickness=2)
        _7.place(relx=0, rely=0.5, relheight=.5, relwidth=.5)

        orangeCubeFrame = tk.Frame(frame, bg='orange', highlightbackground="black", highlightthickness=3)
        orangeCubeFrame.place(relx=.3, rely=.6, relheight=.2, relwidth=.2)

        _12 = tk.Frame(orangeCubeFrame, bg=self.points[12], highlightbackground="black", highlightthickness=2)
        _12.place(relx=0, rely=0, relheight=.5, relwidth=.5)
        _13 = tk.Frame(orangeCubeFrame, bg=self.points[13], highlightbackground="black", highlightthickness=2)
        _13.place(relx=0.5, rely=0, relheight=.5, relwidth=.5)
        _14 = tk.Frame(orangeCubeFrame, bg=self.points[14], highlightbackground="black", highlightthickness=2)
        _14.place(relx=0.5, rely=0.5, relheight=.5, relwidth=.5)
        _15 = tk.Frame(orangeCubeFrame, bg=self.points[15], highlightbackground="black", highlightthickness=2)
        _15.place(relx=0, rely=0.5, relheight=.5, relwidth=.5)

        self.moveCount = tk.Label(frame, font=50, text=('Moves Left: ' + str(self.movesLeft)))
        self.moveCount.place(relheight=.1, rely=.9, relx=.5)
        root.mainloop()

    def shuffle(self):
        for i in range(24):
            self.points[i] = self.colors[self.shuffled[i][0]]

    def next(self):
        if self.count < self.totalMoves:
            move = self.conversion(self.route[self.count])
            for i in range(24):
                self.points[i] = self.colors[move[i][0]]
            self.count += 1
            self.movesLeft = self.totalMoves - self.count
            #self.moveCount['text'] = str(self.movesLeft)
            self.display()

    def conversion(self, current):
        individual = []
        for i in range(len(current)):
            if i % 3 == 2:
                individual.append(current[i-2] + current[i-1] + current[i])
        return individual


if __name__ == '__main__':
    gui = GUI()
    gui.shuffle()


