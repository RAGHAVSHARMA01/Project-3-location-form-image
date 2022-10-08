import PIL.Image  # To open the image, here PILL refers to pillow
import PIL.ExifTags

# from PIL import Image
img = PIL.Image.open("NAME OF THE IMAGE FILE IN THE SAME FOLDER AS THAT OF THIS SOURCE CODE")  # This is where the image is opened

# Now let's get the metadata from the image for the location

exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
}
print(exif) # Here we are taking the  information of the whole matadata but we can specify the things that we want to get information off
print(exif['ExposureTime'])   # For Eg. here we are only taking the information of the Exposure time
