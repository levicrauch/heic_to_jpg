# Import necessary libraries
from PIL import Image
import pillow_heif
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

# Function to convert HEIC images to JPG
def heic_to_jpg(file_path):
    image = Image.open(file_path)  # Open the image
    image.save(file_path.replace(".heic", ".jpg"), "JPEG")  # Save it as a JPEG
    os.remove(file_path)  # Remove the original file
    print("Converted", file_path, "successfully")

# Function to find all HEIC files in a directory
def find_heic_files(directory):
    heic_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".heic"):
                heic_files.append(os.path.join(root, file))
    return heic_files

# GUI class
class App:
    def __init__(self, root):
        self.root = root
        root.title("HEIC to JPG Converter")  # Set window title
        root.configure(bg='#282a36')  # Set background color

        # Create "Select Directory" button
        self.button = tk.Button(root, text="Select Directory for Conversion", command=self.select_directory, font=("Helvetica", 14), bg='#6272a4', fg='white', width=10)
        self.button.grid(row=0, column=0, padx=300, pady=20, sticky='ew')  # Position button

        # Create progress bar
        self.progress = ttk.Progressbar(root, length=300, mode='determinate', style='blue.Horizontal.TProgressbar')
        self.progress.grid(row=1, column=0, padx=20, pady=10, sticky='ew')  # Position progress bar

        # Create progress label
        self.progress_label = tk.Label(root, text="", font=("Helvetica", 12), bg='#282a36', fg='white')
        self.progress_label.grid(row=2, column=0, padx=20, pady=10, sticky='ew')  # Position progress label

        # Create file label
        self.file_label = tk.Label(root, text="", font=("Helvetica", 12), bg='#282a36', fg='white')
        self.file_label.grid(row=3, column=0, padx=20, pady=10, sticky='ew')  # Position file label

    # Function to select directory and start conversion
    def select_directory(self):
        directory = filedialog.askdirectory()  # Ask user to select directory
        heic_files = find_heic_files(directory)  # Find all HEIC files in the directory
        print("Found", len(heic_files), "heic files")
        for file in heic_files:
            print(file)
        
        # Confirm conversion in GUI
        confirm = messagebox.askokcancel("Conversion", "Found " + str(len(heic_files)) + " heic files. Click OK to convert.")
        if confirm:
            self.convert_heic_files(heic_files)  # Start conversion

    # Function to convert all HEIC files to JPG
    def convert_heic_files(self, heic_files):
        self.progress['maximum'] = len(heic_files)  # Set maximum value of progress bar
        failed_files = []  # List to store names of files that failed to convert
        for i, file in enumerate(heic_files):
            try:
                heic_to_jpg(file)  # Convert file
                self.progress['value'] = i + 1  # Update progress bar
                self.progress_label['text'] = f"Converting file {i+1} of {len(heic_files)}"  # Update progress label
                self.file_label['text'] = f"Current file: {file}"  # Update file label
            except Exception as e:
                failed_files.append(file)  # Add file to list of failed files
                self.file_label['text'] = f"Failed to convert: {file}. Error: {str(e)}"  # Update file label
            finally:
                self.root.update_idletasks()  # Update GUI

        # Handle failed files
        if failed_files:
            messagebox.showerror("Conversion Error", "Failed to convert the following files:\n" + "\n".join(failed_files))  # Show error message
            # Ask user if they want to move failed files to a new directory
            if messagebox.askyesno("Move Failed Files", "Do you want to move the failed files to a new directory?"):
                failed_dir = filedialog.askdirectory(title="Select Directory for Failed Files")  # Ask user to select directory
                if failed_dir:
                    for file in failed_files:
                        try:
                            os.rename(file, os.path.join(failed_dir, os.path.basename(file)))  # Move file
                        except Exception as e:
                            messagebox.showerror("File Moving Error", f"Failed to move file {file} due to error: {str(e)}")  # Show error message
                else:
                    messagebox.showinfo("No Directory Selected", "No directory was selected. The failed files were not moved.")  # Show info message
        else:
            messagebox.showinfo("Completion", "All files have been successfully converted.")  # Show info message
                
        self.reset_gui()  # Reset GUI

    # Function to reset GUI
    def reset_gui(self):
        self.progress['value'] = 0  # Reset progress bar
        self.progress_label['text'] = ""  # Reset progress label
        self.file_label['text'] = ""  # Reset file label

# Create and run GUI
root = tk.Tk()
root.geometry("1200x300")  # Set window size
root.columnconfigure(0, weight=1)  # Allow the column to grow and shrink
app = App(root)
root.mainloop()