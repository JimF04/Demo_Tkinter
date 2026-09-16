import tkinter as tk
from PIL import Image, ImageTk

# ==========================================
# CONFIGURACIÓN PRINCIPAL
# ==========================================
root = tk.Tk() # ventana principal
root.title("Test Imagenes") 
root.geometry("640x480")

width = 640
height = 480

# Crear un frame que ocupe toda la ventana
frame = tk.Frame(root, width=width, height=height)
frame.pack(fill="both", expand=True)

# ====================================
# Imagen 1 
# ====================================

# Cargar imagen con label
img1 = tk.PhotoImage(file="img/torchic.png")

# Cambiar tamaño de imagen con subsample o zoom
img1 = img1.subsample(2) # mitad del tamaño original
# img1 = img1.zoom(2) # duplicar tamaño

label1 = tk.Label(frame, image=img1)
label1.pack(pady=10) 

# ====================================
# Imagen 2
# ====================================

# Cambiar tamaño de imagen con PIL
img2_raw = Image.open("img/combusken.png")
img2_raw = img2_raw.resize((100, 100)) # ancho x alto exacto
img2 = ImageTk.PhotoImage(img2_raw)

label2 = tk.Label(frame, image=img2)
label2.place(x=100, y=100)

# ==========================================
# LOOP PRINCIPAL
# ==========================================
root.mainloop() # Loop principal de la ventana