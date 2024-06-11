import objects
import tkinter as tk
from tkinter import ttk

def iniciar():
    n_p = int(entry.get())
    objects.game(n_players = n_p)


def main():
    window.mainloop()

if __name__ == "__main__":
    window = tk.Tk()
    window.title("NO THANKS")
    window.geometry("800x600")
    label = ttk.Label(master = window, text = "Inserte el número de jugadores")
    label.pack()
    entry = ttk.Entry(master = window)
    entry.pack()
    button = ttk.Button(master = window, text = "Iniciar Juego", command = iniciar)
    button.pack()
    main()

