#test program for QRCodeGenerator
#run this after installing requirements.txt
from QRCode import  QRCodeGenerator as Q
data = input("enter your data:\n")
#print("your data : " + data)

q = Q()

q.encode(data, "out.png")

output = q.decode("out.png")
q.writeToFile(output,"output","txt")
#print(output)
