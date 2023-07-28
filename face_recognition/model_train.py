import os
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, MaxPooling2D, Conv2D
import matplotlib.pyplot as plt


class Model:
    def __init__(self, train_data, val_data, classes: int, batch_size=30, epochs=3, filepath='model1'):  # 创建模型
        if not os.path.exists(filepath):  # 模型文件保存文件夹，如果没有就创建
            os.makedirs(filepath)

        self.epochs = epochs  # 迭代次数
        self.batch_size = batch_size  # 每次训练的图片批数
        self.classes = classes  # 分类的类数
        self.train_data = train_data  # 训练数据
        self.val_data = val_data  # 验证数据
        self.save_path = filepath  # 保存路径
        self.model = self.model_generate()  # 构成模型
        self.history = self.train().history  # 获得History对象，方便得到训练历史数据

    def model_generate(self):
        model = Sequential()
        # model.add(Conv2D(64, (3, 3), input_shape=(224, 224, 3), activation='relu',padding='same'))
        model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu', padding='same'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.5))

        # model.add(Conv2D(128, (3, 3), activation='relu',padding='same'))
        model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.5))

        # model.add(Conv2D(256, (3, 3),activation='relu',padding='same'))
        model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.5))

        # model.add(Conv2D(512, (3, 3), activation='relu',padding='same'))
        # model.add(Conv2D(512, (3, 3), activation='relu', padding='same'))
        # model.add(MaxPooling2D(pool_size=(2, 2)))
        # model.add(Dropout(0.5))

        # model.add(Conv2D(512, (3, 3), activation='relu',padding='same'))
        # model.add(Conv2D(512, (3, 3), activation='relu', padding='same'))
        # model.add(MaxPooling2D(pool_size=(2, 2)))
        # model.add(Dropout(0.2))

        model.add(Flatten())

        # model.add(Dense(4096, activation='relu'))
        # model.add(Dropout(0.5))

        model.add(Dense(512, activation='relu'))
        # model.add(Dropout(0.25))

        model.add(Dense(self.classes, activation="softmax"))
        model.compile(loss=tf.keras.losses.categorical_crossentropy, optimizer=tf.keras.optimizers.Adam(),
                      metrics=['accuracy'])
        return model

    def train(self):
        return self.model.fit(self.train_data, batch_size=self.batch_size, epochs=self.epochs, validation_data=self.val_data)

    def save_model(self, model_path=None):
        if model_path is None:
            self.model.save(self.save_path)
            self.model.save(self.save_path+'.h5')
        else:
            self.model.save(model_path)
            self.model.save(str(model_path)+ '.h5')

    def plot(self):  # 画出4张相关的数据与迭代次数的相关联的图像
        loss = self.history['loss']
        acc = self.history['accuracy']
        val_loss = self.history['val_loss']
        val_acc = self.history['val_accuracy']
        plt.subplot(2,2,1)
        plt.plot(acc, marker='*')
        plt.title('train_acc')
        plt.subplot(2, 2, 2)
        plt.plot(loss, marker='*')
        plt.title('train_loss')
        plt.subplot(2, 2, 3)
        plt.plot(val_acc, marker='*')
        plt.title('val_acc')
        plt.subplot(2, 2, 4)
        plt.plot(val_loss, marker='*')
        plt.title('val_loss')
        plt.show()


class Train:  # 训练对象
    def __init__(self, train_position='dataset', val_position='valset', batch_size=30, epochs=3, model_path='model'):
        self.train_position = train_position
        self.val_position = val_position
        self.parts = os.listdir(train_position)
        self.batch_size = batch_size
        self.classes = len(self.parts)
        train_generator = ImageDataGenerator()  # 实例化对象，方便后续处理数据
        val_generator = ImageDataGenerator()
        self.val_data = val_generator.flow_from_directory(directory=val_position, target_size=(64, 64), batch_size=batch_size)
        self.train_data = train_generator.flow_from_directory(directory=train_position, target_size=(64, 64), batch_size=batch_size)
        self.model = Model(self.train_data, self.val_data, classes=self.classes, epochs=epochs, filepath=model_path)


if __name__ == "__main__":
    bs = 120  # batch_size 每批次训练的图片张数
    ep = 80  # 迭代次数
    train_path = 'dataset'  # 训练集的路径（相对路径）
    val_path = 'valset'  # 验证集路径
    model_path = 'model'  # 训练后模型保存位置（相对路径）
    tr = Train(train_path, val_path, bs, ep, model_path=model_path)
    # tr.model.plot()  # 画出4张分析图
    # tr.model.save_model()  # 保存模型
