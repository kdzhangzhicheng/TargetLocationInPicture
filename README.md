# TargetLocationInPicture
Use SIFT to locate target in the picture


# How to use 
In Terminal input

python ZZC_ObjDet.py src1.jpg target1.png target2.png target3.png target4.png

`src1.jpg is the source picture, target 1-5 are target picture`

`We use the SIFT to calculate the confidence of target picutre in the
source picture, and we use the max`

#  important Pip list
opencv-contrib-python==3.2.0.7
aircv==1.4.6
`Do not import opencv-python`
