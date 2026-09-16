# Guía de Tkinter

Guía básica de Tkinter para Python. Cada archivo cubre un tema con ejemplos funcionales.

---

## Archivos

| Archivo | Tema |
|---|---|
| `0_ventana.py` | Ventana básica |
| `1_layout.py` | Posicionamiento: pack, place, anchor |
| `2_varias_ventanas.py` | Múltiples pantallas con frames |
| `3_canvas_vs_frames.py` | Diferencia entre Frame y Canvas |
| `4_widgets.py` | Demo de widgets |
| `5_imagenes.py` | Cargar y redimensionar imágenes |
| `6_animaciones.py` | Animación básica con Canvas |

---

## Conceptos clave

### Ventana principal
```python
root = tk.Tk()
root.title("Mi App")
root.geometry("640x480")
root.mainloop()  # loop principal — siempre al final
```

### Frame vs Canvas

**Frame** — contenedor de widgets. No dibuja gráficos.
```python
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Hola").place(x=100, y=100)
```

**Canvas** — área de dibujo. Soporta gráficos, texto e imágenes.
```python
canvas = tk.Canvas(frame, width=640, height=480, bg="white")
canvas.pack()

canvas.create_rectangle(10, 10, 100, 100)
canvas.create_text(200, 200, text="Hola")
canvas.create_window(300, 300, window=ttk.Entry(canvas))  # widget dentro del canvas
```

### Posicionamiento

**pack** — apila widgets en orden.
```python
tk.Label(frame, text="A").pack()                    # vertical por defecto
tk.Label(frame, text="B").pack(side="left")         # horizontal
tk.Label(frame, text="C").pack(fill="x", padx=5)   # expande al ancho
```

**place** — posición exacta con coordenadas x, y.
```python
tk.Label(frame, text="A").place(x=100, y=50)
tk.Label(frame, text="B").place(x=200, y=50, anchor="center")  # centrado en ese punto
```

**grid** — filas y columnas.
```python
tk.Label(frame, text="A").grid(row=0, column=0)
tk.Label(frame, text="B").grid(row=0, column=1)
tk.Label(frame, text="C").grid(row=1, column=0, columnspan=2)  # ocupa 2 columnas
```

> **Regla importante:** no mezcles `pack` y `place`/`grid` en el mismo contenedor.

### Múltiples ventanas

Se simulan con frames: uno visible a la vez.

```python
def mostrar_ventana2():
    frame_v1.pack_forget()
    frame_v2.pack(fill="both", expand=True)

def mostrar_ventana1():
    frame_v2.pack_forget()
    frame_v1.pack(fill="both", expand=True)
```

### Widgets comunes

| Widget | Uso |
|---|---|
| `tk.Label` | Mostrar texto o imagen |
| `ttk.Entry` | Campo de texto de una línea |
| `tk.Text` | Campo de texto multilínea |
| `ttk.Button` | Botón clickeable |
| `ttk.Checkbutton` | Casilla de verificación |
| `ttk.Radiobutton` | Selección única entre opciones |
| `ttk.Scale` | Slider numérico |
| `ttk.Combobox` | Lista desplegable |
| `tk.Listbox` | Lista de ítems seleccionables |
| `ttk.Progressbar` | Barra de progreso |

### Imágenes

**PNG/GIF sin dependencias:**
```python
img = tk.PhotoImage(file="imagen.png")
img = img.subsample(2)  # mitad del tamaño
tk.Label(frame, image=img).pack()
```

**Cualquier formato con PIL:**
```python
from PIL import Image, ImageTk

img_raw = Image.open("imagen.jpg")
img_raw = img_raw.resize((200, 200))  # tamaño exacto en píxeles
img = ImageTk.PhotoImage(img_raw)

lbl = tk.Label(frame, image=img)
lbl.image = img  # evita que la imagen sea eliminada de memoria
lbl.pack()
```

### Animaciones

Se usan `canvas.move()` y `root.after()` para crear un loop de animación.

```python
box = canvas.create_rectangle(0, 0, 50, 50, fill="black")
velx = 3

def animar():
    global velx
    canvas.move(box, velx, 0)

    pos = canvas.coords(box)  # [x1, y1, x2, y2]
    if pos[2] >= width or pos[0] <= 0:
        velx = -velx

    root.after(16, animar)  # 16ms ≈ 60fps

animar()
```

---

## Instalación

```bash
pip install tkinter
pip install pillow
```