import tkinter as tk
from tkinter import filedialog
from reportlab.pdfgen import canvas
from PIL import Image
import os



class IMGtoPDFConverter:
    def __init__(self, root):
        self.root = root
        self.image_path = []
        self.output_pdf_name = tk.StringVar()
        self.selected_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)

        self.initialize_ui()

    def initialize_ui(self): #Set the UI of the application
        title = tk.Label(self.root, text="PDF Converter", font=("Cambria", 15, "bold"))
        title.pack(pady=10)

        upload_image_button = tk.Button(self.root, text="Upload Image", command= self.upload_image)
        upload_image_button.pack(pady=(0, 10))

        self.selected_images_listbox.pack(pady=(0, 10), fill = tk.BOTH, expand= True)
        label = tk.Label(self.root, text= "Enter output PDF name:")
        label.pack()

        pdf_name = tk.Entry(self.root, textvariable=self.output_pdf_name, width=40, justify='center')
        pdf_name.pack()

        convert_button = tk.Button(self.root, text="Convert to PDF", command=self.convert_to_pdf)
        convert_button.pack(pady=(20, 40))

    def upload_image(self):
        self.image_path = filedialog.askopenfilenames(title="Upload Images", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg:*.docx")])
        self.image_details()

    def image_details(self):
        self.selected_images_listbox.delete(0, tk.END)

        for image_path in self.image_path:
            _, image_path = os.path.split(image_path)
            self.selected_images_listbox.insert(tk.END, image_path)

    def convert_to_pdf(self):
        if not self.image_path:
            return

        output_path = self.output_pdf_name.get() + ".pdf" if self.output_pdf_name.get() else "output.pdf"

        pdf = canvas.Canvas(output_path, pagesize=(612, 792))

        for img_path in self.image_path:
            img = Image.open(img_path)
            def_width = 540
            def_height = 720
            scale_factor = min(def_width/img.width , def_height/img.height)
            new_width = img.width *scale_factor
            new_height = img.height * scale_factor
            x_center = (612 - new_width) / 2
            y_center = (792 - new_height) / 2

            pdf.setFillColorRGB(255, 255, 255)
            pdf.rect(0, 0 , 612, 792, fill= True)
            pdf.drawInlineImage(img, x_center, y_center, width=new_width, height= new_height)
            pdf.showPage()
        pdf.save()






def main():
    root = tk.Tk() #Initialize the library
    root.title("Image to PDF Converter") #Set the title of the application on the Windows app
    converter = IMGtoPDFConverter(root)
    root.geometry("400x600") #Determine the size of the desktop application
    root.mainloop()


if __name__ == "__main__":
    main()

