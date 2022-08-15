"""
File: stanCodoshop.py
Name: Abbie Chen
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import math
import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    p_r = pixel.red
    p_g = pixel.green
    p_b = pixel.blue
    dist = math.sqrt((red - p_r)**2 + (green - p_g)**2 + (blue - p_b)**2)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    red_sum = 0
    green_sum = 0
    blue_sum = 0
    for pixel in pixels:
        red_sum += pixel.red
        green_sum += pixel.green
        blue_sum += pixel.blue
    red_avg = int(red_sum/len(pixels))
    green_avg = int(green_sum/len(pixels))
    blue_avg = int(blue_sum/len(pixels))
    rgb = [red_avg, green_avg, blue_avg]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    avg_r = get_average(pixels)[0]
    avg_g = get_average(pixels)[1]
    avg_b = get_average(pixels)[2]
    best_pixel_dis = 0
    best_pixel = 0
    for pixel in pixels:
        dis = get_pixel_dist(pixel, avg_r, avg_g, avg_b)
        if best_pixel_dis == 0:
            best_pixel_dis = dis
            best_pixel = pixel
        else:
            if best_pixel_dis > dis:
                best_pixel_dis = dis
                best_pixel = pixel
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for x in range(images[0].width):
        for y in range(images[0].height):
            pixel_list = []
            for image in images:
                # pixel_list += [image.get_pixel(x, y)]
                pixel_list.append(image.get_pixel(x, y))
            best_pixel = get_best_pixel(pixel_list)
            original = result.get_pixel(x, y)
            original.red = best_pixel.red
            original.blue = best_pixel.blue
            original.green = best_pixel.green
    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
