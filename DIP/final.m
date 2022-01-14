function varargout = final(varargin)
% FINAL MATLAB code for final.fig
%      FINAL, by itself, creates a new FINAL or raises the existing
%      singleton*.
%
%      H = FINAL returns the handle to a new FINAL or the handle to
%      the existing singleton*.
%
%      FINAL('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in FINAL.M with the given input arguments.
%
%      FINAL('Property','Value',...) creates a new FINAL or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before final_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to final_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help final

% Last Modified by GUIDE v2.5 28-Nov-2021 01:13:40

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @final_OpeningFcn, ...
                   'gui_OutputFcn',  @final_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before final is made visible.
function final_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to final (see VARARGIN)

% Choose default command line output for final
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes final wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = final_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double
global gray_str; global noise_str;global fliter_str;global style_str;
value = str2num(get(handles.edit1,'string'));
if value<1
    value = 1;
elseif value>255
     value=255;
end
% set(handles.edit1,'string',num2str(value));
set(handles.slider1,'value',value);
set(handles.edit1,'string',num2str(value));
if value>=2
gray_str=['灰度级' num2str(value) ' '];
else
    gray_str='不进行直方图均衡化 ';
end
old_str = get(handles.edit3,'string');
set(handles.edit3,'string',char(old_str, [gray_str noise_str fliter_str style_str] ));
set(handles.edit3,'ListboxTop',get(handles.edit3,'ListboxTop')+1);



% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on slider movement.
function slider1_Callback(hObject, eventdata, handles)
% hObject    handle to slider1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
global gray_str; global noise_str;global fliter_str;global style_str;
value = round(get(handles.slider1,'value'));
set(handles.edit1,'string',num2str(value));
if value>=2
gray_str=['灰度级' num2str(value) ' '];
else
    gray_str='不进行直方图均衡化 ';
end
old_str = get(handles.edit3,'string');
set(handles.edit3,'string',char(old_str, [gray_str noise_str fliter_str style_str] ));
set(handles.edit3,'ListboxTop',get(handles.edit3,'ListboxTop')+1);


% --- Executes during object creation, after setting all properties.
function slider1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to slider1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end
handles.noise = 0;
guidata(hObject,handles);
handles.fliter = 0;
guidata(hObject,handles);
handles.style = 0;
guidata(hObject,handles);
handles.have_im1 = 0;
guidata(hObject,handles);
handles.have_im = 0;
guidata(hObject,handles);
global gray_str; global noise_str;global fliter_str;global style_str;
gray_str = '不进行直方图均衡化 ';noise_str='无噪声加入 ';fliter_str='无滤波器使用 ';style_str=' 无形态操作 ';



% --- Executes on selection change in fliter_box.
function fliter_box_Callback(hObject, eventdata, handles)
% hObject    handle to fliter_box (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns fliter_box contents as cell array
%        contents{get(hObject,'Value')} returns selected item from fliter_box
global gray_str; global noise_str;global fliter_str;global style_str;
fliter = get(hObject,'value')-1;
%str = get(hObject,'string');
fliter_f = get(handles.edit2,'string');
%fliter_str = str(fliter_box+1);
set(handles.edit2,'Enable','on');
switch fliter
    case 0
        fliter_str = '无滤波器使用 ';
        set(handles.edit2,'Enable','inactive');
        set(handles.edit2,'string','40');
    case 1
        fliter_str = ['理想低通使用 ' '截止频率' fliter_f];
    case 2
        fliter_str = ['理想高通使用 ' '截止频率' fliter_f];
    case 3
        fliter_str = ['高斯低通使用 '  '截止频率' fliter_f];
    case 4
        fliter_str = ['高斯高通使用 ' '截止频率' fliter_f];
    case 5
        fliter_str = ['巴特沃斯低通使用 ' '截止频率' fliter_f];
    case 6
        fliter_str = ['巴特沃斯高通使用 ' '截止频率' fliter_f];
end
old_str = get(handles.edit3,'string');
handles.fliter = fliter;
guidata(hObject,handles);
set(handles.edit3,'string',char(old_str, [gray_str noise_str fliter_str style_str] ));
set(handles.edit3,'ListboxTop',get(handles.edit3,'ListboxTop')+1);



% --- Executes during object creation, after setting all properties.
function fliter_box_CreateFcn(hObject, eventdata, handles)
% hObject    handle to fliter_box (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double
global gray_str; global noise_str;global fliter_str;global style_str;
fliter = get(handles.fliter_box,'value')-1;
fliter_f = get(hObject,'string');
switch fliter
    case 0
        fliter_str = '无滤波器使用 ';
    case 1
        fliter_str = ['理想低通使用 ' '截止频率' fliter_f];
    case 2
        fliter_str = ['理想高通使用 ' '截止频率' fliter_f];
    case 3
        fliter_str = ['高斯低通使用 '  '截止频率' fliter_f];
    case 4
        fliter_str = ['高斯高通使用 ' '截止频率' fliter_f];
    case 5
        fliter_str = ['巴特沃斯低通使用 ' '截止频率' fliter_f];
    case 6
        fliter_str = ['巴特沃斯高通使用 ' '截止频率' fliter_f];
end
old_str = get(handles.edit3,'string');
handles.fliter = fliter;
guidata(hObject,handles);
set(handles.edit3,'string',char(old_str, [gray_str noise_str fliter_str style_str] ));
set(handles.edit3,'ListboxTop',get(handles.edit3,'ListboxTop')+1);




% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in guass.
function guass_Callback(hObject, eventdata, handles)
% hObject    handle to guass (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of guass


% --- Executes on button press in poss.
function poss_Callback(hObject, eventdata, handles)
% hObject    handle to poss (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of poss


% --- Executes on button press in salt.
function salt_Callback(hObject, eventdata, handles)
% hObject    handle to salt (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of salt


% --- Executes on button press in gauss.
function gauss_Callback(hObject, eventdata, handles)
% hObject    handle to gauss (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of gauss


% --- Executes during object creation, after setting all properties.
function axes1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to axes1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called
set(hObject,'XColor','w') ;% 这两行代码功能：将坐标轴和坐标刻度转为白色
set(hObject,'YColor','w');
 
set(hObject,'XTickLabel',[]); % 这两行代码功能：去除坐标刻度
set(hObject,'YTickLabel',[]);

% Hint: place code in OpeningFcn to populate axes1


% --- Executes during object creation, after setting all properties.
function axes2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to axes2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called
set(hObject,'XColor','w') ;% 这两行代码功能：将坐标轴和坐标刻度转为白色
set(hObject,'YColor','w');
 
set(hObject,'XTickLabel',[]); % 这两行代码功能：去除坐标刻度
set(hObject,'YTickLabel',[]);

% Hint: place code in OpeningFcn to populate axes2


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.have_im
axes(handles.axes2);
im1 = handles.im;
n = round(get(handles.slider1,'value'));
if n>1
im1 = histeq(im1,n);
end

noise = handles.noise;
switch noise
    case 1
        im1 = imnoise(im1,'poisson');
    case 2
        im1 = imnoise(im1,'salt & pepper');
    case 3
        im1 = imnoise(im1,'gaussian');
    otherwise
end

fliter = handles.fliter;
fliter_f = round(str2num(get(handles.edit2,'string')));
if fliter>0&&fliter<=6
I = im2double(im1);
s = fftshift(fft2(I));
[a,b]=size(s);
h=zeros(a,b);%滤波器函数
res=zeros(a,b);%保存结果
a0=round(a/2);
b0=round(b/2);
for i=1:a 
      for j=1:b 
            distance=sqrt((i-a0)^2+(j-b0)^2);
             switch fliter
                 case 1
                     if distance<=fliter_f
                        h(i,j)=1;
                     else
                        h(i,j)=0;
                     end
                 case 2
                     if distance<fliter_f
                        h(i,j)=0;
                     else
                        h(i,j)=1;
                     end
                 case 3
                     h(i,j)=exp(-distance/(2*fliter_f^2));
                 case 4
                     h(i,j)=1-exp(-distance/(2*fliter_f^2));
                 case 5
                     n_0 = 2;
                     h(i,j)=1/(1+(distance/fliter_f)^(2*n_0));
                 case 6
                     n_0 = 2;
                     h(i,j)=1/(1+(fliter_f/distance)^(2*n_0));
             end
      end
end
res=s.*h;
im1=real(ifft2(ifftshift(res)));
end

style=handles.style;
se = strel('octagon', 30);
switch style
    case 1
        im2=imclose(im1,se);
        im1=im1-im2;
    case 2
        im1=imopen(im1,se);
    case 3
        im2=imopen(im1,se);
        im1=im1-im2;
    case 4
        im1=imclose(im1,se);
    otherwise
end

imshow(im1);
handles.have_im1 = 1;
guidata(hObject,handles);
handles.im1 = im1;
guidata(hObject,handles);
else
    w=warndlg('没有源图像!','操作无效','modal');
    w=findobj(w,'Type','text');
    set(w,'FontSize',12);
end




function edit3_Callback(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit3 as text
%        str2double(get(hObject,'String')) returns contents of edit3 as a double


% --- Executes during object creation, after setting all properties.
function edit3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit4_Callback(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit4 as text
%        str2double(get(hObject,'String')) returns contents of edit4 as a double


% --- Executes during object creation, after setting all properties.
function edit4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function noise_CreateFcn(hObject, eventdata, handles)
% hObject    handle to noise (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called


% --------------------------------------------------------------------
function main_Callback(hObject, eventdata, handles)
% hObject    handle to main (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function origin_Callback(hObject, eventdata, handles)
% hObject    handle to origin (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.noise = 0;
guidata(hObject,handles);
handles.fliter = 0;
guidata(hObject,handles);
handles.style = 0;
guidata(hObject,handles);
global gray_str; global noise_str;global fliter_str;global style_str;
gray_str = '不进行直方图均衡化 ';noise_str='无噪声加入 ';fliter_str='无滤波器使用 ';style_str='无形态操作 ';
set(handles.edit1,'string','1');
set(handles.slider1,'value',1);
set(handles.no_noise,'value',1);
set(handles.fliter_box,'value',1);
set(handles.edit2,'string','40')
set(handles.no_change,'value',1);
set(handles.edit3,'string',[gray_str noise_str fliter_str style_str char(13)]);


% --------------------------------------------------------------------
function reverse_Callback(hObject, eventdata, handles)
% hObject    handle to reverse (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.have_im1
    im1 = handles.im1;
    im1 = 255-im1;
    axes(handles.axes2);
    imshow(im1);
    handles.im1=im1;
    guidata(hObject,handles);
else
    w=warndlg('没有用于操作的图片!','处理失败','modal');
    w=findobj(w,'Type','text');
    set(w,'FontSize',12);
end
    


% --------------------------------------------------------------------
function help_Callback(hObject, eventdata, handles)
% hObject    handle to help (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
%42字符/行
helptext = char('GUI作者：夏驰2020190506033', ['灰度级分辨率默认数值为1，代表不进行'...
    '直方图均衡化操作'],'其余选项都默认开始不进行参数设置',['当用户进行参数选取之后,'...
    '程序的处理顺序都是 1、灰度级处理，2、噪声加入，3、滤波处理，4、形态学操作'],['如若选取滤波器'...
     '，截止频率初始默认为40'],'当参数选取完成后点击‘确定操作’，图片会被做相应处理',...
     '该窗口左上角设有菜单栏和工具栏，可以进行相应操作',['当已经有图片进行处理之后'...
     '鼠标右击‘效果图’三个字或效果图的周围，会弹出一个菜单，'],['其会将效果图移入‘小图窗进行暂存显示’，'...
     '方便另外选取参数后处理的对比']);
 h=dialog('name','帮助','position',[200 200 500 500]);
 uicontrol('parent',h,'style','text','string',helptext,'position',[20 20 480 450],'fontsize',12);




% --- Executes during object creation, after setting all properties.
function axes3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to axes3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called
set(hObject,'XColor','w') ;% 这两行代码功能：将坐标轴和坐标刻度转为白色
set(hObject,'YColor','w');
 
set(hObject,'XTickLabel',[]); % 这两行代码功能：去除坐标刻度
set(hObject,'YTickLabel',[]);

% Hint: place code in OpeningFcn to populate axes3


% --------------------------------------------------------------------
function small_Callback(hObject, eventdata, handles)
% hObject    handle to small (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.have_im1
axes(handles.axes3);
im = handles.im1;
imshow(im);
else
    w=warndlg('请先生成效果图!','操作无效','modal');
    w=findobj(w,'Type','text');
    set(w,'FontSize',12);
end

% --------------------------------------------------------------------
function window_Callback(hObject, eventdata, handles)
% hObject    handle to window (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function open_ClickedCallback(hObject, eventdata, handles)
% hObject    handle to open (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
[file, path,i] = uigetfile({'*.bmp';'*.jpg';'*.tif';'*.png'},'选择要打开的图片');
if i ==0
    return
end
str = [path file];
im = imread(str);
handles.im = im;
handles.im1 = im;
handles.have_im = 1;
axes(handles.axes1);
imshow(im);
guidata(hObject,handles);


% --- Executes when selected object is changed in noise.
function noise_SelectionChangeFcn(hObject, eventdata, handles)
% hObject    handle to the selected object in noise 
% eventdata  structure with the following fields (see UIBUTTONGROUP)
%	EventName: string 'SelectionChanged' (read only)
%	OldValue: handle of the previously selected object or empty if none was selected
%	NewValue: handle of the currently selected object
% handles    structure with handles and user data (see GUIDATA)
global gray_str; global noise_str;global fliter_str;global style_str;
var = get(eventdata.NewValue,'Tag');
switch var
    case 'no_noise'
        handles.noise = 0;
        noise_str='无噪声加入 ';
    case 'poss'
        handles.noise = 1;
        noise_str='泊松噪声加入 ';
    case 'salt'
        handles.noise = 2;
        noise_str='椒盐噪声加入 ';
    case 'gauss'
        handles.noise = 3;
        noise_str='高斯噪声加入 ';
end
guidata(hObject,handles);
old_str = get(handles.edit3,'string');
set(handles.edit3,'string',char(old_str, [gray_str noise_str fliter_str style_str] ));
set(handles.edit3,'ListboxTop',get(handles.edit3,'ListboxTop')+1);


% --- Executes when selected object is changed in style.
function style_SelectionChangeFcn(hObject, eventdata, handles)
% hObject    handle to the selected object in style 
% eventdata  structure with the following fields (see UIBUTTONGROUP)
%	EventName: string 'SelectionChanged' (read only)
%	OldValue: handle of the previously selected object or empty if none was selected
%	NewValue: handle of the currently selected object
% handles    structure with handles and user data (see GUIDATA)
global gray_str; global noise_str;global fliter_str;global style_str;
var = get(eventdata.NewValue,'Tag');
switch var
    case 'no_change'
        handles.style=0;
        style_str=' 无形态操作';
    case 'down'
        handles.style=1;
        style_str=' 底帽变换';
    case 'open'
        handles.style=2;
        style_str=' 开操作';
    case 'up'
        handles.style=3;
        style_str=' 顶帽变换';
    case 'close'
        handles.style=4;
        style_str=' 闭操作';
end
guidata(hObject,handles);
old_str = get(handles.edit3,'string');
set(handles.edit3,'string',char(old_str, [gray_str noise_str fliter_str style_str] ));
set(handles.edit3,'ListboxTop',get(handles.edit3,'ListboxTop')+1);



% --------------------------------------------------------------------
function save_ClickedCallback(hObject, eventdata, handles)
% hObject    handle to save (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.have_im1==0
    w=warndlg('没有生成新的图片!','保存失败','modal');
    w=findobj(w,'Type','text');
    set(w,'FontSize',12);
    return
end
[file,path,filterindex]=uiputfile({'*.bmp';'*.jpg';'*.png';'*.tif'},'save image');
if filterindex==0
    return
else
    pathname=[path file];
    imwrite(handles.im1,pathname);
end
