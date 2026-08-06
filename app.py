import customtkinter as ctk
import time
from utilities import Card, Player, fetchAsset, newDeck, BASE_DIR


# Functional ----------------------------------------------------------------------------------------------------------

rootWidth = 800
rootHeight = 1200

root = ctk.CTk()
root.geometry(f"{str(rootHeight)}x{str(rootWidth)}")
root.title("Poker Trainer")
root.configure(fg_color="#000000")

phase = 0

def deal(master):
    newDeck()
    for player in players.values():
        player.dealHand(master)

def onResize(event):
    rootWidth = root.winfo_width()
    rootHeight = root.winfo_height()

def goAgain():
    global phase
    phase = 0
    deal(root)
    dealTableCards()

def revealAll():
    for player in players.values():
        player.reveal()

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
    "burnOne"   : Card(root, bg_color="#167648", showing=False),
    "flopOne"   : Card(root, bg_color="#167648", showing=False),
    "flopTwo"   : Card(root, bg_color="#167648", showing=False),
    "flopThree" : Card(root, bg_color="#167648", showing=False),
    "burnTwo"   : Card(root, bg_color="#167648", showing=False),
    "turn"      : Card(root, bg_color="#167648", showing=False),
    "burnThree" : Card(root, bg_color="#167648", showing=False),
    "river"     : Card(root, bg_color="#167648", showing=False)
    }

    tableCardOffsets = {
        "flopOne" : -146,
        "flopTwo" : -78,
        "flopThree" : -10,
        "turn" : 68,
        "river" : 136
    }

    for key, card in tableCards.items():
        if "burn" in key:
            pass
        else:
            card.place(
                relx=0.5, 
                rely=0.5, 
                anchor="center", 
                x=tableCardOffsets[key])

def game():
    global tableCards
    while True:

        # pre-flop

        deal(root)

        tableCards = {}
        dealTableCards()

        break

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

# players

players = {
    "player1": Player(root, "player1", seat=(0.5, 0.85), position=1, isHero=True),
    "player2": Player(root, "player2", seat=(0.15, 0.7), position=2),
    "player3": Player(root, "player3", seat=(0.15, 0.3), position=3),
    "player4": Player(root, "player4", seat=(0.5, 0.15), position=4),
    "player5": Player(root, "player5", seat=(0.85, 0.7), position=5),
    "player6": Player(root, "player6", seat=(0.85, 0.3), position=6),
}

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

game()

root.mainloop()