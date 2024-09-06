from tkinter import *
import random


def play(): #메인윈도우
    

    def switch_to_attack(): #수비에서 공격으로 전환
        bt1.config(text="휘두르기", command=attack)
        play_label1.config(text="공격")
        play_label2.config(text="수비")
        play_label3.config(text=f"{inning}회 말")


    def switch_to_defend(): #공격에서 수비로 전환
        global inning
        bt1.config(text="던지기", command=defend)
        play_label1.config(text="수비")
        play_label2.config(text="공격")
        inning += 1 #이닝 1 증가
        play_label3.config(text=f"{inning}회 초")


    def attack():    #공격상황
        global b_count
        global s_count
        global o_count
        global bases
        homerun1 = random.randrange(1, 40)  #랜덤한 두 수가 일치하면 홈런
        homerun2 = random.randrange(1, 40)
        com1 = random.randrange(1, 10)
        com2 = random.randrange(1, 100)
        if homerun1 == homerun2:
            b_count = 0
            s_count = 0 #볼, 스트라이크 카운트 리셋
            result_label1.config(text="HOMERUN")
            result_label2.config(text=f"B: {b_count}  S: {s_count}")
            result_label3.config(text=f"O: {o_count}")
            user_hit_homerun() #홈런 함수 호출
        else:   #홈런이 아닐떄
            if rbt.get() == com1: #라디오버튼의 수가 랜덤한 1~9의 수와 일치하면
                result_label1.config(text="안타")
                result_label2.config(text="")
                result_label3.config(text=f"O: {o_count}")
                b_count = 0
                s_count = 0 #리셋
                user_hit_single() #안타 함수 호출
            else: #일치하지 않으면
                if com2 % 2 != 0:   # 50%확률로 스트라이크
                    result_label1.config(text="스트라이크")
                    s_count += 1 #스트라이크 카운트 증가
                    result_label2.config(text=f"B: {b_count}  S: {s_count}")
                    result_label3.config(text=f"O: {o_count}")
                    if s_count == 3: #삼진아웃
                        result_label1.config(text="삼진아웃")
                        result_label2.config(text="")
                        b_count = 0
                        s_count = 0 #리셋
                        o_count += 1 #아웃카운트 증가
                        result_label3.config(text=f"O: {o_count}")
                        if o_count == 3: #3아웃
                            b_count = 0
                            s_count = 0 #리셋
                            o_count = 0
                            if inning >= 3 :    
                                if com_score != user_score: # 점수가 다르면
                                    game_finish() #3이닝 게임종료
                                else: #점수가 같으면 계속
                                    result_label1.config(text="3아웃, 공격 수비 change")
                                    result_label2.config(text=f"B: {b_count}  S: {s_count}")
                                    result_label3.config(text=f"O: {o_count}")
                                    bases = [0, 0, 0]
                                    update_bases()
                                    switch_to_defend()
                            result_label1.config(text="3아웃, 공격 수비 change")
                            result_label2.config(text=f"B: {b_count}  S: {s_count}")
                            result_label3.config(text=f"O: {o_count}")
                            bases = [0, 0, 0] #베이스 초기화
                            update_bases()
                            switch_to_defend()
                else:   #볼
                    result_label1.config(text="볼")
                    b_count += 1 #볼카운트 증가
                    result_label2.config(text=f"B: {b_count}  S: {s_count}")
                    result_label3.config(text=f"O: {o_count}")
                    if b_count == 4: #볼넷
                        result_label1.config(text="볼넷")
                        result_label2.config(text="")
                        result_label3.config(text=f"O: {o_count}")
                        b_count = 0
                        s_count = 0
                        user_base_on_balls()


    def defend():    #수비상황
        global b_count
        global s_count
        global o_count
        global bases
        homerun1 = random.randrange(1, 40)
        homerun2 = random.randrange(1, 40)
        com1 = random.randrange(1, 10)
        com2 = random.randrange(1, 100)
        if homerun1 == homerun2:
            b_count = 0
            s_count = 0
            result_label1.config(text="HOMERUN")
            result_label2.config(text=f"B: {b_count}  S: {s_count}")
            result_label3.config(text=f"O: {o_count}")
            com_hit_homerun()
        else:
            if rbt.get() == com1:
                result_label1.config(text="안타")
                result_label2.config(text="")
                result_label3.config(text=f"O: {o_count}")
                b_count = 0
                s_count = 0
                com_hit_single()
            else:
                if com2 % 2 != 0:
                    result_label1.config(text="스트라이크")
                    s_count += 1
                    result_label2.config(text=f"B: {b_count}  S: {s_count}")
                    result_label3.config(text=f"O: {o_count}")
                    if s_count == 3:
                        result_label1.config(text="삼진아웃")
                        result_label2.config(text="")
                        b_count = 0
                        s_count = 0
                        o_count += 1
                        result_label3.config(text=f"O: {o_count}")
                        if o_count == 3:
                            b_count = 0
                            s_count = 0
                            o_count = 0
                            result_label1.config(text="3아웃, 공격 수비 change")
                            result_label2.config(text=f"B: {b_count}  S: {s_count}")
                            result_label3.config(text=f"O: {o_count}")
                            bases = [0, 0, 0]
                            update_bases()
                            switch_to_attack()
                else:
                    result_label1.config(text="볼")
                    b_count += 1
                    result_label2.config(text=f"B: {b_count}  S: {s_count}")
                    result_label3.config(text=f"O: {o_count}")
                    if b_count == 4:
                        result_label1.config(text="볼넷")
                        result_label2.config(text="")
                        result_label3.config(text=f"O: {o_count}")
                        b_count = 0
                        s_count = 0
                        com_base_on_balls()



    def com_hit_single():    #수비상황 안타
        global com_score
        if bases[2] == 1: #3루에 주자가 있으면
            com_score += 1  #득점
            score_label4.config(text=f"{com_score}") #점수판 업데이트
            bases[2] = 0 #3루 비움
        if bases[1] == 1:   #2루에 주자가 있으면
            bases[2] = 1    #3루로 이동
            bases[1] = 0    #2리 비움
        if bases[0] == 1:   #1루에 주자가 있으면
            bases[1] = 1    #2루로 이동
            bases[0] = 0    #1루 비움
        bases[0] = 1    #타자는 1루로 이동
        update_bases()  #베이스상황 업데이트


    def user_hit_single():    #공격상황 안타
        global user_score
        if bases[2] == 1:
            user_score += 1
            score_label2.config(text=f"{user_score}")
            bases[2] = 0
        if bases[1] == 1:
            bases[2] = 1
            bases[1] = 0
        if bases[0] == 1:
            bases[1] = 1
            bases[0] = 0
        bases[0] = 1
        update_bases()


    def com_hit_homerun():    #수비상황 홈런
        global com_score
        count = 0   #지역변수 count로 점수 합
        if bases[2] == 1: #3루에 주자가 있으면
            count += 1  #count 1 증가
            bases[2] = 0    #3루 비움
        if bases[1] == 1:   #2루에 주자가 있으면
            count += 1  # count 1 증가
            bases[1] = 0 #2루비움
        if bases[0] == 1:   #1루에 주자가 있으면
            count += 1  # count 1 증가
            bases[0] = 0    #1루 비움
        count += 1  #타자까지 해서 count 1 증가
        com_score += count # count만큼 점수 증가
        score_label4.config(text=f"{com_score}")    #점수판 업데이트
        update_bases()  #베이스 업데이트


    def user_hit_homerun():    #공격상황 홈런
        global user_score
        count = 0
        if bases[2] == 1:
            count += 1
            bases[2] = 0
        if bases[1] == 1:
            count += 1
            bases[1] = 0
        if bases[0] == 1:
            count += 1
            bases[0] = 0
        count += 1
        user_score += count
        score_label2.config(text=f"{user_score}")
        update_bases()


    def com_base_on_balls():    #수비상황 볼넷
        global com_score
        if bases[0] == 0: #1루주자 없으면
            bases[0] = 1    #타자 1루로 이동
        else: #1루주자 있으면
            if bases[1] == 0:   #2루주자 없으면
                bases[1] = 1    #1루주자 2루로 이동
                bases[0] = 1 #타자 1루로 이동
            else:  #2루주자 있으면
                if bases[2] == 0:   #3루주자 없으면
                    bases[2] = 1    #2루주자 3루로 이동
                    bases[1] = 1    #1루주자 2루로 이동
                    bases[0] = 1    #타자 1루로 이동
                else:   #3루주자 있으면(만루)
                    com_score += 1  #3루주자 홈으로 득점, 여전히 만루상황
                    score_label4.config(text=f"{com_score}") #점수판 업데이트
                    bases[2] = 1
                    bases[1] = 1
                    bases[0] = 1
        update_bases()  #베이스 업데이트


    def user_base_on_balls():    #공격상황 볼넷
        global user_score
        if bases[0] == 0:
            bases[0] = 1
        else:
            if bases[1] == 0:
                bases[1] = 1
                bases[0] = 1
            else:
                if bases[2] == 0:
                    bases[2] = 1
                    bases[1] = 1
                    bases[0] = 1
                else:
                    user_score += 1
                    score_label2.config(text=f"{user_score}")
                    bases[2] = 1
                    bases[1] = 1
                    bases[0] = 1
        update_bases()


    def update_bases():
        if bases[0] == 1: #1루에 주자 있으면
            base_label1.config(bg="green")   # 1루 베이스 활성화, 배경색 변경
        if bases[1] == 1: #2루에 주자 있으면
            base_label2.config(bg="green")   # 2루 베이스 활성화, 배경색 변경
        if bases[2] == 1: #3루에 주자 있으면
            base_label3.config(bg="green")   # 3루 베이스 활성화, 배경색 변경
        if bases[0] == 0: #1루에 주자 없으면
            base_label1.config(bg="white")   # 1루 베이스 비활성화, 배경색 변경
        if bases[1] == 0: #2루에 주자 없으면
            base_label2.config(bg="white")   # 2루 베이스 비활성화, 배경색 변경
        if bases[2] == 0: #3루에 주자 없으면
            base_label3.config(bg="white")   # 3루 베이스 비활성화, 배경색 변경


    def game_finish():  #게임종료
        judge() #승자판단
        root2 = Toplevel(root1) #새로운 윈도우 생성
        root2.geometry("600x400")
        root2.resizable(False, False)
        root2.title("야구게임")
        empty_label3 = Label(root2, text="", font=("Arial", 40))
        empty_label3.pack()
        finish_label1 = Label(root2, text="게임종료", font=("Arial", 60))
        finish_label1.pack()
        empty_label4 = Label(root2, text="", font=("Arial", 40)) #결과를 알려줄 라벨
        empty_label4.pack()
        finish_label2 = Label(root2, text=f"{result}", font=("Arial", 40))
        finish_label2.pack()
        empty_label5 = Label(root2, text="", font=("Arial", 40))
        empty_label5.pack()
        replay_bt = Button(root2, text="다시시작", width=5, height=2, command=replay) #다시시작 버튼
        replay_bt.place(x=200, y=300)
        quit_bt = Button(root2, text="게임종료", width=5, height=2, command=quit_game)  #게임종료 버튼
        quit_bt.place(x=320, y=300)


    def judge(): #승자판단
        global com_score
        global user_score
        global result
        if com_score > user_score:
            result = "YOU LOSE"
        elif com_score < user_score:
            result = "YOU WIN"
        else:
            result = "DRAW"
    

    def replay(): #게임 다시시작
        global com_score
        global user_score
        global inning
        global bases
        com_score = 0   #점수초기화
        user_score = 0
        inning = 1 #이닝초기화
        bases = [0, 0, 0]   #베이스초기화
        root1.destroy() #창닫고
        play() #게임다시시작

    
    def quit_game():
        root1.destroy() #윈도우닫고 게임종료

        

    root1 = Toplevel(root)
    root1.geometry("900x800")
    root1.resizable(False, False)
    root1.title("야구게임")

    image1 = PhotoImage(file="/Users/songjihun/Desktop/파이썬프로젝트/야구선수.png")    #야구선수 이미지
    image_label1 = Label(root1, image=image1)
    image_label1.place(x=530, y=50)


    rbt = IntVar() #9개의 라디오버튼 묶음

    #9개의 라디오버튼에 1~9의 value 할당
    
    frame1 = Frame(root1, bg="white", relief="solid", borderwidth=1)
    frame1.place(x=306, y=316, width=65, height=85)
    rbt1 = Radiobutton(frame1, value=1, variable=rbt, bg="white")
    rbt1.pack(fill=BOTH, expand=True)

    frame2 = Frame(root1, bg="white", relief="solid", borderwidth=1)
    frame2.place(x=370, y=316, width=65, height=85)
    rbt2 = Radiobutton(frame2, value=2, variable=rbt, bg="white")
    rbt2.pack(fill=BOTH, expand=True)

    frame3 = Frame(root1, bg="white", relief="solid", borderwidth=1)
    frame3.place(x=434, y=316, width=65, height=85)
    rbt3 = Radiobutton(frame3, value=3, variable=rbt, bg="white")
    rbt3.pack(fill=BOTH, expand=True)

    frame4 = Frame(root1, bg="white", relief="solid", borderwidth=1)
    frame4.place(x=306, y=400, width=65, height=85)
    rbt4 = Radiobutton(frame4, value=4, variable=rbt, bg="white")
    rbt4.pack(fill=BOTH, expand=True)

    frame5 = Frame(root1, bg="white", relief="solid", borderwidth=1)
    frame5.place(x=370, y=400, width=65, height=85)
    rbt5 = Radiobutton(frame5, value=5, variable=rbt, bg="white")
    rbt5.pack(fill=BOTH, expand=True)

    frame6 = Frame(root1, bg="white", relief="solid", borderwidth=1)
    frame6.place(x=434, y=400, width=65, height=85)
    rbt6 = Radiobutton(frame6, value=6, variable=rbt, bg="white")
    rbt6.pack(fill=BOTH, expand=True)

    frame7 = Frame(root1, bg="white", relief="solid", borderwidth=1)
    frame7.place(x=306, y=484, width=65, height=85)
    rbt7 = Radiobutton(frame7, value=7, variable=rbt, bg="white")
    rbt7.pack(fill=BOTH, expand=True)

    frame8 = Frame(root1, bg="white", relief="solid", borderwidth=1)
    frame8.place(x=370, y=484, width=65, height=85)
    rbt8 = Radiobutton(frame8, value=8, variable=rbt, bg="white")
    rbt8.pack(fill=BOTH, expand=True)

    frame9 = Frame(root1, bg="white", relief="solid", borderwidth=1)
    frame9.place(x=434, y=484, width=65, height=85)
    rbt9 = Radiobutton(frame9, value=9, variable=rbt, bg="white")
    rbt9.pack(fill=BOTH, expand=True)

    #공던지기 버튼, 공격수비 바뀔때마다 text와 command 바뀜
    bt1 = Button(root1, text="던지기", command=defend,font=("Arial, 20"))
    bt1.place(x=360, y=600, width=90, height=60)

    #공격,수비 안내 라벨
    play_label1 = Label(root1, text="수비", font=("Arial", 20))
    play_label1.place(x=50, y=110)
    play_label2 = Label(root1, text="공격", font=("Arial", 20))     
    play_label2.place(x=50, y=160)
    play_label3 = Label(root1, text=f"{inning}회 초", font=("Arail, 20"))
    play_label3.place(x=100, y=60)

    #스트라이크, 볼, 아웃 등 메세지 라벨
    result_label1 = Label(root1, text="", font=("Arial", 20))
    result_label1.place(x=80, y=460)
    result_label2 = Label(root1, text=f"B: {b_count}  S: {s_count}", font=("Arial", 20))
    result_label2.place(x=80, y=490)
    result_label3 = Label(root1, text=f"O: {o_count}", font=("Arial", 20))
    result_label3.place(x=80, y=520)

    #베이스상황 안내 라벨
    base_label1 = Label(root1, text="1루", width=5, height=3, bg="white", relief="solid", bd=1)
    base_label1.place(x=128, y=330)
    base_label2 = Label(root1, text="2루", width=5, height=3, bg="white", relief="solid", bd=1)
    base_label2.place(x=80, y=330)
    base_label3 = Label(root1, text="3루", width=5, height=3, bg="white", relief="solid", bd=1)
    base_label3.place(x=80, y=381)

    id = id_entry.get() #입력받은 아이디

    #점수판생성
    score_label1 = Label(root1, text=f"{id}", width=10, height=3, bg="white", relief="solid", bd=1)
    score_label1.place(x=100, y=100)
    score_label2 = Label(root1, text="0", width=6, height=3, bg="white", relief="solid", bd=1)
    score_label2.place(x=193, y=100)
    score_label3 = Label(root1, text="COM", width=10, height=3, bg="white", relief="solid", bd=1)
    score_label3.place(x=100, y=151)
    score_label4 = Label(root1, text="0", width=6, height=3, bg="white", relief="solid", bd=1)
    score_label4.place(x=193, y=151)


    
    root1.mainloop()

#전역변수
inning = 1
b_count = 0
s_count = 0
o_count = 0
bases = [0, 0, 0]
com_score = 0
user_score = 0
result = ""

#초기윈도우
root = Tk()
root.geometry("400x270")
root.resizable(False, False)
root.title("야구게임")

empty_label0 = Label(root, text="", font=("Arail", 40))
empty_label0.pack()

id_label1 = Label(root, text="닉네임을 입력하세요:", font=("Arail", 30))
id_label1.pack()

empty_label1 = Label(root, text="", font=("Arail", 15))
empty_label1.pack()

#아이디 입력 박스
id_entry = Entry(root)
id_entry.pack()

empty_label2 = Label(root, text="", font=("Arail", 15))
empty_label2.pack()

#게임시작버튼
play_bt = Button(root, text="게임시작", width=5, height=2, command=play)
play_bt.pack()

root.mainloop()