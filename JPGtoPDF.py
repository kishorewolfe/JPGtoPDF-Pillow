from PIL import Image
image1=Image.open('image1.png')
image2=Image.open('image1.png')
image3=Image.open('image1.png')
image4=Image.open('image1.png')
imglist=[image2,image3,image4]
image1.save("multiple.pdf",save_all=True,append_images=imglist)