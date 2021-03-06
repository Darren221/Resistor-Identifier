from resReader import *
from resFinder import *
import numpy as np
import cv2
# import sys
# sys.path.append('/usr/local/lib/python3.7/site-packages')

CASCADE_PATH = './model/cascade.xml'

def main():

    cap = cv2.VideoCapture(0)
    # cap.set(28,255)
    # cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)
    
    finder = resFinder(CASCADE_PATH)
    reader = resReader()
    last = dict()
    while not cv2.waitKey(1) & 0xFF == ord('q'):
        curr = dict()
        ret, frame = cap.read()
        res = finder.find_res(frame)

        for (x, y, w, h) in res:
            
            y, h = y+h//4, h//2
            # print(f'{x}, {y}, {w}, {h}')
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)


            reader.read_img(frame[y:y+h, x:x+w])
            sorted_band = reader.read_band()
            result = reader.read_value(sorted_band, frame)

            
            for (xl, yl) in last.keys():
                if (xl-x)**2+(yl-y)**2 < 100 and result == '':
                    result = last[(xl, yl)]

            curr[(x,y)] = result

            cv2.putText(frame, result, (x, y-10), FONT, 1, (255,0,0),2 ,cv2.LINE_AA)

        last = curr
        cv2.imshow('frame', frame)


    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
