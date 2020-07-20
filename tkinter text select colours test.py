from tkinter import *

# new window and the title of the window
root = Tk()
root.title("some test for now lol")

# text thing on the top
label = Label(root, text="Hellowww")
label.pack()

# some thing you input i think idk never played the game
text = StringVar()

# text label info idk the colour settings part i think
text_entry = Entry(root, textvariable=text, bg="white", fg="blue", selectbackground="tan", selectforeground="black")
text_entry.pack()

# some other label with longer text idk never played!
label_two = Label(root, textvariable=text, wraplength=180)
label_two.pack()

# main loop lol
root.mainloop()
