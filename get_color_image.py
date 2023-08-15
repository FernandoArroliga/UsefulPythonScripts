from PIL import Image

# Cargar la imagen
image = Image.open("Login App/Images/background_image.jpg")

# Obtener el color en una posición específica
x = 100  # Coordenada x del píxel
y = 200  # Coordenada y del píxel

pixel_color = image.getpixel((x, y))

# Convertir el color en código hexadecimal
hex_color = '#{:02x}{:02x}{:02x}'.format(pixel_color[0], pixel_color[1], pixel_color[2])

print("Color en la posición ({}, {}): {}".format(x, y, hex_color))
