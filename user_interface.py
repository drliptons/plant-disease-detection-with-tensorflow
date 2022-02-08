import os
import tkinter as tk
import tkmacosx as tkmac
import sys
from tkinter import filedialog
from PIL import Image, ImageTk
from backend import Backend


class UserInterface(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.root = root

        # Store image and image path
        self._image = []
        self._image_path = tk.StringVar()

        # Frame 1: for load and preview to the app
        self._frame_1 = tk.LabelFrame(self.root, text='Source')
        self._frame_1.pack(fill='both', expand=True, padx=10, pady=10)
        # Preview image box
        self._preview_image_frame = tk.LabelFrame(self._frame_1, width=300, height=300)
        self._preview_image_frame.pack(fill='both', expand=True, side='top', padx=1, pady=1)
        self._in_frame = tk.Label(self._preview_image_frame)
        self._in_frame.pack()
        # Path label
        self._path_label = tk.Label(self._frame_1, text='Path:')
        self._path_label.pack(side='left', padx=10, pady=10)
        # Entry box
        self._path_entry = tk.Entry(self._frame_1, textvariable=self._image_path, width=30)
        self._path_entry.pack(side='left', padx=10, pady=10)
        # 'Browse' and 'Detect' button
        if sys.platform == "darwin":
            self._browse_button = tkmac.Button(self._frame_1, text='Browse', bg='#D6E6F2', activebackground='#D6E6F2',
                                               command=self._browse_image)
            self._browse_button.pack(side='left', padx=10, pady=10)
            self._detect_button = tkmac.Button(self._frame_1, text='Detect', bg='#B9D7EA', command=self._detect_image)
            self._detect_button.pack(side='left', padx=10, pady=10)
        else:
            self._browse_button = tk.Button(self._frame_1, text='Browse', bg='#D6E6F2', command=self._browse_image)
            self._browse_button.pack(side='left', padx=10, pady=10)
            self._detect_button = tk.Button(self._frame_1, text='Detect', bg='#B9D7EA', command=self._detect_image)
            self._detect_button.pack(side='left', padx=10, pady=10)

        # Frame 2: displaying model predicted result
        self._frame_2 = tk.LabelFrame(self.root, text='Result')
        self._frame_2.pack(fill='both', expand=False, padx=10, pady=10)
        # Result title text
        self._result_label = tk.Label(self._frame_2, text='Result:')
        self._result_label.grid(row=0, column=0, sticky='w')
        # Predicted result text
        self._output_text = tk.Label(self._frame_2, text='Waiting for an image...')
        self._output_text.grid(row=1, column=0, sticky='w')

        # Initialize Backend class
        self._backend = Backend()

    def _show_image(self, path: str):
        img = Image.open(path)
        resize_img = img.resize((530, 530), Image.ANTIALIAS)
        self._image = ImageTk.PhotoImage(resize_img)
        self._in_frame.configure(image=self._image)

    def _browse_image(self):
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title='Browse Image', filetypes=(
            ('JPEG/JPG', '*.jpg'),
            ('PNG', '*.png'),
            ('All Files', '*.*')))
        self._image_path.set(fln)
        self._show_image(fln)

    def _detect_image(self):
        text = self._backend.predict_image(self._image_path.get())
        self._output_text.configure(text=text)
