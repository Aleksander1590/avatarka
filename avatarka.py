from PIL import Image
image = Image.open("C:\\python_scripts\\4-Narezaem_avatarki\\example.jpg")
rgb_image = image.convert("RGB")
(red, green, blue) = rgb_image.split()
red.save("C:\\python_scripts\\4-Narezaem_avatarki\\red.jpg")
green.save("C:\\python_scripts\\4-Narezaem_avatarki\\green.jpg")
blue.save("C:\\python_scripts\\4-Narezaem_avatarki\\blue.jpg")

image1 = Image.open("C:\\python_scripts\\4-Narezaem_avatarki\\red.jpg")
displacement_value1 = 50
coordinates1 = (displacement_value1, 0, 417, 417)
cropped1 = image1.crop(coordinates1)
image2 = Image.open("C:\\python_scripts\\4-Narezaem_avatarki\\red.jpg")
displacement_value2 = 417 - displacement_value1
coordinates2 = (0, 0, displacement_value2, 417)
cropped2 = image2.crop(coordinates2)
blend_displacement1 = Image.blend(cropped1, cropped2, 0.9)

image3 = Image.open("C:\\python_scripts\\4-Narezaem_avatarki\\blue.jpg")
coordinates3 = (0, 0, displacement_value2, 417)
cropped3 = image3.crop(coordinates3)
image4 = Image.open("C:\\python_scripts\\4-Narezaem_avatarki\\blue.jpg")
coordinates4 = (displacement_value1, 0, 417, 417)
cropped4 = image4.crop(coordinates4)
blend_displacement2 = Image.blend(cropped3, cropped4, 0.1)

image5 = Image.open("C:\\python_scripts\\4-Narezaem_avatarki\\green.jpg")
displacement_value3 = displacement_value1 / 2
displacement_value4 = 417 - displacement_value1 / 2
coordinates5 = (displacement_value3, 0, displacement_value4, 417)
cropped5 = image5.crop(coordinates5)

merge_image = Image.merge("RGB", (blend_displacement1, blend_displacement2, cropped5))
merge_image.save("C:\\python_scripts\\4-Narezaem_avatarki\\final.jpg")
final_resized = Image.open("C:\\python_scripts\\4-Narezaem_avatarki\\final.jpg")
final_resized.thumbnail((80, 80))
final_resized.save("C:\\python_scripts\\4-Narezaem_avatarki\\final_resized.jpg")