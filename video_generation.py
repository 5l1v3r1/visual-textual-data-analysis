import cv2
import pandas as pd
import sys
import os
import glob

#input_data_file = 'test_data.csv'
#input_video_file = '/Users/mayanksaxena/Desktop/gesture-analysis/videos/bicycle.avi'
#input_data_file = sys.argv[1]
#input_video_file = sys.argv[2]

df = pd.DataFrame()

def read_from_input_data_file(input_data_file):
    df = pd.read_csv(input_data_file)
    #df.head(5)
    x = df['CURRENT_FIX_X']
    y = df['CURRENT_FIX_Y']
    return x, y

def process_input_video_to_frames(x, y, input_video_file):
    vidcap = cv2.VideoCapture(input_video_file)
    success,image = vidcap.read()
    print('success', success)
    count = 0

    i = 0
    while success:
        success,image = vidcap.read()
        #print('Read a new frame: ', success)
        count += 1
        if (count % 10 == 0):
            if (i < 888):
                i += 1
                print('count', count)
                print('i', i)
                x_coord = int(x[i])
                y_coord = int(y[i])
                z =(x_coord,y_coord)
                cv2.circle(image, z, 5, (0,0,255), -1)
                #cv2.imwrite("processed-videos/bicycle/frame%d.jpg" % i, image)
                cv2.imwrite("temp/frame%d.jpg" % i, image)

            #x_coord = int(x[i])
            #y_coord = int(y[i])
            #z =(x_coord,y_coord)
            #cv2.circle(image, z, 5, (0,0,255), -1)
            #x_coord = int(x[i])
            #y_coord = int(y[i])
            #z =(x_coord,y_coord)
            #cv2.circle(image, z, 5, (0,0,255), -1)
            #cv2.imwrite("processed-videos/bicycle/frame%d.jpg" % i, image)
            #cv2.imwrite("temp/frame%d.jpg" % i, image)

    print('final count', count)
    print('final i', i)


def add_in_slide_column(x, y, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
    in_slide = []
    for i in range(len(x)):
        x_coord = int(x[i])
        y_coord = int(y[i])

        if ((top_left_x <= x_coord <= bottom_right_x) and (top_left_y <= y_coord <= bottom_right_y)):
        # Point is within the slide
            in_slide.append(1)
        else:
            in_slide.append(0)

    df['in_slide'] = in_slide
    df.to_csv('temp/test_data_with_in_slide.csv')

def add_in_image_area_column(x, y, image_top_x, image_top_y, image_bottom_x, image_bottom_y):
    in_image = []
    in_text = []
    in_slide = df['in_slide']
    for i in range(len(x)):
        x_coord = int(x[i])
        y_coord = int(y[i])

        if ((image_top_x <= x_coord <= image_bottom_x) and (image_top_y <= y_coord <= image_right_y)):
        # Point is within the slide
            in_image.append(1)
            in_text.append(0)
        else:
            if (in_slide[i] == 1):
                in_text.append(1)
                in_image.append(0)
            else:
                in_text.append(0)
                in_image.append(0)

    df['in_image'] = in_image
    df['in_text'] = in_text
    df.to_csv('temp/test_data_with_in_slide.csv')

def convert_frames_to_video(images_path, output_video_name):
    print('in this function')
    image_folder = images_path
    video_name = 'temp/' + output_video_name
    print('video name', video_name)

    #images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    #images = sorted(img for img in glob.glob(image_folder + '*.jpg'))
    #images.sort()
    images = []
    for i in range(1, 888):
        s = 'frame' + str(i) + '.jpg'
        images.append(s)
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    print('images', images)

    #video = cv2.VideoWriter(video_name, -1, 1, (width,height))
    video = cv2.VideoWriter(video_name,cv2.VideoWriter_fourcc('M','J','P','G'), 3, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

def main():
    input_data_file = sys.argv[1]
    input_video_file = sys.argv[2]
    output_video_name = sys.argv[3]
    images_path = 'temp/'

    #Defined coordinates for slide in bicycle video
    top_left_x = 233
    top_left_y = 74
    bottom_right_x = 830
    bottom_right_y = 414

    x, y = read_from_input_data_file(input_data_file)
    process_input_video_to_frames(x, y, input_video_file)
    add_in_slide_column(x,y, top_left_x, top_left_y, bottom_right_x, bottom_right_y)
    convert_frames_to_video(images_path, output_video_name)

if __name__ == '__main__':
    # Argument 1: input_data_file path
    # Argument 2: input_video_file_path
    # Argument 3: output_video_name
    main()
