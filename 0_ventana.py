import tkinter as tk

# ==========================================
# CONFIGURACIÓN PRINCIPAL
# ==========================================
root = tk.Tk() # ventana principal
root.title("Test Ventana") 
root.geometry("640x480")

width = 640
height = 480

# Crear un frame que ocupe toda la ventana
frame = tk.Frame(root, width=width, height=height, bg="#32a852")
frame.pack(fill="both", expand=True)

# ==========================================
# LOOP PRINCIPAL
# ==========================================
root.mainloop() 