from rembg import remove
from PIL import Image
input_path = 'Jerome-Powell.jpg'
output_path = 'Jerome-Powell.png'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
Image.open(output_path)