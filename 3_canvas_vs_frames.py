import tkinter as tk
from tkinter import ttk

# ==========================================
# CONFIGURACIÓN PRINCIPAL
# ==========================================
root = tk.Tk()
root.title("Frames vs Canvas")
root.geometry("640x480")

WIDTH  = 640
HEIGHT = 480

# ==========================================
# NAVEGACIÓN
# ==========================================
def mostrar_ventana2():
    frame_v1.pack_forget()
    frame_v2.pack(fill="both", expand=True)

def mostrar_ventana1():
    frame_v2.pack_forget()
    frame_v1.pack(fill="both", expand=True)

# ==========================================
# VENTANA 1 - Frame
# ==========================================
frame_v1 = tk.Frame(root)
frame_v1.pack(fill="both", expand=True)

tk.Label(frame_v1, text="Frame", font=("Arial", 16, "bold")).place(x=WIDTH//2, y=20, anchor="center")
tk.Label(frame_v1, text="Contenedor de widgets. Posiciona con pack / place / grid.").place(x=WIDTH//2, y=55, anchor="center")

# Demo widgets con pack
demo_frame = tk.Frame(frame_v1, relief="solid", bd=1, width=400, height=220)
demo_frame.place(x=WIDTH//2, y=90, anchor="n")
demo_frame.pack_propagate(False)

tk.Label(demo_frame,  text="Soy un Label").pack(pady=8)
ttk.Entry(demo_frame, width=25).pack(pady=5)
ttk.Button(demo_frame, text="Soy un Button").pack(pady=5)
ttk.Checkbutton(demo_frame, text="Soy un Checkbutton").pack(pady=5)
ttk.Scale(demo_frame, from_=0, to=100, orient="horizontal", length=200).pack(pady=5)

tk.Label(frame_v1, text="Usa Frame cuando necesites organizar widgets").place(x=WIDTH//2, y=340, anchor="center")

ttk.Button(frame_v1, text="Siguiente", command=mostrar_ventana2).place(x=WIDTH - 110, y=HEIGHT - 35)

# ==========================================
# VENTANA 2 - Canvas
# ==========================================
frame_v2 = tk.Frame(root)

tk.Label(frame_v2, text="Canvas", font=("Arial", 16, "bold")).place(x=WIDTH//2, y=20, anchor="center")
tk.Label(frame_v2, text="Área de dibujo. Usa coordenadas x, y para gráficos y widgets.").place(x=WIDTH//2, y=55, anchor="center")

# Demo gráficos
demo_canvas = tk.Canvas(frame_v2, width=400, height=220, bg="white", relief="solid", bd=1)
demo_canvas.place(x=WIDTH//2, y=90, anchor="n")

demo_canvas.create_rectangle(20,  20, 120, 80, outline="black")
demo_canvas.create_oval(140, 20, 240, 80, outline="black")
demo_canvas.create_line(260, 20, 380, 80, fill="black", width=2)
demo_canvas.create_text(200, 110, text="Texto dibujado con create_text", font=("Arial", 10))
demo_canvas.create_polygon(60, 140, 100, 200, 20, 200, outline="black", fill="lightgray")

entry_canvas = ttk.Entry(demo_canvas, width=15)
demo_canvas.create_window(300, 170, window=entry_canvas)
demo_canvas.create_text(300, 148, text="Entry con create_window", font=("Arial", 9))

tk.Label(frame_v2, text="Usa Canvas cuando necesites dibujar gráficos o animaciones").place(x=WIDTH//2, y=340, anchor="center")

ttk.Button(frame_v2, text="Anterior", command=mostrar_ventana1).place(x=20, y=HEIGHT - 35)

# ==========================================
# LOOP PRINCIPAL
# ==========================================
root.mainloop()