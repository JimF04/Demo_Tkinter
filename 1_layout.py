import tkinter as tk
from tkinter import ttk

# ==========================================
# CONFIGURACIÓN PRINCIPAL
# ==========================================
root = tk.Tk()
root.title("Test Layout")
root.geometry("640x480")

WIDTH  = 640
HEIGHT = 480

# Frame principal
frame = tk.Frame(root, bg="#1e1e2e")
frame.pack(fill="both", expand=True)

tk.Label(frame, text="pack  vs  place", bg="#1e1e2e", fg="white", font=("Arial", 16, "bold")).place(x=WIDTH//2, y=20, anchor="center")

# ==========================================
# PACK: apila widgets en orden 
# ==========================================
tk.Label(frame, text="── pack ──", bg="#1e1e2e", fg="#aaaaaa").place(x=50, y=60)

pack_frame = tk.Frame(frame, bg="#313244", width=250, height=150)
pack_frame.place(x=50, y=85)
pack_frame.pack_propagate(False)  # evita que el frame se encoja

# pack con fill="x": alinea los widgets horizontalmente y los expande al ancho del frame
tk.Label(pack_frame, text="Label A", bg="#7c3aed", fg="white").pack(fill="x", padx=5, pady=3)
tk.Label(pack_frame, text="Label B", bg="#7c3aed", fg="white").pack(fill="x", padx=5, pady=3)
tk.Label(pack_frame, text="Label C", bg="#7c3aed", fg="white").pack(fill="x", padx=5, pady=3)

# pack con side="left": alinea los widgets horizontalmente y los coloca uno al lado del otro
tk.Label(pack_frame, text="side=LEFT", bg="#2a6f97", fg="white").pack(side="left", padx=5, pady=3)
tk.Label(pack_frame, text="side=LEFT", bg="#2a6f97", fg="white").pack(side="left", padx=5, pady=3)

# pack con side="top": alinea los widgets verticalmente y los coloca uno encima del otro
tk.Label(pack_frame, text="side=TOP", bg="#2a6f97", fg="white").pack(side="top", padx=5, pady=3)
tk.Label(pack_frame, text="side=TOP", bg="#2a6f97", fg="white").pack(side="top", padx=5, pady=3)

# ==========================================
# PLACE: posición exacta en x, y 
# ==========================================
tk.Label(frame, text="── place ──", bg="#1e1e2e", fg="#aaaaaa").place(x=360, y=60)

place_frame = tk.Frame(frame, bg="#313244", width=200, height=150)
place_frame.place(x=360, y=85)

# place con x, y: coloca los widgets en coordenadas exactas dentro del frame
tk.Label(place_frame, text="x=10, y=10",   bg="#7c3aed", fg="white").place(x=10,  y=10)
tk.Label(place_frame, text="x=80, y=60",   bg="#2a6f97", fg="white").place(x=80,  y=60)
tk.Label(place_frame, text="x=30, y=110",  bg="#7c3aed", fg="white").place(x=30,  y=110)


tk.Label(frame, text="── anchor ──", bg="#1e1e2e", fg="#aaaaaa").place(x=50, y=260)

# anchor en place: permite alinear el widget respecto a un punto de referencia (norte, sur, este, oeste, centro)
tk.Label(frame, text="anchor='nw' (default)", bg="#313244", fg="white").place(x=50, y=285, anchor="nw")
tk.Label(frame, text="anchor='center'", bg="#313244", fg="white").place(x=WIDTH//2, y=320, anchor="center")
tk.Label(frame, text="anchor='e'", bg="#313244", fg="white").place(x=WIDTH-50, y=355, anchor="e")

# ==========================================
# LOOP PRINCIPAL
# ==========================================
root.mainloop()