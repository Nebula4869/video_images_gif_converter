import cv2
import os


def video2images(video_dir, images_dir):
    """
    Convert a video file to images.
    :param video_dir: Path of video file to be converted
    :param images_dir: Path to the folder holding the images
    :return: None
    """
    if not os.path.exists(video_dir):
        print('Invalid Video path!')
        return

    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    cap = cv2.VideoCapture(video_dir)
    cnt = 0
    while True:
        cnt += 1
        _, frame = cap.read()
        if frame is not None:
            cv2.imwrite(os.path.join(images_dir, str(cnt) + '.jpg'), frame)
        else:
            break


def images2video(images_dir, video_name, fps, size):
    """
    Convert image sequence to an MP4 video.
    :param images_dir: Path to the folder holding the images to be converted
    :param video_name: Name of the video file
    :param fps: Frame rate of the video
    :param size: Frame size of the video
    :return: None
    """
    if not os.path.exists(images_dir):
        print('Invalid Images path!')
        return

    image_list = os.listdir(images_dir)
    image_list.sort(key=lambda x: int(x[:-4]))

    videoWriter = cv2.VideoWriter(video_name + '.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

    for image in image_list:
        img = cv2.imread(os.path.join(images_dir, image))
        img = cv2.resize(img, size)
        videoWriter.write(img)

    videoWriter.release()


if __name__ == '__main__':
    video2images('test.mp4', './images')
    # images2video('./images', 'convert', 30, (1920, 1080))
