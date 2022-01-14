//
// Created by Sharch on 2021/10/14.
//
#include"Hunter.h"

Hunter::Hunter(Hunter&h){
    p_x = h.p_x, p_y = h.p_y;
    width = h.width, height = h.height;
    x_step = 10, y_step = 10;
    face = h.face;
    win_w = h.win_w, win_h = h.win_h;
    inside = 0.0;
    fat_x=fat_y=0;
}
Hunter::Hunter(char const *name, int p_x, int p_y, int w, int h, int win_w, int win_h, int x_s, int y_s) {
    loadImage(name, &face);
    this->win_w = win_w, this->win_h = win_h;
    this->p_x = p_x, this->p_y = p_y;
    width = w, height = h;
    x_step = x_s, y_step = y_s;
    inside = 0.0;
    fat_x=fat_y=0;
}
void Hunter::move(int i){
    this->speed();
    switch(i){
        case VK_UP:
            p_y -= y_step;
            if(p_y<0)p_y=win_h-height-fat_y;
            break;
        case VK_DOWN:
            p_y += y_step;
            if(p_y+height+fat_y>win_h)p_y=0;
            break;
        case VK_LEFT:
            p_x -= x_step;
            if(p_x<0)p_x=win_w-width-fat_x;
            break;
        case VK_RIGHT:
            p_x += x_step;
            if(p_x+width+fat_x>win_w)p_x=0;
            break;
    }
}
int Hunter::eat(Prey &p){
    info *i = p.getinfo();
    float value;
    if(inside>50)
        value = 50*(i->value)/inside;
    else  value = i->value;
    if(p_x-width<i->p_x&&p_x+width+fat_x>i->p_x){
        if(p_y-height<i->p_y&&p_y+height+fat_y>i->p_y){
            inside += value;
            speed();
            delete i, i = NULL;
            return 1;
        }
    }
    delete i, i = NULL;
    return 0;
}
void Hunter::speed(){
    if(inside<=50)x_step=y_step=10;
    else{
        x_step=y_step=10;
        x_step=y_step=10-(int)(inside/50)*2;
    }
    if(x_step<3)x_step=y_step=3;
}
info_h *Hunter::get_in(){
    info_h *h = new info_h;
    h->in = inside;
    h->p_x = this->p_x;
    h->p_y = this->p_y;
    h->fat_x = this->fat_x;
    h->fat_y = this->fat_y;
    return h;
}
void Hunter::lose_weight(){
    if(inside>160)inside-=5.5;
    else if(inside>120)inside-=4;
    else if(inside>70)inside-=3;
    else if(inside>30)inside-=2.5;
    else if(inside>0)inside-=2;
    if(inside<0)inside=0;
}
void Hunter::change_weight() {
    fat_y=fat_x=(int)inside/3;
}
void Hunter::h_paint() {
    putImageScale(&face,p_x,p_y,width+fat_x,height+fat_y);
}

H_Hunter::H_Hunter(const char *name, int p_x, int p_y, int w, int h, int win_w, int win_h, int x_s, int y_s): Hunter(name,p_x,p_y,w,h,win_w,win_h,x_s,y_s) {
    fat_x=fat_y=0;
    inside=0;
}
float H_Hunter::speed(Hunter &h) {
    info_h *inf=h.get_in();
    float in = inf->in;
    delete inf, inf=NULL;
    return in/120;
}
void H_Hunter::run_after(Hunter &h) {
    info_h *inf=h.get_in();
    int x=inf->p_x,y=inf->p_y;
    float x_vector=(float)x-(float)p_x, y_vector=(float)y-(float)p_y;
    float sed=(float)(x_step+y_step)*speed(h)/2;
    p_x+=(int)(x_vector/(abs(x_vector)+abs(y_vector))*sed);
    p_y+=(int)(y_vector/(abs(x_vector)+abs(y_vector))*sed);
    if(p_x<=0)p_x=0;
    else if(p_x+width>=win_w)p_x=win_w-width;
    if(p_y<=0)p_y=0;
    else if(p_y+height>=win_h)p_y=win_h-height;
}
bool H_Hunter::get_hunter(Hunter &h) {
    info_h *inf=h.get_in();
    int x=inf->p_x,y=inf->p_y,f_x=inf->fat_x,f_y=inf->fat_y;
    delete inf, inf=NULL;
    if(p_x-width/2-f_x<x&&p_x+width>x)
        if(p_y-height/2-f_y<y&&p_y+height>y)
            return true;
    return false;
}

Prey_2::Prey_2(const char *name, int p_x, int p_y, int w, int h, int win_w, int win_h, float v, int x_s, int y_s, int s_d,float sc, float in_sc):Prey_1(name,p_x,p_y,w,h,win_w,win_h,v,x_s,y_s,sc,in_sc) {
    safe_distance = s_d;
    flag_s = true;
}
bool Prey_2::test(Hunter &h) {
    info_h *hu = h.get_in();
    int fat_x=hu->fat_x, fat_y=hu->fat_y, x=hu->p_x, y=hu->p_y;
    delete hu, hu=NULL;//获得猎手位置等信息后
    if(p_x+safe_distance+width>x&&p_x-safe_distance<x+width+fat_x)
        if(p_y+safe_distance+height>y&&p_y-safe_distance<y+height+fat_y) {
            if(flag_s) {//前两个if判断是否进入预警距离，标志位初始为true
                flag_s=false;//第三个if使用标志位，保证进入时才改变方向
                return true;
            }
            else return false;//已经进入还没跑出预警距离，不变方向
        }
    flag_s=true;//跑出预警距离，所以标志位又回到 true
    return false;
}
void Prey_2::move(Hunter&h) {
    speed();//根据恐惧值改变速度
    p_x+=(x_s_i+x_step);
    p_y+=(y_s_i+y_step);//移动一次后的坐标
    if(p_x+width<0)p_x=win_w-width;
    else if(p_x>win_w)p_x=0;
    if(p_y+height<0)p_y=win_h-height;
    else if(p_y>win_h)p_y=0;
    if(test(h)){//需要改变方向即改变方向
        x_step *= -1;
        y_step *= -1;
    }
}