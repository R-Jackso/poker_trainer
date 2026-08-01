import customtkinter as ctk
import time
from utilities import Card, Hand, fetchAsset, newDeck, BASE_DIR


# Functional ----------------------------------------------------------------------------------------------------------

rootWidth = 800
rootHeight = 1200

root = ctk.CTk()
root.geometry(f"{str(rootHeight)}x{str(rootWidth)}")
root.title("Poker Trainer")
root.configure(fg_color="#000000")

hands = []
phase = 0
heroPosition = (0.5, 0.85)

seatPositions = [
    heroPosition,
    (0.15, 0.7),
    (0.15, 0.3),
    (0.5, 0.15),
    (0.85, 0.7),
    (0.85, 0.3),
]

def deal(master):
    newDeck()
    for relx, rely in seatPositions:
        if (relx, rely) == heroPosition:
            hand = Hand(master=master, showing=True)
        else:
            hand = Hand(master=master)
        
        hand.place(relx, rely)
        hands.append(hand)

def onResize(event):
    rootWidth = root.winfo_width()
    rootHeight = root.winfo_height()

def goAgain():
    global hands, phase
    for hand in hands:
        hand.frame.destroy()
    hands.clear()

    phase = 0
    deal(root)
    dealTableCards()

def revealAll():
    for hand in hands:
        hand.reveal()

def progressHand():
    global phase

    if phase == 0:
        tableCards["flopOne"].reveal()
        tableCards["flopTwo"].reveal()
        tableCards["flopThree"].reveal()
        phase += 1
    
    elif phase == 1:
        tableCards["turn"].reveal()
        phase += 1
    
    elif phase == 2:
        tableCards["river"].reveal()
        phase += 1

def dealTableCards():
    global tableCards

    for card in tableCards.values():
        card.label.destroy()

    tableCards = {
    "flopOne" : Card(root, bg_color="#167648", showing=False),
    "flopTwo" : Card(root, bg_color="#167648", showing=False),
    "flopThree" : Card(root, bg_color="#167648", showing=False),
    "turn" : Card(root, bg_color="#167648", showing=False),
    "river" : Card(root, bg_color="#167648", showing=False)
    }

    tableCardOffsets = {
        "flopOne" : -146,
        "flopTwo" : -78,
        "flopThree" : -10,
        "turn" : 68,
        "river" : 136
    }

    for key, card in tableCards.items():
        card.place(
            relx=0.5, 
            rely=0.5, 
            anchor="center", 
            x=tableCardOffsets[key])

# UI ------------------------------------------------------------------------------------------------------------------

root.bind("<Configure>", onResize)

# background

bgImage = ctk.CTkImage (
    light_image=fetchAsset("pokerTable.jpg", card=False), 
    dark_image=fetchAsset("pokerTable.jpg", card=False), 
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

# table cards

tableCards = {}
dealTableCards()

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

# reveal button

revealButton = ctk.CTkButton(
    master=root,
    width=100,
    height=50,
    corner_radius=5,
    command=revealAll,
    text="Reveal Hands"
)

revealButton.grid(
    row=0,
    column=1,
    padx=20,
    pady=20
    )

# progress button

progressButton = ctk.CTkButton(
    master=root,
    width=100,
    height=50,
    corner_radius=5,
    command=progressHand,
    text="Progress"
)

progressButton.grid(
    row=0,
    column=2,
    padx=20,
    pady=20
    )

root.mainloop()