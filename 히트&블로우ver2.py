import tkinter as tk #윈도우창 import하고 tk라고 부르겠다.
import tkinter.messagebox as msg
import random

global sum
sum = 0

def Buttonclick() :
    global sum
    sum += 1
    b = editbox1.get()
    isok = False
    if len(b) != 5:
        msg.showerror('오류', '5자릿수의 숫자를 입력하세요') #title, label
    else:
        numberok = True
        for i in range(5) :
            if("0" > b[i] or b[i] > "9"):
                msg.showerror('오류', '숫자가 아닙니다.')
                numberok = False
                break
        if numberok == True:
            isok=True

#아랫쪽에 히트와 블로를 검색하는 코드가 들어감.
    hit = 0
    blow = 0
    if isok == True:
        for i in range(5):
            if(a[i]==int(b[i])):
                hit += 1
        for i in range(5):
            for j in range(5):
                if(int(b[i])==a[j]) and (a[i]) != int(b[i]) and (a[i] != int(b[j])):
                    blow +=1
                    break

    if hit == 5:
        msg.showinfo('정답', '축하합니다.')
        root.destroy()
    elif sum == 20:
        msg.showinfo('기회종료', f'어휴 답답해...정답은 {a}')
        root.destroy()
    else:
        historybox.insert(tk.END, b + "/H:"+str(hit) + '/' + ' B:' + str(blow)+"\n")
    #print(sum)

a  = [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
#print(str(a[0])+str(a[1])+str(a[2])+str(a[3])+str(a[4]))

root = tk.Tk() #윈도우창 이름을 root
root.geometry('600x400') #크기지정
root.title('수 맞추기 게임')

label1 = tk.Label(root, text='숫자를 입력하세요')
label1.place(x=20, y=60)

editbox1 = tk.Entry(width=5, font=('Helvetica', 28))
editbox1.place(x=200, y=60)

button1 = tk.Button(root, text ='확인', font=('Helvetica',14), command=Buttonclick)
button1.place(x=350, y=60)

historybox = tk.Text(root, font=("Helvetica", 14))
historybox.place(x=0,y=150, width=600, height=250)


root.mainloop() #창을 연다.