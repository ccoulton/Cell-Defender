import threading

import Tkinter as tk

class SplashScreen():

    def __init__(self, delay, image_file):

        self.delay = delay
        self.image_file = image_file

    def run(self):

        root = tk.Tk()
        # show no frame
        root.overrideredirect(True)
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry('%dx%d+%d+%d' % (width*1, height*1, width*0.00, height*0.00))
        #image_file = "../media/materials/textures/wankershimStartScreen.gif"
        image = tk.PhotoImage(file=self.image_file)
        canvas = tk.Canvas(root, height=height*1, width=width*1, bg="brown")
        #canvas.create_image(width*0.8/2, height*0.8/2, image=image)
        canvas.create_image(0, 0, image=image, anchor=tk.NW)
        canvas.pack()
        # show the splash screen for 'dealy' milliseconds, then destroy
        root.after(self.delay, root.destroy)
        root.mainloop()

