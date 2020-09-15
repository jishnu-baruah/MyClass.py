class MyObject(object):
    def __init__(self, name, height, width):
        self.name = name
        self.height = height
        self.width = width
        self.area = 0

    def setArea(self, height, width):
        self.area = int(self.height)*int(self.width)

    def getArea(self, area):
        return self.area

    def getDimensions(self):
        dimensions = "name :"+self.name+" ,area :" + \
            str(int(self.height)*int(self.width))+" ,height :"+str(self.height) + \
            " ,width :"+str(self.width)
        return dimensions


newObjectName = input("name : ")
# print(newObjectName)
newObjectWidth = input("width : ")

newObjectHeight = input("height : ")

newObject = MyObject(newObjectName, newObjectWidth, newObjectHeight)
print(newObject.width)

print(newObject.getDimensions())
