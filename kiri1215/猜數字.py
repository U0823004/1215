import random
print("猜數字遊戲")
print("游戲規則：系統隨機給出1-9的4位數字，您可以輸入您猜測的4位數字，系統會比較並給予提示，A表示數字對且位置對，B表示數字對位置不對，如1A2B表示有1位您猜對了數字和位置，有2位您猜對數字，但位置不對。")
total='123456789'
answer=random.sample(total,4)
guessTimesrange=input('請輸入想挑戰的最多要在幾次內完成，否則挑戰失敗(最多20次)')
if guessTimesrange == '':
    guessTimesrange = 20
else:
    guessTimesrange=int(guessTimesrange)
    if guessTimesrange >= 20:
        guessTimesrange=20
    else:
        guessTimesrange=guessTimesrange
for guessTimes in range(guessTimesrange):
   guess=""
   for inputErros in range(3):
      guess=input("請輸入4位1-9的不重復數字：") 
      if guess.isdigit()==True and len(guess)==4:
         guessSet=set(guess)
         if len(guessSet)==4 and guessSet.isdisjoint(set('0')):
            break
   else:
      print("您沒有理解游戲規則，答案是%s，游戲結束。"%(answer))
      break   
   A=0
   B=0
   for j in range(4):
      if guess[j]==answer[j]:
         A+=1
      else:
         for k in range(4):
            if guess[j]==answer[k]:
               B+=1
   if A<4:
      if guessTimes<int(guessTimesrange-1):
         print("%dA%dB，您還有%d次機會。" %(A,B,guessTimesrange-guessTimes-1))
      else:
         print("很遺憾您沒有猜對，答案是%s，再玩一局吧。" %(answer))   
   else:
      print("恭喜您猜對了！總共猜了%d次" %(guessTimes+1))
      break