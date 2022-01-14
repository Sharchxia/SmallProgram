image = imread('bank.bmp');
figure('NumberTitle', 'off', 'MenuBar', 'none', 'Name', '直线检测及过程中的其他图像');
BW = edge(image, 'canny');
subplot(251);imshow(image);title('原图像');
subplot(252);imshow(BW);title('边缘检测后图像');
[H, theta, rho] = hough(BW);
subplot(2,5,[3,8]);imshow(imadjust(mat2gray(H)),'DisplayRange',[],'XData',theta,'YData',rho,'InitialMagnification','fit');
title('参数空间中的图像');xlabel('theta (degrees)'); ylabel('rho');
P = houghpeaks(H,10,'threshold', ceil(0.3*max(H(:))));
x=theta(P(:,2)); y=rho(P(:,1));
subplot(2,5,[6 7]);plot(x,y,'*','color','g');title('10个峰值点的');xlabel('theta');ylabel('rho');
lines = houghlines(BW, theta, rho, P, 'FillGap', 10, 'MinLength', 10);
subplot(2,5,4);imshow(image);title('最小长度10,缝合长度10');hold on;
for k = 1 : length(lines)
    xy = [lines(k).point1; lines(k).point2];
    plot(xy(:,1),xy(:,2),'LineWidth',2,'Color','g');
    plot(xy(1,1),xy(1,2),'*','Color','r');
    plot(xy(2,1),xy(2,2),'*','Color','r');
end

lines = houghlines(BW, theta, rho, P, 'FillGap', 10, 'MinLength', 30);
subplot(2,5,5);imshow(image);title('最小长度30,缝合长度10');hold on;
for k = 1 : length(lines)
    xy = [lines(k).point1; lines(k).point2];
    plot(xy(:,1),xy(:,2),'LineWidth',2,'Color','g');
    plot(xy(1,1),xy(1,2),'*','Color','r');
    plot(xy(2,1),xy(2,2),'*','Color','r');
end

lines = houghlines(BW, theta, rho, P, 'FillGap', 40, 'MinLength', 10);
subplot(2,5,9);imshow(image);title('最小长度10,缝合长度40');hold on;
for k = 1 : length(lines)
    xy = [lines(k).point1; lines(k).point2];
    plot(xy(:,1),xy(:,2),'LineWidth',2,'Color','g');
    plot(xy(1,1),xy(1,2),'*','Color','r');
    plot(xy(2,1),xy(2,2),'*','Color','r');
end

lines = houghlines(BW, theta, rho, P, 'FillGap', 40, 'MinLength', 30);
subplot(2,5,10);imshow(image);title('最小长度30,缝合长度40');hold on;
for k = 1 : length(lines)
    xy = [lines(k).point1; lines(k).point2];
    plot(xy(:,1),xy(:,2),'LineWidth',2,'Color','g');
    plot(xy(1,1),xy(1,2),'*','Color','r');
    plot(xy(2,1),xy(2,2),'*','Color','r');
end