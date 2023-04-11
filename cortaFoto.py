import cv2
img = cv2.imread("sprites.png")
row = 30
col = 40
i = 0
for r in range(0,img.shape[0],row):
    for c in range(0,img.shape[1],col):
        cv2.imwrite("sprites/"+str(i)+".png",img[r:r+row, c:c+col,:])
        i+=1