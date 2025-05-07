from PIL import Image, ImageSequence
import os
import time

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=80):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55) 
    return image.resize((new_width, new_height))

def image_to_ascii(image):
    grayscale = image.convert("L")
    pixels = grayscale.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel * len(ASCII_CHARS) // 256] for pixel in pixels)
    return ascii_str

def gif_to_ascii_animation(path, width=80, delay=0.1):
    gif = Image.open(path)
    frames = []
    
    for frame in ImageSequence.Iterator(gif):
        frame = resize_image(frame, new_width=width)
        ascii_frame = image_to_ascii(frame)
        ascii_frame_lines = [
            ascii_frame[i:i+width] for i in range(0, len(ascii_frame), width)
        ]
        frames.append("\n".join(ascii_frame_lines))

    try:
        while True:
            for frame in frames:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(frame)
                time.sleep(delay)
    except KeyboardInterrupt:
        pass

gif_to_ascii_animation("weirdsmiley.gif", width=80, delay=0.1)
