"Module for comparing pictures"
from pathlib import Path
from PIL import Image
import numpy as np



_DEBUG=True
if _DEBUG:
    from matplotlib import pyplot, image, use, get_backend
    from mpl_toolkits.mplot3d import axes3d

def diff_pic(img1, img2):
    "calculate picture differense as numpy array"
    if _DEBUG:
        for i in img1, img2:
            print("Image1 format", i.format, i.size, i.mode)
            print("absimg1 max", np.max(i), "min", np.min(i))
            print("Background (0,0)", i.getpixel((0,0)))
    if img1.format != img2.format or img1.size != img2.size:
        raise Exception("File have not same format")
    arr1 = np.asarray(img1)
    if _DEBUG:
        pyplot.imshow(arr1, cmap='gray')
        pyplot.show()
    arr2 = np.asarray(img2)
    if _DEBUG:
        pyplot.imshow(arr2, cmap='gray')
        pyplot.show()
    n = arr1 - arr2
    if _DEBUG:
        print("diff max", np.max(n), "min", np.min(n))
        print("mean error", np.mean(np.abs(n)))
        pyplot.imshow(n)
        pyplot.show()
    return n

def show_diff(fil1,fil2):
    img1 = Image.open(fil1)
    img2 = Image.open(fil1)
    res = diff_pic(img1, img2)
    if _DEBUG:
        fig = pyplot.figure(figsize=(5,5))
        ax = fig.add_subplot(222, projection="3d")
        # print (res, res.shape)
        # x = np.array()
        # y = np.array()
        # z = np.array()

        for x in range(160):
            for y in range(160):
                #print(res[x,y])
                ax.scatter(x,y, 10)
        #         y.add(y)
        #         z.add(z)

        #ax.plot_wireframe(x,y,z)
        pyplot.show()
   

def show_pic_diff(file1, file2):
    "Show picture wit difference in pictures"
    img1 = Image.open(file1)
    print("Image1 format", img1.format, img1.size, img1.mode)
    print("absimg1 max", np.max(img1), "min", np.min(img1))
    print("Background (0,0)", img1.getpixel((0,0)))
    arr1 = np.asarray(img1)
    pyplot.imshow(arr1, cmap='gray')
    print("img1 max", np.max(arr1), "min", np.min(arr1))
    pyplot.show()
    img2 = image.imread(file2)
    arr2 = np.asarray(img2)
    print("img2 max", np.max(arr2), "min", np.min(arr2))
    pyplot.imshow(arr2, cmap='gray')
    pyplot.show()
    n = arr1 - arr2
    #print (n)
    print("diff max", np.max(n), "min", np.min(n))
    print("mean error", np.mean(np.abs(n)))
    pyplot.imshow(n, )
    pyplot.show()
    # pyplot.imshow(img2)
    # pyplot.show()

if __name__ == "__main__":
    print("Starting")
    #use('qtagg')
    #print("Matplotlib backend", get_backend())
    PICFOLDER = Path(__file__).parent / 'testpictures/compare/pictures'

    print("Compare wrapped image")
    file1 = PICFOLDER / "analytic/analog_im_wrap1.png"
    file2 = PICFOLDER / "inf/wrap.png"
    show_diff(file1, file2)






#     return
# print("K")
# PICFOLDER = Path(__file__).parent / 'testpictures/compare/pictures'
# file = PICFOLDER / "analytic/kdata.png"
# file2 = "pictures/inf/nnk.png"

# print(file)
# show_pic_diff(file, file2)

# print("unwrapped")
# file = "pictures/analytic/unwrap.png"
# file2 = "pictures/inf/unwrap.png"
# show_diff(file, file2)

# show_diff(file, file2)
