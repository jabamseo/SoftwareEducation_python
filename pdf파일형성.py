import os
import tkinter as tk
import tkinter.messagebox as msg
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import reportlab.lib.units as unit
import reportlab.lib.pagesizes as pagesizes
# TrueType
from reportlab.pdfbase import ttfonts

def Buttonclick() :
    a = editbox1.get()
    b = editbox2.get()
    c = editbox3.get()
    d = editbox4.get()
    letterok = False
    numberok = False
    fontok = False
    if len(a) <= 10 and len(a) != 0:
        letterok = True
    else:
        msg.showerror('오류', '10글자 이내입니다.')

    if len(b) == 3:
        numbercheck = True
        for i in range(3):
            if("0" > b[i] or b[i] > "9"):
                msg.showerror('오류', '숫자가 아닙니다.')
                numbercheck = False
                break
        if numbercheck == True:
            new_b = int(b[0])*100 + int(b[1])*10 + int(b[2])
            if new_b >= 150 and new_b <= 210:
                numberok = True
            else:
                msg.showerror('오류', '유효글자 크기 범위가 아닙니다.')
    elif len(b) == 0:
        msg.showerror('오류', '글자 크기를 입력해 주세요.')
    else:
        msg.showerror('오류', '유효글자 크기 범위가 아닙니다.')

    if len(c) == 0:
        c = "gulim.ttc"
        fontok = True
    else:
        path = "C:/Windows/Fonts/"
        file_name = os.listdir(path)
        if c not in file_name:
            msg.showerror('오류', f'{c}는 없는 폰트입니다.')
        else:
            fontok = True
    
    if len(d) == 0:
        d = "final"
    else:
        pass
    
    if letterok == True & numberok == True & fontok == True:
        # TrueType 폰트 등록
        pdfmetrics.registerFont(ttfonts.TTFont(f"{c}", f"C:\\Windows\\Fonts\\{c}"))

        # PDF를 만든다
        pdf = canvas.Canvas(f"{d}.pdf", pagesize=pagesizes.A4)

        title = a
        for letter in title:
            # 폰트 크기는 용지 너비와 같은 210mm으로 한다
            # 폰트 종류는 TTFFont의 첫번에 인수에 지정한 것
            pdf.setFont(f"{c}", new_b * unit.mm)
            # 높이
            h = (297 - new_b) / 2 * unit.mm
            
            pdf.drawString(0 * unit.mm, h, letter)
            pdf.showPage()

        # 저장
        pdf.save()
        msg.showinfo('완료', '저장되었습니다')


root = tk.Tk()
root.geometry('500x300')
root.title('플래시 카드 만들기')
#label, editbox 1
label1 = tk.Label(root, text='1. 10글자 이내 내용을 입력하세요')
label1.place(x=20, y=20)
editbox1 = tk.Entry(width=20, font=('Helvetica', 14))
editbox1.place(x=250, y=20)
#label, editbox 2
label2 = tk.Label(root, text='2. 글자크기를 입력하세요(150-210. 단위 mm)')
label2.place(x=20, y=50)
editbox2 = tk.Entry(width=20, font=('Helvetica', 14))
editbox2.place(x=250, y=70)
#label, editbox 3
label3 = tk.Label(root, text='3. 폰트를 입력하세요(대소문자 구별하여 입력, 지정하지 않으면 기본 gulim)')
label3.place(x=20, y=110)
editbox3 = tk.Entry(width=20, font=('Helvetica', 14))
editbox3.place(x=250, y=130)
#label, editbox 4
label4 = tk.Label(root, text='4. 저장할 파일이름을 입력하세요(지정하지 않으면 기본 final.pdf)')
label4.place(x=20, y=170)
editbox4 = tk.Entry(width=20, font=('Helvetica', 14))
editbox4.place(x=250, y=190)

button1 = tk.Button(root, text ='만들기', font=('Helvetica',14), command=Buttonclick)
button1.place(x=220, y=250)

root.mainloop()