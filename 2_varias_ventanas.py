import tkinter as tk
from tkinter import ttk

# ==========================================
# CONFIGURACIÓN PRINCIPAL
# ==========================================
root = tk.Tk()
root.title("Test multiples ventanas")
root.geometry("640x480")

WIDTH  = 640
HEIGHT = 480

# ==========================================
# NAVEGACIÓN
# ==========================================
def mostrar_ventana2():
    frame_v1.pack_forget()  # Oculta la ventana 1
    frame_v2.pack(fill="both", expand=True)  # Muestra la ventana 2

def mostrar_ventana1():
    frame_v2.pack_forget()  # Oculta la ventana 2
    frame_v1.pack(fill="both", expand=True)  # Muestra la ventana 1

# ==========================================
# VENTANA 1
# ==========================================
frame_v1 = tk.Frame(root)
frame_v1.pack(fill="both", expand=True)

tk.Label(frame_v1, text="Ventana 1", font=("Arial", 24)).place(x=WIDTH//2, y=HEIGHT//2, anchor="center")

btn_v1 = ttk.Button(
    frame_v1,
    text="Ir a Ventana 2",
    command=mostrar_ventana2
)
btn_v1.place(x=20, y=20)

# ==========================================
# VENTANA 2
# ==========================================
frame_v2 = tk.Frame(root)

# Puedes agregar canvas dentro de frames
canvas_v2 = tk.Canvas(frame_v2, width=WIDTH, height=HEIGHT, bg="#2a6f97")
canvas_v2.pack()

canvas_v2.create_text(WIDTH//2, HEIGHT//2, text="Ventana 2", fill="white", font=("Arial", 24))

btn_v2 = ttk.Button(
    frame_v2,
    text="Volver a Ventana 1",
    command=mostrar_ventana1
)
btn_v2.place(x=20, y=20)

# ==========================================
# LOOP PRINCIPAL
# ==========================================
root.mainloop()