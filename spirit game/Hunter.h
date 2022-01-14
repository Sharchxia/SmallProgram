//
// Created by Sharch on 2021/10/14.
//
#include"acllib.h"
#include"Prey.h"
#ifndef GAME_HUNTER_H
#define GAME_HUNTER_H

typedef struct info_h{
    float in;
    int p_x, p_y;
    int fat_x, fat_y;
}info_h;
class Hunter{
protected:
    int fat_x, fat_y;//当饥饿值（饱腹值）改变，猎手尺寸会改变（长胖、消瘦）
    int win_w, win_h;//窗口大小
    int p_x, p_y;// position
    int width, height;// size
    int x_step, y_step;// speed
    float inside;// hungry value
    ACL_Image face;// picture
public:
    Hunter(Hunter &h);
    Hunter(char const *name, int p_x, int p_y, int w, int h, int win_w, int win_h, int x_s, int y_s);
    void move(int i);//通过键盘控制移动
    int eat(Prey &p);//通过判断决定食物是否被吃掉，返回1代表被吃
    void speed();//速度会随体型大小而改变
    info_h* get_in();//得到并返回猎手饥饿值，位置信息供猎物使用，该值会影响class 2的恐惧值
    void lose_weight();//每一段时间猎手的体重（饥饿值）都会下降，最低为0
    void change_weight();//改变猎手体重
    void h_paint();//画出猎手
};
class H_Hunter:public Hunter {
public:
    H_Hunter(char const *name, int p_x, int p_y, int w, int h, int win_w, int win_h, int x_s, int y_s);
    void run_after(Hunter& h);
    float speed(Hunter& h);
    bool get_hunter(Hunter& h);
};
class Prey_2:public Prey_1{
    int safe_distance;//预警距离
public:
    bool flag_s;//预警到猎手后改变方向与否
    Prey_2(char const *name, int p_x, int p_y, int w, int h, int win_w, int win_h, float v, int x_s, int y_s, int s_d, float sc, float in_sc);
    void move(Hunter&h);
    bool test(Hunter&h);//检测是否预警到猎手
};
#endif //GAME_HUNTER_H
