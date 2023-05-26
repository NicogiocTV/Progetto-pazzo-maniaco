import tkinter as tk
from PIL import Image, ImageTk, ImageSequence, GifImagePlugin
import io

#x = "goku-fortnite.gif"
def gif(x):
    # crea una finestra
    window = tk.Tk()
    # carica la GIF
    with open(x, 'rb') as f:
        gif = Image.open(io.BytesIO(f.read()))
    # converti la GIF in un formato leggibile da tkinter
    frames = []
    for frame in ImageSequence.Iterator(gif):
        frame = frame.convert('RGBA')
        frames.append(ImageTk.PhotoImage(frame))
    num_frames = len(frames)
    # crea un widget Label e aggiungi la GIF
    label = tk.Label(window, image=frames[0])
    label.pack()
    # definisci una funzione per aggiornare l'immagine
    def update(frame):
        label.configure(image=frames[frame])
        window.after(50, update, (frame+1) % num_frames)
    # avvia la funzione per aggiornare l'immagine
    window.after(0, update, 0)

    # gestisci la chiusura della finestra
    def on_window_close():
        global window_open
        window_open = False
        window.quit()

    window.protocol("WM_DELETE_WINDOW", on_window_close)
#gif(x)
#print("suca")
#sws= input("Inserisci: ")