import customtkinter as ctk
from utilities import BASE_DIR, fetchAsset

# Functional ----------------------------------------------------------------------------------------------------------

rootWidth = 800
rootHeight = 1200

def onResize(event):
    rootWidth = root.winfo_width()
    rootHeight = root.winfo_height()

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

# card frame

playerHandFrame = ctk.CTkFrame(
    master=root, 
    width=135,
    height=95, 
    corner_radius=0, 
    border_width=2, 
    border_color="#ffffff"
    )

playerHandFrame.grid_propagate(False)

playerHandFrame.place(
    relx=0.5,
    rely=0.85,
    anchor="center"
)

# cards

cardOne = ctk.CTkImage (
    light_image=fetchAsset("2_of_clubs.png", True, True), 
    dark_image=fetchAsset("2_of_clubs.png", True, True), 
    size=(50, 70)
    )
cardTwo = ctk.CTkImage (
    light_image=fetchAsset("2_of_diamonds.png", True, True), 
    dark_image=fetchAsset("2_of_diamonds.png", True, True), 
    size=(50, 70)
    )

cardOneFrame = ctk.CTkLabel(
    master=playerHandFrame, 
    width=50,
    height=85, 
    corner_radius=5, 
    fg_color="#ffffff",
    image=cardOne,
    text=""
    )
cardTwoFrame = ctk.CTkLabel(
    master=playerHandFrame, 
    width=50,
    height=85, 
    corner_radius=5, 
    fg_color="#ffffff",
    image=cardTwo,
    text=""
    )

cardOneFrame.grid(
    row=0,
    column=0,
    sticky="nsw",
    padx=(5, 2.5),
    pady=5
)
cardTwoFrame.grid(
    row=0,
    column=1,
    sticky="nse",
    padx=(2.5, 5),
    pady=5
)

root.mainloop()