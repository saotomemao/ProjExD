import tkinter as tk
import maze_maker as mm # 練習8
import tkinter.messagebox as tkm

# 練習5
def key_down(event):
    global key
    key = event.keysym


# 練習6
def key_up(event):
    global key
    key = ""


# 練習7
def main_proc():
    # 練習12
    delta = {
        # [横座標移動分, 縦座標移動分]
        ""     : [0,  0], 
        "Up"   : [0, -1],
        "Down" : [0, +1],
        "Left" : [-1, 0],
        "Right": [+1, 0],
    }
    global mx, my
    global cx, cy
    # 練習12：仮に移動した先が床なら／else壁なら何もしない
    if maze_lst[my+delta[key][1]][mx+delta[key][0]] == 0:
        mx, my = mx+delta[key][0], my+delta[key][1] # 練習11
        cx, cy = mx*100+50, my*100+50
    canv.coords("tori", cx, cy)
    if mx==13 and my==7:
        tkm.showinfo("おめでと！", "よくできました！")
    elif mx==7 and my==4:
        tkm.showinfo("残念！", "失敗だよ！")
    else:
        root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") # 練習1

    # 練習2
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    # 練習9,10
    maze_lst = mm.make_maze(15, 9)
    #print(len(maze_lst)) 9x15

    # print(maze_lst) # 1:壁／0:床
    mm.show_maze(canv, maze_lst) 

    # 練習3
    tori = tk.PhotoImage(file="ex03/fig/5.png") 
    mx, my = 1, 1 # 練習11
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx, cy, image=tori, tag="tori")

    # 練習4
    key = "" # 現在押されているキーを表す

    # 練習5,6
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)    

    # 練習7
    main_proc()

    root.mainloop()