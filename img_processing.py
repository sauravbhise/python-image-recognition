from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
panelA = None
panelB = None
panelC = None
panelD = None


def select_image():
    # grab a reference to the image panels
    global panelA, panelB, panelC, panelD
    # open a file chooser dialog and allow the user to select an input image

    path = filedialog.askopenfilename()
# ensure a file path was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale, and detect edges in it
        face_Cascade = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')

        image = cv2.imread(path)
        imageDetected = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 100)

        faces = face_Cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(imageDetected, (x, y),
                          (x + w, y + h), (255, 0, 0), 2)

        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        imageDetected = cv2.cvtColor(imageDetected, cv2.COLOR_BGR2RGB)
        # convert the images to PIL format...
        image = Image.fromarray(image)
        gray = Image.fromarray(gray)
        edged = Image.fromarray(edged)
        detected = Image.fromarray(imageDetected)
        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        gray = ImageTk.PhotoImage(gray)
        edged = ImageTk.PhotoImage(edged)
        detected = ImageTk.PhotoImage(detected)

# if the panels are None, initialize them
    if panelA is None or panelB is None or panelC is None or panelD is None:
        # the first panel will store our original image
        panelA = Label(image=image)
        panelA.image = image
        panelA.pack(side="left", padx=10, pady=10)
    # while the second panel will store the edge map
        panelB = Label(image=edged)
        panelB.image = edged
        panelB.pack(side="right", padx=10, pady=10)

        panelC = Label(image=gray)
        panelC.image = gray
        panelC.pack(side=BOTTOM, padx=10, pady=10)
    # otherwise, update the image panels
        panelD = Label(image=detected)
        panelD.image = detected
        panelD.pack(side=TOP, padx=10, pady=10)
    else:
        # update the panels
        panelA.configure(image=image)
        panelB.configure(image=edged)
        panelC.configure(image=gray)
        panelD.configure(image=detected)
        panelA.image = image
        panelB.image = edged
        panelC.image = gray
        panelD.image = detected


# initialize the window toolkit along with the two image panels
root = Tk()

# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="100", pady="100")
# kick off the GUI
root.mainloop()
