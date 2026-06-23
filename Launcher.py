import tkinter as tk
import webbrowser
from tkinter import ttk

root = tk.Tk()
root.title("GTA5 Launcher")
root.geometry("400x300")

def very_good():
    select_text = combo.get()
    return select_text

def playgame():
    selected_platform = very_good()
    if selected_platform == "Steam":
        GTA5_APPID = 271590
        steam_launch_url = f"steam://rungameid/{GTA5_APPID}"
        webbrowser.open(steam_launch_url)
        print("The game and startup might take a bit of time")
    elif selected_platform == "Rockstar Games Launcher":
        print("Stay tuned")
    elif selected_platform == "Epic":
        print("Stay tuned")
    else:
        print("Please choose a way to start first!")

combo = ttk.Combobox(
    root,
    values=["Steam", "Rockstar Games Launcher", "Epic"],
    state="readonly"
)
combo.pack(pady=30)
combo.set("Startup method")

btn = tk.Button(root, text="play!", command=playgame)
btn.pack(pady=20)

root.mainloop()