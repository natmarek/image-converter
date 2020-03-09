from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

# print(img.format)
# print(img.mode)
# print(img.size)
# print(dir(img))
# filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert('L')
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("GREY.png","png")
# crooked = filtered_img.rotate(90)
# crooked.save("crooked.png", "png")
# # crooked.show()
# resize = filtered_img.resize((300,300))
# resize.save("resize.png", "png")
# print(crooked.size)