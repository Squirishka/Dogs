from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
from PIL import Image, ImageTk
from io import BytesIO


def get_dog_image():
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response.raise_for_status()
        data = response.json()
        return data['message']
    except Exception as ex:
        mb.showerror(title='Ошибка!', message=f'Возникла ошибка при запросе к API = {ex}')
        return None


def show_image():
    image_url = get_dog_image()
    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            image_data = BytesIO(response.content)
            img = Image.open(image_data)
            img_size = (int(width_spinbox.get()), int(height_spinbox.get()))
            img.thumbnail(img_size)
            img = ImageTk.PhotoImage(img)
            new_window = Toplevel(window)
            new_window.title('Случайно изображение')
            lb = ttk.Label(new_window, image=img)
            lb.pack()
            lb.image = img
        except Exception as ex:
            mb.showerror(title='Ошибка!', message=f'Возникла ошибка при загрузке изображения - {ex}')

    prog_bar.stop()


def prog():
    prog_bar['value'] = 0
    prog_bar.start(30)
    window.after(3000, show_image)


window = Tk()
window.title('Картинки и собачки')
window.geometry('360x420')

label = ttk.Label()
label.pack(pady=10)

button = ttk.Button(text='Загрузить изображение', command=prog)
button.pack(pady=10)

prog_bar = ttk.Progressbar(mode='determinate', length=300)
prog_bar.pack(pady=10)

width_label = ttk.Label(text='Ширина: ')
width_label.pack(side='left', padx=(10, 0))

width_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
width_spinbox.pack(side='left', padx=(0, 10))

height_label = ttk.Label(text='Высота: ')
height_label.pack(side='left', padx=(10, 0))

height_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
height_spinbox.pack(side='left', padx=(0, 10))

window.mainloop()
