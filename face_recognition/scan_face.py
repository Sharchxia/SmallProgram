import tensorflow as tf
import cv2
import numpy as np

class ScanFace:
    def __init__(self, model_path: str, predict_name: list):
        # print(model_path)
        self.model = tf.keras.models.load_model(model_path)  # 加载模型
        self.capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.xml = cv2.CascadeClassifier('D:/anaconda/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml')
        self.predict_object = predict_name  # 要预测的对象的名字
        self.scan()

    def scan(self):
        while self.capture.isOpened():
            ret, img = self.capture.read()
            if ret:
                img1 = img.copy()
                faces = self.xml.detectMultiScale(img1, 1.15)  # 获取人脸
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)  # 画出人脸识别框
                    face = img1[x-25:x+w+25, y-25:y+h+25]
                    if len(face)>50 and len(face[0])>50:  # 保证获取到的数据可用
                        face = cv2.resize(face, (224, 224))
                        cv2.imshow('Face', face)
                        face = cv2.resize(face, (64, 64))  # 归一化处理
                        face1 = face.copy()
                        face1 = np.array([face1.astype(np.float32)])  # 转换数据类型，符合模型预测的输入数据格式
                        # print(type(face))
                        # print(face.shape)
                        pre = self.model.predict(face1).tolist()[0]
                        # print(pre)
                        predict_name = self.predict_object[pre.index(max(pre))]
                        cv2.putText(img, predict_name, (x-25, y-25), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)  # 将预测好的名字放入图片后续显示
                cv2.imshow('Video', img)

                key = cv2.waitKey(1)  # 等待1ms，主要用于退出的检测
                if key == 32:  # 空格退出
                    self.capture.release()
                    break
        cv2.destroyAllWindows()

if __name__ == '__main__':
    model = 'model.h5'  # 将加载的模型的路径（相对路径）
    predict = ['GZY', 'HKH', 'MQL', 'WRQ', 'WSH', 'XC', 'XCY']  # 将预测的对象的名字
    # predict = ['NEUTRAL']*7
    sc = ScanFace(model, predict)  # 预测
