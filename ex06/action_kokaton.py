import pygame as pg
import sys
from random import randint
import tkinter.messagebox as tkm
import tkinter as tk


canjump = True
ysoku=0
g = 0.2


def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate



def jamp():##ジャンプの判定
    global canjump, ysoku
    if canjump:
        canjump = False
        ysoku=-10

def main():
    global canjump, ysoku, g 
    pg.display.set_caption("こうかとん")
    scrn_sfc = pg.display.set_mode((800, 480))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("figge/pg_bg1.png")
    bg_rct = bg_sfc.get_rect()
    pg.init()

    #(プレイヤーの操作する)こうかとんの追加
    tori_sfc = pg.image.load("figge/2.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 100, 350
    #敵エネミー「スライム」の追加
    sura_sfc = pg.image.load("figge/sura.png")
    sura_sfc = pg.transform.rotozoom(sura_sfc, 0, 2.0)
    sura_rct = sura_sfc.get_rect()
    sura_rct.center = 400, 400
    #ゴールポールの追加
    pol_sfc = pg.Surface((20, 20))
    pol_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(pol_sfc, (255, 0, 0), (10, 10), 10) 
    pol_rct = pol_sfc.get_rect()
    pol_rct.centerx = 700
    pol_rct.centery = 70

    vx, vy = 0, 0

    clock = pg.time.Clock()
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)#背景の表示
        scrn_sfc.blit(sura_sfc, sura_rct)#スライムの表示
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        #ゴールポールの線画
        pg.draw.rect(scrn_sfc, (255,255,255), (695,70,10,350))

        key_states = pg.key.get_pressed()
        #矢印キーの設定
        if key_states[pg.K_UP]:
            jamp()
        if key_states[pg.K_LEFT]:  tori_rct.centerx -= 2
        if key_states[pg.K_RIGHT]: tori_rct.centerx += 2

        #ジャンプの場合の設定
        if canjump == False:
            ysoku+=g
            tori_rct.bottom+=ysoku
            if tori_rct.centery>360:
                tori_rct.centery=360
                ysoku=0
                canjump=True

        
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT]: 
                tori_rct.centerx += 2
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 2
        if tate == -1:
            if key_states[pg.K_UP]: 
                tori_rct.centery += 2
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 2    
        
        if key_states[pg.K_a]:  tori_rct.centerx -= 2
        if key_states[pg.K_d]: tori_rct.centerx += 2
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_w]: 
                tori_rct.centerx += 2
            if key_states[pg.K_s]:
                tori_rct.centerx -= 2
        if tate == -1:
            if key_states[pg.K_a]: 
                tori_rct.centery += 2
            if key_states[pg.K_d]:
                tori_rct.centery -= 2 
        
        scrn_sfc.blit(tori_sfc, tori_rct)
        
        yoko, tate = check_bound(pol_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        if(vx<0):
            vx-=0.001
        else:
            vx+=0.001
        if(vy<0):
            vy-=0.001
        else:
            vy+=0.001
        scrn_sfc.blit(pol_sfc, pol_rct)

        #ポールに接触したなら
        if tori_rct.right >=695:
            ti=pg.time.get_ticks()
            tkm.showinfo("おめでとう！", f'クリアおめでとう！\n記録は{ti//1000}秒だよ')
            return
        
        #ポール先端の丸に接触したなら
        if tori_rct.colliderect(pol_rct):
            ti=pg.time.get_ticks()
            tkm.showinfo("おめでとう！", f'クリアおめでとう！\n記録は{ti//1000}秒だよ')
            return

        #スライムに接触したなら
        if tori_rct.colliderect(sura_rct):
            ti=pg.time.get_ticks()
            tkm.showinfo("残念!", f'記録は{ti//1000}秒だよ\nまた挑戦してね！')
            return
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()