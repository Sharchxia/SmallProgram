image = imread('rice.bmp');
base = strel('octagon', 30);
figure('NumberTitle','off','MenuBar','none','Name','��ñ�任ԭͼ�����','color','g');
subplot(1,3,1);imshow(image);title('ԭͼ');
image_1 = imopen(image,base);
subplot(1,3,2);imshow(image_1);title('��������ͼ��');
image_2 = image-image_1;
subplot(1,3,3);imshow(image_2);title('�任��ͼ��');