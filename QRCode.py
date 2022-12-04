# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys, qrcode
import cv2
class QRCodeGenerator:

    def encode(self,data,filename):
        # Encoding data using make() function
        img = qrcode.make(data)
        # Saving as an image file
        img.save(filename)

    def decode(self,filename):
        # Name of the QR Code Image file

        # read the QRCODE image
        image = cv2.imread(filename)

        # initialize the cv2 QRCode detector
        detector = cv2.QRCodeDetector()

        # detect and decode
        data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

        # if there is a QR code
        # print the data
        if vertices_array is not None:
            print("QRCode data:")
            print(data)
            return data
        else:
            print("There was some error")
            return None






