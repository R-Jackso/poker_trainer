import customtkinter as ctk
from utilities import BASE_DIR, fetchAsset, Hand

# Functional ----------------------------------------------------------------------------------------------------------

rootWidth = 800
rootHeight = 1200
hands = []

def deal(master):
    hands.append(Hand(master=master, relx=0.5, rely=0.85))
    hands.append(Hand(master=master, relx=0.15, rely=0.7))
    hands.append(Hand(master=master, relx=0.15, rely=0.3))
    hands.append(Hand(master=master, relx=0.5, rely=0.15))
    hands.append(Hand(master=master, relx=0.85, rely=0.7))
    hands.append(Hand(master=master, relx=0.85, rely=0.3))

def onResize(event):
    rootWidth = root.winfo_width()
    rootHeight = root.winfo_height()

def goAgain():
    global hands
    for hand in hands:
        hand.frame.destroy()
    hands.clear()
    
    deal(root)

# UI ------------------------------------------------------------------------------------------------------------------

# root

root = ctk.CTk()
root.geometry(f"{str(rootHeight)}x{str(rootWidth)}")
root.title("Poker Trainer")
root.configure(fg_color="#000000")

root.bind("<Configure>", onResize)

# background

bgImage = ctk.CTkImage (
    light_image=fetchAsset("pokerTable.jpg", True), 
    dark_image=fetchAsset("pokerTable.jpg", True), 
    size=(1200, 675)
    )

bg_label = ctk.CTkLabel(
    master=root, 
    image=bgImage, 
    text=""
    )
bg_label.place(
    x=0, 
    y=0, 
    relwidth=1, 
    relheight=1
    )

# hands (initial creation)
deal(root)

# go again button
goAgainButton = ctk.CTkButton(
    master=root,
    width=100,
    height=50,
    corner_radius=5,
    command=goAgain,
    text="Go Again"
)

goAgainButton.grid(
    row=0, 
    column=0,
    padx=20,
    pady=20
    )

root.mainloop()