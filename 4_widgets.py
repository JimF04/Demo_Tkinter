import tkinter as tk
from tkinter import ttk

# ==========================================
# CONFIGURACIÓN PRINCIPAL
# ==========================================
root = tk.Tk()
root.title("Test Widgets")
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
# VENTANA 1 - Widgets de entrada
# ==========================================
frame_v1 = tk.Frame(root)
frame_v1.pack(fill="both", expand=True)

tk.Label(frame_v1, text="Widgets de Entrada", font=("Arial", 18, "bold")).place(x=WIDTH//2, y=30, anchor="center")

# Label
tk.Label(frame_v1, text="Label:", font=("Arial", 10)).place(x=50, y=80)
tk.Label(frame_v1, text="Hola, soy un Label", font=("Arial", 11)).place(x=200, y=80)

# Entry
tk.Label(frame_v1, text="Entry:", font=("Arial", 10)).place(x=50, y=130)
ttk.Entry(frame_v1, width=25).place(x=200, y=130)

# Button
tk.Label(frame_v1, text="Button:", font=("Arial", 10)).place(x=50, y=180)
ttk.Button(frame_v1, text="Click aquí").place(x=200, y=180)

# Checkbutton
tk.Label(frame_v1, text="Checkbutton:", font=("Arial", 10)).place(x=50, y=230)
check_var = tk.BooleanVar()
ttk.Checkbutton(frame_v1, text="Activar opción", variable=check_var).place(x=200, y=230)

# Radiobutton
tk.Label(frame_v1, text="Radiobutton:", font=("Arial", 10)).place(x=50, y=280)
radio_var = tk.StringVar(value="A")
ttk.Radiobutton(frame_v1, text="Opción A", variable=radio_var, value="A").place(x=200, y=280)
ttk.Radiobutton(frame_v1, text="Opción B", variable=radio_var, value="B").place(x=310, y=280)

# Scale
tk.Label(frame_v1, text="Scale:", font=("Arial", 10)).place(x=50, y=330)
ttk.Scale(frame_v1, from_=0, to=100, orient="horizontal", length=200).place(x=200, y=330)

# Navegación
ttk.Button(frame_v1, text="Siguiente", command=mostrar_ventana2).place(x=WIDTH - 110, y=HEIGHT - 40)

# ==========================================
# VENTANA 2 - Widgets de selección/display
# ==========================================
frame_v2 = tk.Frame(root)

tk.Label(frame_v2, text="Widgets de Selección / Display", font=("Arial", 18, "bold")).place(x=WIDTH//2, y=30, anchor="center")

# Combobox
tk.Label(frame_v2, text="Combobox:", font=("Arial", 10)).place(x=50, y=90)
combo_demo = ttk.Combobox(frame_v2, values=["Opción 1", "Opción 2", "Opción 3"], width=20)
combo_demo.set("Selecciona...")
combo_demo.place(x=200, y=90)

# Listbox
tk.Label(frame_v2, text="Listbox:", font=("Arial", 10)).place(x=50, y=150)
listbox_demo = tk.Listbox(frame_v2, height=4, width=20, selectbackground="#7c3aed")
listbox_demo.insert(tk.END, "Item 1")
listbox_demo.insert(tk.END, "Item 2")
listbox_demo.insert(tk.END, "Item 3")
listbox_demo.insert(tk.END, "Item 4")
listbox_demo.place(x=200, y=150)

# Text
tk.Label(frame_v2, text="Text:", font=("Arial", 10)).place(x=50, y=270)
text_demo = tk.Text(frame_v2, height=4, width=30, insertbackground="white")
text_demo.insert("1.0", "Área de texto\nmulti-línea...")
text_demo.place(x=200, y=270)

# Progressbar
tk.Label(frame_v2, text="Progressbar:", font=("Arial", 10)).place(x=50, y=390)
ttk.Progressbar(frame_v2, length=200, value=65).place(x=200, y=390)
tk.Label(frame_v2, text="65%", font=("Arial", 10)).place(x=415, y=390)

# Navegación
ttk.Button(frame_v2, text="Anterior", command=mostrar_ventana1).place(x=20, y=HEIGHT - 40)

# ==========================================
# LOOP PRINCIPAL
# ==========================================
root.mainloop()