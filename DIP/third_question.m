image = imread('rice.bmp');
base = strel('octagon', 30);
figure('NumberTitle','off','MenuBar','none','Name','顶帽变换原图及结果','color','g');
subplot(1,3,1);imshow(image);title('原图');
image_1 = imopen(image,base);
subplot(1,3,2);imshow(image_1);title('开操作后图像');
image_2 = image-image_1;
subplot(1,3,3);imshow(image_2);title('变换后图像');