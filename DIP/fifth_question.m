image = imread('rice.bmp');
level = graythresh(image);
BW0 = im2bw(image, level);
BW1 = bwareaopen(BW0, 1000);
subplot(221);imshow(image);title('原图');
subplot(222);imshow(BW0);title('分割原结果');
subplot(223);imshow(BW1);title('筛选结果');

[b,im] = bwboundaries(BW1,4);
subplot(224);imshow(label2rgb(BW1));title('中心和矩形标注');hold on;

center = regionprops(im,'Area','Centroid');
for i = 1:length(b)
    bound = b{i};
    center0 = center(i).Centroid;
    plot(center0(1),center0(2),'.','Color','r');
    a1 = min(bound,[],1);
    a2 = max(bound,[],1);
    rectangle('Position',[a1(2) a1(1) a2(2)-a1(2) a2(1)-a1(1)],'EdgeColor','k');
end
