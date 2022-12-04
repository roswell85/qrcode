#test program for QRCodeGenerator
#run this after installing requirements.txt
from QRCode import  QRCodeGenerator as Q
data = "My Data 1234"

q = Q()

q.encode(data, "out.png")

output = q.decode("out.png")


