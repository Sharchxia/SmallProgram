import cv2
import os

POSITION = "dataset"  # 文件保存位置的主文件夹
NAME = 'XCY'  # 文件归类的子文件夹，储存一个人的相关照片
NUMBER = 2000  # 获得数据张数


class GetFace:  # 获得人脸
    def __init__(self, name: str, number=2000, position='dataset'):
        self.position = position + '/'+ name
        self.number = number
        self.name = name
        self.model = cv2.CascadeClassifier('D:/anaconda/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml')  # 选取的级联分类器，这里是绝对路径
        if not os.path.exists(self.position):
            os.makedirs(self.position)  # 创建数据的保存文件夹

    def rename(self, name: str):
        self.name = name  # 更改数据文件夹名称

    def re_position(self, position):
        self.position = position + '/'+ self.name  # 更改数据保存位置

    def change_size(self, number):  # 更改数据获取张数
        self.number = number

    def run(self):
        # cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
        # cv2.namedWindow('Face', cv2.WINDOW_NORMAL)
        capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        count = len(os.listdir(self.position))

        while capture.isOpened() and self.number>count:
            ret, img = capture.read()
            if ret:
                image = img.copy()
                faces = self.model.detectMultiScale(image, 1.5)
                for (x, y, w, h) in faces:
                    face = image[x-25:x+w+25, y-25:y+h+25]
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)
                    if len(face):  # 如果检测到有效的人脸，则进行相关处理保存操作
                        cv2.imshow('Face', face)
                        filename = self.position+'/'+str('{:04d}'.format(count))+'.jpg'  # 保存格式为jpg
                        face = cv2.resize(face, (224, 224))
                        cv2.imwrite(filename, face)
                        count += 1
                cv2.putText(img, str(count), (50, 50), cv2.FONT_HERSHEY_DUPLEX, 2.0, (0, 0, 255), 5)  # 在摄像头获得的图片上打印出已获得的张数，不会影响要保存的数据
                cv2.imshow('Video', img)

            key = cv2.waitKey(1)
            if key == 32:  # 按空格关闭摄像头退出获取
                capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    my = GetFace(NAME, position=POSITION, number=NUMBER)
    my.run()
