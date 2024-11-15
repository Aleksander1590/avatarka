from PIL import Image
image = Image.open("example.jpg")
rgb_image = image.convert("RGB")
(red, green, blue) = rgb_image.split()

image1 = red
displacement_value1 = 50
coordinates1 = (displacement_value1, 0, 417, 417)
cropped1 = image1.crop(coordinates1)
image2 = red
displacement_value2 = displacement_value1 / 2
displacement_value3 = 417 - displacement_value2
coordinates2 = (displacement_value2, 0, displacement_value3, 417)
cropped2 = image2.crop(coordinates2)
blend_displacement1 = Image.blend(cropped1, cropped2, 0.9)

image3 = blue
coordinates3 = (displacement_value2, 0, displacement_value3, 417)
cropped3 = image3.crop(coordinates3)
image4 = blue
coordinates4 = (displacement_value1, 0, 417, 417)
cropped4 = image4.crop(coordinates4)
blend_displacement2 = Image.blend(cropped3, cropped4, 0.1)

image5 = green
coordinates5 = (displacement_value2, 0, displacement_value3, 417)
cropped5 = image5.crop(coordinates5)

merge_image = Image.merge("RGB", (blend_displacement1, cropped5, blend_displacement2))
merge_image.save("final.jpg")
final_resized = Image.open("final.jpg")
final_resized.thumbnail((80, 80))
final_resized.save("final_resized.jpg")
