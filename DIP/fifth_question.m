image = imread('rice.bmp');
level = graythresh(image);
BW0 = im2bw(image, level);
BW1 = bwareaopen(BW0, 1000);
subplot(221);imshow(image);title('ԭͼ');
subplot(222);imshow(BW0);title('�ָ�ԭ���');
subplot(223);imshow(BW1);title('ɸѡ���');

[b,im] = bwboundaries(BW1,4);
subplot(224);imshow(label2rgb(BW1));title('���ĺ;��α�ע');hold on;

center = regionprops(im,'Area','Centroid');
for i = 1:length(b)
    bound = b{i};
    center0 = center(i).Centroid;
    plot(center0(1),center0(2),'.','Color','r');
    a1 = min(bound,[],1);
    a2 = max(bound,[],1);
    rectangle('Position',[a1(2) a1(1) a2(2)-a1(2) a2(1)-a1(1)],'EdgeColor','k');
end
