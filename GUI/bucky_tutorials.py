from Tkinter import *

root = Tk()

topframe = Frame(root)
topframe.pack(side = TOP)

bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

button1 = Button(topframe, text = "Click Me!", foreground = "red")
button2 = Button(topframe, text = "Click Me!", foreground = "blue")
button3 = Button(topframe, text = "Click Me!" , foreground  = "green")
button4 = Button(bottomframe, text = "Click Me!", foreground = "grey")

button1.pack(side = LEFT, fill = X)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack()




root.mainloop()