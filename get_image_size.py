from PIL import Image

# Abre la imagen
image_path = "imagepath.jpg"  # Cambia esto a la ruta de tu imagen
image = Image.open(image_path)

# Obtiene el tamaño de la imagen (ancho x alto)
width, height = image.size

print(f"Ancho: {width}px")
print(f"Alto: {height}px")
