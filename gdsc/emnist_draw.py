import tkinter as tk
from tkinter import messagebox
import numpy as np
from PIL import Image, ImageDraw, ImageOps
import tensorflow as tf
import io

class EMNISTApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Klasifikasi Karakter EMNIST")

        self.canvas_width = 280
        self.canvas_height = 280
        self.bg_color = "black"
        self.paint_color = "white"
        self.brush_size = 8

        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height, bg=self.bg_color)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.paint)

        self.predict_button = tk.Button(self.master, text="Prediksi", command=self.predict)
        self.predict_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.RIGHT)

        self.model = tf.keras.models.load_model('emnist_model.keras')
        
        self.image = Image.new("L", (self.canvas_width, self.canvas_height), self.bg_color)
        self.draw = ImageDraw.Draw(self.image)

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.paint_color, outline=self.paint_color)
        self.draw.ellipse([x1, y1, x2, y2], fill=self.paint_color, outline=self.paint_color)

    def predict(self):
        img = self.image.copy()
        img = img.resize((28, 28), Image.LANCZOS)
        img = np.array(img)
        img = img.reshape(1, 28, 28, 1)
        img = img.astype('float32')
        img /= 255.0

        prediction = self.model.predict(img)
        predicted_char = np.argmax(prediction)
        maps = {
            0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
            10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 16: "G", 17: "H", 18: "I",
            19: "J", 20: "K", 21: "L", 22: "M", 23: "N", 24: "O", 25: "P", 26: "Q", 27: "R",
            28: "S", 29: "T", 30: "U", 31: "V", 32: "W", 33: "X", 34: "Y", 35: "Z",
            36: "a", 37: "b", 38: "d", 39: "e", 40: "f", 41: "g", 42: "h", 43: "n", 44: "q", 
            45: "r", 46: "t"
        }

        predicted_char = maps.get(predicted_char, "???")
        messagebox.showinfo("Prediksi", f"Karakter yang Diprediksi: {predicted_char}")

    def reset(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_width, self.canvas_height), self.bg_color)
        self.draw = ImageDraw.Draw(self.image)

if __name__ == "__main__":
    root = tk.Tk()
    app = EMNISTApp(root)
    root.mainloop()
