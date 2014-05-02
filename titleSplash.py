import Tkinter as tk

class TitleSplashScreen(tk.Frame, ):

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

        playButton = tk.Button(self, text='Play Game!', command=self.root.destroy, width = 60, height = 7, bg = '#000fff000', highlightcolor = '#00ffff', highlightbackground = '#00ffff')
        #playButton.place(x = (width/2), y = (height/2))
        #playButton.place(x = 500, y = 500, anchor = tk.CENTER)
        playButton.pack(side = tk.TOP)
        #self.root.after(5000, self.root.destroy)
        self.root.mainloop()


class EndScreen(TitleSplashScreen):
    def __init__(self, image_file, keepPlaying):
        TitleSplashScreen.__init__(self, image_file)
        self.keepPlaying = keepPlaying

    def quit(self):
        self.keepPlaying = False
        self.root.destroy()

    def run(self):
        # show no frame
        self.root.overrideredirect(True)
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (width*1, height*1, width*0.00, height*0.00))
        image = tk.PhotoImage(file=self.image_file)
        canvas = tk.Canvas(self.root, height=height*1, width=width*1, bg="brown")
        canvas.create_image(0, 0, image=image, anchor=tk.NW)
        canvas.pack()
        quitButton = tk.Button(self, text='Exit Game', command=self.quit, width = 60, height = 7, bg = '#000fff000', highlightcolor = '#00ffff')
        quitButton.pack(side = tk.TOP)
        #self.root.after(5000, self.root.destroy)
        self.root.mainloop()






