image = imread('lena.bmp');
image_gaussian = imnoise(image, 'gaussian');
image_poisson = imnoise(image, 'poisson');
image_salt = imnoise(image, 'salt & pepper');
figure('NumberTitle','off','MenuBar','none','Name','���뼰�˲����ͼ��','color','g');
subplot(3,3,1);imshow(image_gaussian);title('��˹����');
subplot(3,3,2);imshow(image_poisson);title('��������');
subplot(3,3,3);imshow(image_salt);title('��������');
I_g = im2double(image_gaussian);
I_g = fftshift(fft2(I_g));
subplot(3,3,4);imshow(log(abs(I_g)+1),[]);title('��˹����Ƶ��');
I_p = im2double(image_poisson);
I_p = fftshift(fft2(I_p));
subplot(3,3,5);imshow(log(abs(I_p)+1),[]);title('���ɸ���Ƶ��');
I_s = im2double(image_salt);
I_s = fftshift(fft2(I_s));
subplot(3,3,6);imshow(log(abs(I_s)+1),[]);title('���θ���Ƶ��');

d=90; %�뾶(��ֹƵ��)

[a,b]=size(I_g);
h=zeros(a,b);
a0=round(a/2);
b0=round(b/2);
for i=1:a 
    for j=1:b 
        distance=sqrt((i-a0)^2+(j-b0)^2);
        if distance<=d
            h(i,j)=1;
        else
            h(i,j)=0;
        end
    end
end
res=I_g.*h;
res=real(ifft2(ifftshift(res)));
subplot(3,3,7);imshow(res);title('�˲����1');

[a,b]=size(I_p);
h=zeros(a,b);
a0=round(a/2);
b0=round(b/2);
for i=1:a 
    for j=1:b 
        distance=sqrt((i-a0)^2+(j-b0)^2);
        if distance<=d
            h(i,j)=1;
        else
            h(i,j)=0;
        end
    end
end
res=I_p.*h;
res=real(ifft2(ifftshift(res)));
subplot(3,3,8);imshow(res);title('�˲����2');

[a,b]=size(I_s);
h=zeros(a,b);
a0=round(a/2);
b0=round(b/2);
for i=1:a 
    for j=1:b 
        distance=sqrt((i-a0)^2+(j-b0)^2);
        if distance<=d
            h(i,j)=1;
        else
            h(i,j)=0;
        end
    end
end
res=I_s.*h;
res=real(ifft2(ifftshift(res)));
subplot(3,3,9);imshow(res);title('�˲����3');