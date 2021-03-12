import tkinter as tk
import tkinter.messagebox as msg
import random

def ButtonClick() :
    
    b=editbox1.get()

    isok = False
    
    if len(b) != 4 :
        msg.showinfo("오류", "네 자릿수 숫자 오류")
    else :
        numberok = True
        for i in range(4) :
            if("0" > b[i] or b[i] > "9") :
                msg.showinfo("오류", "숫자가 아닙니다.")
                numberok = False
                break
            if numberok == True :
                    isok=True

#아랫쪽에 히트와 블로를 검색하는 코드가 들어감.
    hit=0
    blow=0
    if isok==True :
        for i in range(4) :
            if(a[i]==int(b[i])) :
                hit = hit +1

        for i in range(4) :
            for j in range(4) :
                if(int(b[i])==a[j])  and (a[i] != int(b[i])) and (a[j] != int(b[j])) :
                    blow = blow + 1
                    break  
      
    if hit == 4 :
        msg.showinfo("정답", "축하합니다.")
        root.destroy()
    else :
        historybox.insert(tk.END, b + "/H:" + str(hit) + "  B:"+str(blow)+"\n")
        editbox1.delete(0, 'end')
        #msg.showinfo("힌트", "힛트"+str(hit) + "/" +"블로"+str(blow))

a = [random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9)]
print(str(a[0])+str(a[1])+str(a[2])+str(a[3]))

root = tk.Tk()
root.geometry("600x400")
root.title("수맞추기 게임")

label1=tk.Label(root, text="숫자를 입력해 주세요")
label1.place(x=20, y=20)

editbox1=tk.Entry(width=4, font=("Helvetica", 28))
editbox1.place(x=120, y=60)

button1=tk.Button(root, text ="확인", font=("Helvetica", 14), command=ButtonClick)
button1.place(x=220, y=60)

historybox=tk.Text(root, font=("Helvetica", 14))
historybox.place(x=400, y=0, width=200, height=400)


root.mainloop()