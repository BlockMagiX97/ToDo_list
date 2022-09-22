from tkinter import *

def close(frame):
    frame.pack_forget()
    frame.destroy()

def new(root, entry):
    newFrame = Frame(root)
    newText = Label(newFrame, text=entry.get())
    closeButton = Button(newFrame, text="x", command=lambda: close(newFrame))
    newFrame.grid(rowspan=2)
    newText.grid(column=0)
    closeButton.grid(column=1, row=0)
    entry.delete(0, 'end')

root = Tk()

a = Entry()
a.grid(column=0)
a.insert(0, "Add new note")

b = Button(text="save", command=lambda: new(root, a))
b.grid(column=1, row=0)

root.mainloop()