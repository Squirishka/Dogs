from tkinter import *
from tkinter import messagebox as mb
import requests
from PIL import Image, ImageTk
from io import BytesIO



def show_image():
    image_url = get_dog_image()
    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            image_data = BytesIO(response.content)
            img = Image.open(image_data)
            img.thumbnail((300, 300))
            label.config(image=img)
            label.image = img
        except Exception as ex:
            mb.showerror(title='Ошибка!', message=f'Возникла ошибка - {ex}')

window = Tk()
window.title('Картинки и собачки')
window.geometry('360x420')

label = Label()
label.pack(pady=10)

button = Button(text='Загрузить изображение', command=show_image)
button.pack(pady=10)

window.mainloop()
