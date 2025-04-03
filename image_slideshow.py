import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from pathlib import Path

class ImageSlideshow:
    def __init__(self, root):
        self.root = root
        self.root.title("이미지 슬라이드쇼")
        
        # 이미지 리스트와 현재 인덱스
        self.images = []
        self.current_index = 0
        
        # 메인 프레임
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(expand=True, fill='both')
        
        # 이미지 표시 레이블
        self.image_label = tk.Label(self.main_frame)
        self.image_label.pack(expand=True)
        
        # 컨트롤 프레임
        self.control_frame = tk.Frame(self.main_frame)
        self.control_frame.pack(side='bottom', pady=10)
        
        # 버튼들
        self.prev_button = tk.Button(self.control_frame, text="이전", command=self.prev_image)
        self.prev_button.pack(side='left', padx=5)
        
        self.next_button = tk.Button(self.control_frame, text="다음", command=self.next_image)
        self.next_button.pack(side='left', padx=5)
        
        self.select_folder_button = tk.Button(self.control_frame, text="폴더 선택", command=self.select_folder)
        self.select_folder_button.pack(side='left', padx=5)
        
        # 키보드 바인딩
        self.root.bind('<Left>', lambda e: self.prev_image())
        self.root.bind('<Right>', lambda e: self.next_image())
        
        # 창 크기 조절 이벤트
        self.root.bind('<Configure>', self.on_resize)
        
    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.load_images(folder_path)
    
    def load_images(self, folder_path):
        self.images = []
        valid_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
        
        for file in os.listdir(folder_path):
            if Path(file).suffix.lower() in valid_extensions:
                self.images.append(os.path.join(folder_path, file))
        
        if self.images:
            self.current_index = 0
            self.show_current_image()
        else:
            messagebox.showwarning("경고", "선택한 폴더에 이미지 파일이 없습니다.")
    
    def show_current_image(self):
        if not self.images:
            return
            
        # 이미지 로드 및 리사이즈
        image = Image.open(self.images[self.current_index])
        self.display_image(image)
    
    def display_image(self, image):
        # 창 크기에 맞게 이미지 리사이즈
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        
        # 이미지 비율 유지하면서 리사이즈
        image_ratio = image.width / image.height
        window_ratio = window_width / window_height
        
        if window_ratio > image_ratio:
            new_height = window_height
            new_width = int(new_height * image_ratio)
        else:
            new_width = window_width
            new_height = int(new_width / image_ratio)
        
        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(resized_image)
        
        self.image_label.config(image=photo)
        self.image_label.image = photo  # 참조 유지
    
    def next_image(self):
        if self.images:
            self.current_index = (self.current_index + 1) % len(self.images)
            self.show_current_image()
    
    def prev_image(self):
        if self.images:
            self.current_index = (self.current_index - 1) % len(self.images)
            self.show_current_image()
    
    def on_resize(self, event):
        if self.images:
            self.show_current_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSlideshow(root)
    root.mainloop() 