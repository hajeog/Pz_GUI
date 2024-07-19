from tkinter import *
from tkinter import ttk
import tkinter as Tk


root = Tk.Tk()

#이름 변경
root.title('독감 진단키트 예측 프로그램')

#창 크기 변경
root.geometry('600x600+100+100')


#함수
def make_lab14(): #labll14에 ent12의 결과를 받는다
    labll14.configure(text=ent12.get())

def make_lab24(): #labll24에 ent22의 결과를 받는다
    labll24.configure(text=ent22.get())

def make_lab34():
    labll34.configure(text=ent32.get())

def make_PPV_NPV():
    Sen = float(labll14.cget("text"))/100
    Spe = float(labll24.cget("text"))/100
    P_r = float(labll34.cget("text"))/100

    PPV = round((P_r *Sen)/(P_r*Sen+(1-P_r)*(1-Spe))*100,2)

    NPV = round(((1-P_r)*Spe)/((1-P_r)*Spe+P_r*(1-Sen))*100,2)

    labll54.config(text=PPV)
    labll64.config(text=NPV)





# 1행 라벨 생성
labll = Tk.Label(root,text="민감도",bg='red',fg='white',width=8,height=2,font=('맑은 고딕',16,'bold')) #라벨 생성 각각 [삽입 단어],[색상],[글자색상],[가로],[세로],[폰트]
labll.grid(row=0,column=0,padx=5,pady=10)

#입력창 생성
ent12=Tk.Entry(bg='white',width=8,font=('맑은 고딕',16,'bold'))
ent12.grid(row=0,column=1,padx=5,pady=10)

#버튼 생성
button13=Tk.Button(root,text='\u2192',font=('맑은 고딕',12,'bold'),bg='red',fg='white',width=4,height=1,command=make_lab14)
button13.grid(row=0,column=2,padx=5,pady=10)

#결과 생성
labll14 = Tk.Label(root,bg='white',width=8,height=1,font=('맑은 고딕',16,'bold'))
labll14.grid(row=0,column=3,padx=5,pady=10)



# 2행 라벨 생성
labl2 = Tk.Label(root,text="특이도",bg='red',fg='white',width=8,height=2,font=('맑은 고딕',16,'bold')) #라벨 생성 각각 [삽입 단어],[색상],[글자색상],[가로],[세로],[폰트]
labl2.grid(row=1,column=0,padx=5,pady=10)

#입력창 생성
ent22=Tk.Entry(bg='white',width=8,font=('맑은 고딕',16,'bold'))
ent22.grid(row=1,column=1,padx=5,pady=10)

#버튼 생성
button23=Tk.Button(root,text='\u2192',font=('맑은 고딕',12,'bold'),bg='red',fg='white',width=4,height=1,command=make_lab24)
button23.grid(row=1,column=2,padx=5,pady=10)

#결과 생성
labll24 = Tk.Label(root,bg='white',width=8,height=1,font=('맑은 고딕',16,'bold'))
labll24.grid(row=1,column=3,padx=5,pady=10)


# 3행 라벨 생성
labl3 = Tk.Label(root,text="발생도",bg='red',fg='white',width=8,height=2,font=('맑은 고딕',16,'bold')) #라벨 생성 각각 [삽입 단어],[색상],[글자색상],[가로],[세로],[폰트]
labl3.grid(row=2,column=0,padx=5,pady=10)

#입력창 생성
ent32=Tk.Entry(bg='white',width=8,font=('맑은 고딕',16,'bold'))
ent32.grid(row=2,column=1,padx=5,pady=10)

#버튼 생성
button33=Tk.Button(root,text='\u2192',font=('맑은 고딕',12,'bold'),bg='red',fg='white',width=4,height=1,command=make_lab34)
button33.grid(row=2,column=2,padx=5,pady=10)

#결과 생성
labll34 = Tk.Label(root,bg='white',width=8,height=1,font=('맑은 고딕',16,'bold'))
labll34.grid(row=2,column=3,padx=5,pady=10)


#4행 라벨
labl4=Tk.Button(root,text="계산하기(클릭)",font=('맑은 고딕',12,'bold'),bg='red',fg='white',width=4,height=1,command=make_PPV_NPV)
labl4.grid(row=3,column=0,padx=5,pady=10,columnspan=4,sticky='we')


# 5행 라벨 생성
labl5 = Tk.Label(root,text="양성 예측(양성 = 진짜 양성)",bg='red',fg='white',width=8,height=2,font=('맑은 고딕',16,'bold')) #라벨 생성 각각 [삽입 단어],[색상],[글자색상],[가로],[세로],[폰트]
labl5.grid(row=4,column=0,padx=5,pady=10,columnspan=3,sticky='we')

#결과 생성
labll54 = Tk.Label(root,bg='yellow',width=8,height=1,font=('맑은 고딕',16,'bold'))
labll54.grid(row=4,column=3,padx=5,pady=10)

# 6행 라벨 생성
labl6 = Tk.Label(root,text="음성 예측(음성 = 진짜 음성)",bg='red',fg='white',width=8,height=2,font=('맑은 고딕',16,'bold')) #라벨 생성 각각 [삽입 단어],[색상],[글자색상],[가로],[세로],[폰트]
labl6.grid(row=5,column=0,padx=5,pady=10,columnspan=3,sticky='we')

#결과 생성
labll64 = Tk.Label(root,bg='yellow',width=8,height=1,font=('맑은 고딕',16,'bold'))
labll64.grid(row=5,column=3,padx=5,pady=10)


root.mainloop()