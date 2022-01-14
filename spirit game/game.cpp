#include"Hunter.h"
#include"ctime"
#include"cstdlib"
#include"iostream"

const int W_w=1500, W_h=700, class_w=70, class_h=70;//窗口宽高和对象的宽高
const int h_s_x=12, h_s_y=12;//猎手的每次移动长度
const int s_f = 150;//预警距离
const int v_vegetable=3,v_rabbit=10,v_deer=20;//各猎物的value
const float scary_rabbit=20,scary_rabbit_step=15;//兔子的初始恐惧及恐惧影响速度系数
const float scary_deer=30,scary_deer_step=25;//鹿的初始恐惧及恐惧影响速度系数
int score=0;//初始化分数
bool flag_ab=false;//技能标志位
float ability_time=0;//技能剩余时间
ACL_Image bg, bg1;

#define ate(x) do{h_eat_voice();score +=(int)(x)->getinfo()->value;delete (x);(x) = NULL;}while(0)
#define ate_1(x) do{info_h* h=hunter->get_in();float in = h->in;delete h, h = NULL;(x)->Scary(in);}while(0)

Hunter*hunter=NULL;
H_Hunter*human=NULL;//
unsigned int num_p1=0,num_p2=0,num_p3=0;
const unsigned int max_p = 15;
Prey *vegetable[max_p]={NULL};
Prey_1 *rabbit[max_p]={NULL};
Prey_2 *deer[max_p]={NULL};


void time_event(int i);
void key_event(int key, int action);
void Paint_all();
void h_eat_voice();
void ability();

int Setup(){
    ACL_Sound one;
    initWindow("HUNTING",20,20,W_w,W_h);
    unsigned seed = time(0);
    srand(seed);
    int h_x=rand()%W_w+2*class_w, h_y=rand()%W_h+2*class_h;//
    if(h_x+class_w>W_w)h_x=W_w-class_w;
    if(h_y+class_h>W_h)h_y=W_h-class_h;
    hunter=new Hunter("wolf.jpg",h_x,h_y,class_w,class_h,W_w,W_h,3*h_s_x,3*h_s_y);
    human=new H_Hunter("hunter.jpg",0,0,2*class_w,2*class_h,W_w,W_h,h_s_x,h_s_y);//
    loadSound("one.mp3",&one);
    loadImage("bg.jpg", &bg);
    loadImage("bg1.jpg", &bg1);
    playSound(one,1);
    registerKeyboardEvent(key_event);
    startTimer(0,500);
    startTimer(1,50);
    startTimer(2,1000);
    registerTimerEvent(time_event);
    Paint_all();
    return 0;
}

