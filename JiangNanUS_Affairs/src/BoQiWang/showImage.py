from PIL import Image
import matplotlib.pyplot as plt
img=Image.open('vcode.png')
plt.figure("dog")
plt.imshow(img)
plt.show()