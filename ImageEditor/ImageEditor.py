
from PIL import Image, ImageEnhance, ImageFilter 
# import from Pillow library the classes: Image, ImageEnhance and ImageFilter

import os 
# import from the os module to provide functions for interacting with os such as listing files/handling paths

path = './imgs' 
# path variable that holds the directory to where the input images are stored

path0ut = '/editedimgs' 
# path variable that holds where the edited images will be saved

for filename in os.listdir(path): 
    # iterate thru each file in the specified directory (path). os.listdir(path) returns a list of all the file names in the directory
    
    img = Image.open(f"{path}/{filename}") # For each filename in the directory, the code opens the image using Image.open(). The path to the image is constructed using an f-string, combining the base path with the filename. 

    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90) 
    # The image undergoes a series of edits. .filter(ImageFilter.SHARPEN): Applies a sharpening filter to the image, .convert('L'): Converts the image to grayscale, .rotate(-90): Rotates the image 90 degrees counterclockwise.  

    factor = 1.5 
    # This line defines a contrast enhancement factor, which is set to 1.5 to increase its contrast
   
    enchancer = ImageEnhance.Contrast(edit)
   # Prepares to enhance the contrast of the edited image using the (edit) image
   
    edit = enchancer.enhance(factor) 
    # Enhances the contrast of the image by the factor of 1.5. A factor of 1.0 leaves the image unchanged, while greater than 1.0 increases contrast.

    clean_name = os.path.splitext(filename)[0] 
    #Splits the filename into the name and extension (.jpg, .png, etc.) using os.path.splitext(). The [0] part ensures only the name (without the extension) is saved in clean_name

    edit.save(f'.{path0ut}/{clean_name}_edited.jpg')
   # Saves the edited image in the editedimgs directory, appending _edited to the original file name. The new file will be saved as a .jpg image, even if the original image was in another format.