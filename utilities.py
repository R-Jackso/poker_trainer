import customtkinter as ctk
import sys
import random
from pathlib import Path
from PIL import Image


if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys._MEIPASS) / "synapse"
else:
    BASE_DIR = Path(__file__).parent

cardBank = [
    "ace_of_clubs", "2_of_clubs", "3_of_clubs", "4_of_clubs", "5_of_clubs",
    "6_of_clubs", "7_of_clubs", "8_of_clubs", "9_of_clubs", "10_of_clubs",
    "jack_of_clubs", "queen_of_clubs", "king_of_clubs",
    "ace_of_diamonds", "2_of_diamonds", "3_of_diamonds", "4_of_diamonds", "5_of_diamonds",
    "6_of_diamonds", "7_of_diamonds", "8_of_diamonds", "9_of_diamonds", "10_of_diamonds",
    "jack_of_diamonds", "queen_of_diamonds", "king_of_diamonds",
    "ace_of_hearts", "2_of_hearts", "3_of_hearts", "4_of_hearts", "5_of_hearts",
    "6_of_hearts", "7_of_hearts", "8_of_hearts", "9_of_hearts", "10_of_hearts",
    "jack_of_hearts", "queen_of_hearts", "king_of_hearts",
    "ace_of_spades", "2_of_spades", "3_of_spades", "4_of_spades", "5_of_spades",
    "6_of_spades", "7_of_spades", "8_of_spades", "9_of_spades", "10_of_spades",
    "jack_of_spades", "queen_of_spades", "king_of_spades",
]

class Hand:
    def __init__(self, master, relx, rely):
        self.frame = ctk.CTkFrame(
            master=master,
            width=135,
            height=95,
            corner_radius=0,
            border_width=2,
            border_color="#ffffff"
        )

        self.frame.grid_propagate(False)
        self.frame.place(relx=relx, rely=rely, anchor="center")

        cardOne = ctk.CTkImage (
            light_image=draw(), 
            dark_image=draw(), 
            size=(50, 70)
            )
        cardTwo = ctk.CTkImage (
            light_image=draw(), 
            dark_image=draw(), 
            size=(50, 70)
            )
        
        cardOneLabel = ctk.CTkLabel(
            master=self.frame, 
            width=50,
            height=85, 
            corner_radius=5, 
            fg_color="#ffffff",
            image=cardOne,
            text=""
            )
        cardTwoLabel = ctk.CTkLabel(
            master=self.frame, 
            width=50,
            height=85, 
            corner_radius=5, 
            fg_color="#ffffff",
            image=cardTwo,
            text=""
            )

        cardOneLabel.grid(
            row=0,
            column=0,
            sticky="nsw",
            padx=(5, 2.5),
            pady=5
        )
        cardTwoLabel.grid(
            row=0,
            column=1,
            sticky="nse",
            padx=(2.5, 5),
            pady=5
        )
        
def draw():
    selectedCard = random.choice(cardBank)
    fetchAsset(selectedCard, True, True)

def fetchAsset(assetPath, open=False, card=False):
    if card:
        fullPath = Path(BASE_DIR / "assets" / "cards" / assetPath)
    else:
        fullPath = Path(BASE_DIR / "assets" / assetPath)

    if open:
        return Image.open(fullPath)
    else:
        return Path(fullPath)