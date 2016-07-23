#simple GUI

from Tkinter import *

#create the window
root = Tk()

#modify the root window
root.title("Labeler")
root.geometry("200x100")

app = Frame(root)
app.grid()
label = Label(app, text = "This is a label!")

label.grid()

button1 = Button(app, text = "Click Me!")
button1.grid()


#kickoff the event loop
root.mainloop()