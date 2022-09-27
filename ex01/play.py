import random
import datetime

all_alp = 26  # 全アルファベット数
ti = 10 # 対象文字数
lost = 2  # 欠損文字数

def shutudai(alphabet):
    toi = random.sample(alphabet, ti)
    print("対象文字：", end="")
    for c in sorted(toi): 
        print(c, end=" ")
    print()
    kesson = random.sample(toi, lost)
    print("表示文字：", end="")
    for c in toi: 
        if c not in kesson: 
            print(c, end=" ")
    print()
    #print("デバッグ用欠損文字：", kesson)
    return kesson

def kaito(ans):
    print("欠損数")
    a=input("回答")
    
    if int(a) == lost:
        print("正解！！良いね！！")
        for i in range(lost):
            b = input(f"{i+1}文字目は？：")
            if b not in ans:
                print("不正解です")
                kaito(ans)
            else:
                ans.remove(b)
    else:
        print("不正解")
        kaito(ans)
    print("正解！すごい！！")

if __name__ == "__main__":

    alphabet = [chr(i+65) for i in range(all_alp)]
    #print(alphabet)
    st = datetime.datetime.now()
    ans=shutudai(alphabet)
    kaito(ans)
    ed = datetime.datetime.now()
    print(f"全ての問題正解までにかかった時間{(ed-st).seconds}秒")