void time_event(int i){
    if(human->get_hunter(*hunter)){
        Paint_all();
        return;
    }//
    hunter->change_weight();
    if(i==3&&flag_ab)flag_ab=false;
    int percent=rand()%10,j;
    switch(i){
        case 0:
            if(num_p1+num_p2+num_p3>=max_p)break;
            int p_x,p_y,s_x,s_y;
            p_x=rand()%W_w,p_y=rand()%W_h;
            s_x=rand()%(2*h_s_x)-h_s_x,s_y=rand()%(2*h_s_y)-h_s_y;
            if(p_x+class_w>W_w)p_x=W_w-class_w;
            if(p_y+class_h>W_h)p_y=W_h-class_h;
            if(percent>=5&&percent<=8) {
                for (j = 0; j < max_p; j++)
                    if (rabbit[j] == NULL) {
                        rabbit[j] = new Prey_1("rabbit.jpg", p_x, p_y, class_w, class_h, W_w, W_h, v_rabbit, s_x, s_y,
                                               scary_rabbit, scary_rabbit_step);
                        num_p2 += 1;
                        break;
                    }
            }
            else if(percent<5){
                for(j = 0; j < max_p; j++)
                    if (vegetable[j] == NULL) {
                        vegetable[j] = new Prey("vege.jpg", p_x, p_y, class_w, class_h, W_w, W_h, v_vegetable, s_x,
                                                s_y);
                        num_p1 += 1;
                        break;
                    }
            }
            else{
                for(j=0;j<max_p;j++)
                    if(deer[j] == NULL){
                        deer[j] = new Prey_2("deer.jpg", p_x, p_y, class_w, class_h,W_w,W_h,v_deer,s_x,s_y,s_f,scary_deer,scary_deer_step);
                        num_p3 += 1;
                        break;
                    }
            }
            break;
        case 1:
            if(ability_time>0)ability_time-=0.05;
            human->run_after(*hunter);
            if(flag_ab)break;
            for(j=0;j<max_p;j++){
                if(rabbit[j]!=NULL) {
                    ate_1(rabbit[j]);
                    rabbit[j]->move();
                    if (hunter->eat(*rabbit[j])) {
                        ate(rabbit[j]);
                        num_p2 -= 1;
                    }
                }
                if(vegetable[j]!=NULL) {
                    vegetable[j]->move();
                    if(hunter->eat(*vegetable[j])){
                        ate(vegetable[j]);
                        num_p1-=1;
                    }
                }
                if(deer[j]!=NULL) {
                    ate_1(deer[j]);
                    deer[j]->move(*hunter);
                    if(hunter->eat(*deer[j])){
                        ate(deer[j]);
                        num_p3-=1;
                    }
                }
            }
            break;
        case 2:
            hunter->lose_weight();
            break;
    }
    hunter->change_weight();
    Paint_all();
}
void key_event(int key, int action){
    if(human->get_hunter(*hunter)){
        Paint_all();
        return;
    }//
    if(action != KEY_DOWN)return;
    if(key==0x0d&& !flag_ab)ability();
    hunter->move(key);
    for(int j=0;j<max_p;j++){
        if(rabbit[j]!=NULL)
            if(hunter->eat(*rabbit[j])){
                ate(rabbit[j]);
                num_p2-=1;
            }
        if(vegetable[j]!=NULL)
            if(hunter->eat(*vegetable[j])){
                ate(vegetable[j]);
                num_p1-=1;
                    }
        if(deer[j]!=NULL)
            if(hunter->eat(*deer[j])){
                ate(deer[j]);
                num_p3-=1;
            }
    }
    hunter->change_weight();
    Paint_all();
}
void Paint_all(){
    beginPaint();
    clearDevice();
    if(! human->get_hunter(*hunter)){
        if (flag_ab)putImageScale(&bg1, 0, 0, W_w, W_h);
        else putImageScale(&bg, 0, 0, W_w, W_h);
        for (int j = 0; j < max_p; j++) {
            if (rabbit[j] != NULL)rabbit[j]->p_paint();
            if (vegetable[j] != NULL)vegetable[j]->p_paint();
            if (deer[j] != NULL)deer[j]->p_paint();
        }
        human->h_paint();
        hunter->h_paint();
        char weight[10], Score[15], time[15];
        char const s[] = " seconds";
        info_h *h = hunter->get_in();
        float in = h->in;
        delete h, h = NULL;
        sprintf(weight, "%.3f", in);
        sprintf(Score, "%d", score);
        sprintf(time, "%.3f", ability_time);
        strcat(time, s);
        paintText(5, 5, "Score:");
        paintText(5, 20, Score);
        paintText(5, 35, "Weight");
        paintText(5, 50, weight);
        paintText(5, 65, "Ability: (Push Enter)");
        if (ability_time <= 0 && score >= 60)paintText(5, 80, "The ability is ready !");
        else if (score < 80 && !flag_ab)paintText(5, 80, "Too tired to use ability ~");
        else paintText(5, 80, time);
    }else{
        char Score[15];
        sprintf(Score, "%d", score);
        setTextSize(100);
        paintText(300,50,"GAME OVER !");
        paintText(300,250, "THE TOTAL SCORE IS:");
        paintText(300,450,Score);
    }
    endPaint();
}
void h_eat_voice(){
    ACL_Sound eat;
    loadSound("eat.mp3",&eat);
    playSound(eat,0);
}
void ability(){
    if(score<60)return;
    score -= 60;
    hunter->lose_weight();
    hunter->lose_weight();
    hunter->lose_weight();
    flag_ab = true;
    startTimer(3, 5000);
    ability_time=5;
}