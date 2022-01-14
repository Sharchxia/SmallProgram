//
// Created by Sharch on 2021/10/14.
//
#include"Prey.h"
Prey::Prey(Prey&p){
    win_w = p.win_w, win_h = p.win_h;
    p_x = p.p_x, p_y = p.p_y;
    width = p.width, height = p.height;
    value = p.value;
    face = p.face;
    x_step = p.x_step, y_step = p.y_step;
}
Prey::Prey(char const*c, int p_x, int p_y, int w, int h, int win_w, int win_h, float v, int x_s, int y_s){
    this->win_w=win_w, this->win_h=win_h;
    this->p_x=p_x, this->p_y=p_y;
    width = w, height = h;
    loadImage(c, &face);
    value = v;
    x_step = x_s, y_step = y_s;
}
void Prey::move(){
    p_x += x_step, p_y += y_step;
    if(p_x+width>win_w){
        p_x=win_w-width;
        if(x_step>0)
        x_step *= -1;
    }else if(p_x<0){
        p_x=0;
        if(x_step<0)
        x_step *= -1;
    }
    if(p_y+height>win_h){
        p_y=win_h-height;
        if(y_step>0)
        y_step *= -1;
    }else if(p_y<0){
        p_y=0;
        if(y_step<0)
        y_step *= -1;
    }
}
info *Prey::getinfo() {
    info *i = new info;
    i->p_x = p_x;
    i->p_y = p_y;
    i->value = value;
    return i;
}
void Prey::p_paint() {
    putImageScale(&face,p_x,p_y,width,height);
}

Prey_1::Prey_1(char const *name, int p_x, int p_y, int w, int h, int win_w, int win_h, float v, int x_s, int y_s, float sc, float in_sc):Prey(name,p_x,p_y,w,h,win_w,win_h,v,x_s,y_s){
    scary = sc;
    increase_scary = in_sc;
    x_s_i=y_s_i=0;
}
info *Prey_1::getinfo() {
    info *i = new info;
    i->p_x = p_x;
    i->p_y = p_y;
    i->value = value+(scary+increase_scary)/10;
    return i;
}
void Prey_1::speed() {
    if(x_step<0){
        x_s_i = -((int)(scary+increase_scary)/4);
    }else{
        x_s_i = (int)(scary+increase_scary)/4;
    }
    if(y_step<0){
        y_s_i = -((int)(scary+increase_scary)/4);
    }else{
        y_s_i = (int)(scary+increase_scary)/4;
    }
}
void Prey_1::move(){
    speed();
    p_x+=(x_s_i+x_step);
    if(p_x+width>win_w){
        p_x=win_w-width;
        if(x_step>0)x_step *= -1;
    }else if(p_x<0){
        p_x=0;
        if(x_step<0)x_step *= -1;
    }
    p_y+=(y_s_i+y_step);
    if(p_y+height>win_h){
        p_y=win_h-height;
        if(y_step>0)y_step *= -1;
    }else if(p_y<0){
        p_y=0;
        if(y_step<0)y_step *= -1;
    }
}
void Prey_1::Scary(float in){
    if(in>150){
        increase_scary = 0;
    }else{
        increase_scary = ((float)150.0-in)/15;
    }
}
