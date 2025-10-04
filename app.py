import turtle
import tkinter as tk
wn = turtle.Screen()
wn.title("Touch + Tastatursteuerungs zeichen Program.")
t = turtle.Turtle()
def nach_vorne():
    t.forward(20)
    print("Richtung:", t.heading())
def nach_links():
    t.left(15)
    print("Richtung:", t.heading())
def nach_rechts():
    t.right(15)
    print("Richtung:", t.heading())
def zurueck():
    t.backward(20)
    print("Richtung:", t.heading())
wn.listen()
wn.onkeypress(nach_vorne, "Up")
wn.onkeypress(zurueck, "Down")
wn.onkeypress(nach_links, "Left")
wn.onkeypress(nach_rechts, "Right")
root = wn._root
frame = tk.Frame(root)
frame.pack(side=tk.RIGHT, padx=20, pady=20)
btn_vorne = tk.Button(frame, text=" Vorne", font=("Arial", 14), command=nach_vorne, width=10, height=2)
btn_links = tk.Button(frame, text=" Links", font=("Arial", 14), command=nach_links, width=10, height=2)
btn_rechts = tk.Button(frame, text=" Rechts", font=("Arial", 14), command=nach_rechts, width=10, height=2)
btn_zurueck = tk.Button(frame, text="Zurück", font=("Arial", 14), command=zurueck, width=10, height=2)
btn_vorne.grid(row=0, column=1, pady=5)
btn_links.grid(row=1, column=0, padx=5)
btn_rechts.grid(row=1, column=2, padx=5)
btn_zurueck.grid(row=2, column=1, pady=5)
wn.mainloop()
