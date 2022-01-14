//
// Created by Sharch on 2021/10/14.
//
#include"acllib.h"
#ifndef GAME_PREY_H
#define GAME_PREY_H
typedef struct info {
    int p_x, p_y;
    float value;
}info;//此结构体用于方便传输食物信息
class Prey{
protected:
    int win_w, win_h;//窗口大小
    int p_x, p_y;//食物的位置
    int width, height;//食物的尺寸大小
    float value;//食物所含营养价值
    int x_step, y_step;//每一帧的步长，需要在主文件中随机生成
    ACL_Image face;//食物的特征图片
public:
    Prey(Prey & p);
    Prey(char const*c, int p_x, int p_y, int w, int h, int win_w, int win_h, float v, int x_s, int y_s);
    virtual void move();//移动
    virtual void speed(){}//基类没有恐惧值属性，所以速度相当于不变
    virtual info *getinfo();//
    void p_paint();
};
class Prey_1:public Prey{
    float increase_scary,scary;//变化恐惧及基础恐惧（警惕值）
protected:
    int x_s_i;
    int y_s_i;
public:
    Prey_1(char const *name, int p_x, int p_y, int w, int h, int win_w, int win_h, float v, int x_s, int y_s, float sc, float in_sc);
    info *getinfo();//得到食物的一些信息，方便猎手使用（位置，营养价值）该类的营养价值会随恐惧值而改变
    void speed();//由于恐惧值的改变而改变速度
    virtual void move();//每一帧的移动
    void Scary(float in);//改变class 2的恐惧值
};

#endif //GAME_PREY_H
