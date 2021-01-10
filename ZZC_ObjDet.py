

import sys
import cv2
import aircv as ac



def draw_dot(img, pos):
    pos=list(pos)
    pos[0]=int(pos[0])
    pos[1]=int(pos[1])
    pos=tuple(pos)
    cv2.circle(img, pos, 5, (0, 255, 0), 5)
    cv2.imshow('objDetect', imsrc)
    cv2.waitKey(500)  # wait for 500ms

    cv2.imwrite('DetecImg.png', imsrc)

if __name__ == "__main__":
    InputImg1 = sys.argv[1]  # source.jpg

    InputImg2 = sys.argv[2]  # target.jpg
    InputImg3 = sys.argv[3]
    InputImg4 = sys.argv[4]
    InputImg5 = sys.argv[5]

    imsrc = ac.imread(InputImg1)
    imtarget1 = ac.imread(InputImg2)
    imtarget2 = ac.imread(InputImg3)
    imtarget3 = ac.imread(InputImg4)
    imtarget4 = ac.imread(InputImg5)

    # find the match position

    pos1 = ac.find_all_sift(imsrc,imtarget1)
    pos2 = ac.find_all_sift(imsrc,imtarget2)
    pos3 = ac.find_all_sift(imsrc,imtarget3)
    pos4 = ac.find_all_sift(imsrc,imtarget4)

    l1=[]
    
    l2=[]
    l2.append(pos1[0].get('result'))
    l2.append(pos2[0].get('result'))
    l2.append(pos3[0].get('result'))
    l2.append(pos4[0].get('result'))



    l1.append(pos1[0].get('confidence')[0]/pos1[0].get('confidence')[1])
    l1.append(pos2[0].get('confidence')[0]/pos2[0].get('confidence')[1])
    l1.append(pos3[0].get('confidence')[0]/pos3[0].get('confidence')[1])
    l1.append(pos4[0].get('confidence')[0]/pos4[0].get('confidence')[1])


    
    temp=l1[0]
    pos = 0
    for i in range(len(l1)):
        if temp < l1[i]:
            temp = l1[i]
            pos = i

    draw_dot(imsrc,l2[pos])


