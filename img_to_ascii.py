import PIL.Image

# ascii characters
ASCII_CHARS = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]

# pass the image as command line argument
# image_path = sys.argv[1]
# new_width = 360

# resize the image
def resize_img(img, new_width):
    width, height = img.size
    aspect_ratio = height/width

    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    return img

# convert image to greyscale format
def grayify(img):
    img = img.convert('L')
    return img

# replace each pixel with a character from array
def px_to_ascii(img):
    pixels = img.getdata()
    new_pixels = [ASCII_CHARS[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    return new_pixels

# write to a text file.
def save(img, filename):
    file_path = "./tmp/ascii_frames/" + filename + ".txt"
    with open(file_path, "w") as f:
        f.write(img)

def img_to_ascii(image_path, filename, new_width):
    try:
        image = PIL.Image.open(image_path)
    except:
        print(image_path, " isn't valid")

    resized_img = resize_img(image, new_width)
    gray_img = grayify(resized_img)
    new_pixels = px_to_ascii(gray_img)

    # split string of chars into multiple strings of length equal to new width and create a list
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    save(ascii_image, filename)
    # print(ascii_image)
 
# img_to_ascii('./frames/1.jpg', '1', 480) # Test