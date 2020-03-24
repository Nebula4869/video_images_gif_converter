from PIL import Image
import imageio
import os


def gif2images(gif_dir, images_dir):
    """
    Convert .gif file to images.
    :param gif_dir: Path of gif file to be converted
    :param images_dir: Path to the folder holding the images
    :return: None
    """
    if not os.path.exists(gif_dir):
        print('Invalid GIF path!')
        return

    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    im = Image.open(gif_dir)
    while True:
        current = im.tell()
        img = im.convert('RGB')
        img.save(os.path.join(images_dir, str(current + 1) + '.jpg'))
        try:
            im.seek(current + 1)
        except EOFError:
            break


def images2gif(images_dir, gif_name, fps):
    """
    Convert image sequence to a .gif file.
    :param images_dir: Path to the folder holding the images to be converted
    :param gif_name: Name of the gif file
    :param fps: Frame rate of the gif
    :return: None
    """
    if not os.path.exists(images_dir):
        print('Invalid Images path!')
        return

    image_list = os.listdir(images_dir)
    image_list.sort(key=lambda x: int(x[:-4]))

    frames = []

    for image in image_list:
        im_origin = imageio.imread(os.path.join(images_dir, image))
        frames.append(im_origin)

    imageio.mimsave(gif_name + '.gif', frames, 'GIF', duration=1 / fps)


if __name__ == '__main__':
    images2gif('./images', 'convert', fps=30)
    # gif2images('test.gif', './images')
