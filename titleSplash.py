import Tkinter as tk

class TitleSplashScreen(tk.Frame):

    def __init__(self, image_file):
        self.root = tk.Tk()
        tk.Frame.__init__(self, master=self.root)
        self.image_file = image_file
        self.pack(side = tk.BOTTOM)
        self.run()


    def run(self):
        # show no frame
        self.root.overrideredirect(True)
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (self.width*1, self.height*1, self.width*0.00, self.height*0.00))
        image = tk.PhotoImage(file=self.image_file)
        canvas = tk.Canvas(self.root, height=self.height*1, width=self.width*1, bg="brown")
        canvas.create_image(0, 0, image=image, anchor=tk.NW)
        canvas.pack()

        playButton = tk.Button(self, text='Play Game!', font=("Comic Sans", 32), command=self.root.destroy, width = 90, height = 2, bg = '#000fff000', highlightcolor = '#00ffff', highlightbackground = '#00ffff')
        #playButton.place(x = (width/2), y = (height/2))
        #playButton.place(x = 500, y = 500, anchor = tk.CENTER)
        playButton.pack(side = tk.TOP, fill=tk.X)
        #self.root.after(5000, self.root.destroy)
        self.root.mainloop()


class EndScreen(tk.Frame):
    def __init__(self, image_file, score):
        self.root = tk.Tk()
        tk.Frame.__init__(self, master=self.root)
        self.image_file = image_file
        self.score = score
        self.pack(side = tk.BOTTOM)
        self.run()

    def quit(self):

        self.root.destroy()

    def run(self):
        # get high score
        f = open('highScore.txt', 'r')

        HS = f.read()
        f.close()
        HS = int(HS)

        if self.score > HS:
            HS = self.score
            f = open('highScore.txt', 'w')
            f.write(str(HS))
            f.close()

        # show no frame
        self.root.overrideredirect(True)
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (width*1, height*1, width*0.00, height*0.00))

        scoreText = 'Score: ' + str(self.score)
        scoreLabel = tk.Label(self, text= scoreText, font=("Comic Sans", 60), fg = 'green', bg = 'black', width = 150)
        scoreLabel.pack(side = tk.TOP)

        scoreText2 = 'High Score: ' + str(HS)
        scoreLabel2 = tk.Label(self, text= scoreText2, font=("Comic Sans", 60), fg = 'green', bg = 'black', width = 150)
        scoreLabel2.pack(side = tk.TOP)

        quitButton = tk.Button(self, text='Exit Game', font=("Comic Sans", 52), command=self.quit, width = 150, height = 2, bg = '#000fff000', highlightcolor = '#00ffff')
        quitButton.pack(side = tk.TOP, fill=tk.Y, anchor = tk.SE)

        image = tk.PhotoImage(file=self.image_file)
        canvas = tk.Canvas(self.root, height=height*1, width=width*1, bg="brown")
        canvas.create_image(0, 0, image=image, anchor=tk.NW)
        canvas.pack()
        #self.root.after(5000, self.root.destroy)
        self.root.mainloop()






