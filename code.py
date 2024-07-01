import os
import shutil
import ctypes

def install_fonts(directory):
  # Get all files in the specified directory
  base = "your_directory_path"
  files = os.listdir(base)

  # Filter only the font files (you may need to customize this based on the types of font files you have, you get)
  # this is just fine for most fonts
  font_files = [file for file in files if file.lower().endswith(('.ttf', '.otf', '.woff', '.woff2'))]

  # The path where Windows fonts are usually stored
  windows_fonts_path = os.path.join(os.environ['SystemRoot'], 'Fonts')

  # Install each font file
  for font_file in font_files:
      font_path = os.path.join(base, font_file)
      destination_path = os.path.join("C:/Users/Hp/Downloads/NewFonts", font_file)

      # Copy the font file to the Fonts directory
      shutil.copy(font_path, destination_path)

      print(f"{font_file} installed successfully.")

  # Inform the system about the changes (this might require administrator privileges)
  ctypes.windll.user32.SendMessageW(0xFFFF, 0x001D, 0, 0)

# Replace 'your_directory_path' with the path of the directory containing the font files
directory_path = 'your_directory_path'
install_fonts(directory_path)
