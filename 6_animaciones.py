import tkinter as tk

# Configuración de ventana
root = tk.Tk()
root.title("Test Animation")
root.geometry("640x480")

width = 640
height = 480

# Crear el lienzo (Canvas)
canvas = tk.Canvas(root, width=width, height=height, bg="black")
canvas.pack()

# Crear objeto en el canvas (rectangulo)
box = canvas.create_rectangle(30, 30, 100, 100, fill="purple") # [x1, y1, x2, y2]

# Estado inicial (pasos en x)
velx = 3

def animar():
    global velx

    # Mover la caja
    canvas.move(box, velx, 0)

    # Obtener pos actual de la caja [x1, y1, x2, y2]
    pos = canvas.coords(box)

    # Detectar colisiones con borde
    if pos[2] >= width or pos[0] <= 0:
        velx = -velx

    # Loop de animar() 
    root.after(16, animar) # 16 ms = 60 fps

# Iniciar animación
animar()

# ==========================================
# LOOP PRINCIPAL
# ==========================================
root.mainloop()