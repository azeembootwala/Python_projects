import pandas,numpy,cv2
from matplotlib import pyplot as plt
img = cv2.imread("smallgray.png",1)
plt.imshow(img)
plt.show()

for item,i in zip(img,range(0,14)):
    item =255-item
    img[i]=item
cv2.imwrite("modified.png",img)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.show()
