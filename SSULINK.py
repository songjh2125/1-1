from tkinter import *
from tkinter import messagebox

users = {}  # 회원 정보를 저장할 딕셔너리

def register():
    def save_user():
        username = entry_username.get()
        password = entry_password.get()

        if username and password:
            if username in users:
                messagebox.showerror("회원가입 실패", "이미 존재하는 아이디입니다.")
            else:
                users[username] = password
                messagebox.showinfo("회원가입 완료", "회원가입이 완료되었습니다.")
                register_window.destroy()
        else:
            messagebox.showerror("입력 오류", "사용자 이름과 비밀번호를 입력해주세요.")

    # 새로운 회원가입 창 생성
    register_window = Toplevel(win1)
    register_window.title("회원가입")
    register_window.geometry("300x200")
    register_window.resizable(False, False)

    empty_label1 = Label(register_window)
    empty_label1.pack()

    label_username = Label(register_window, text="ID")
    label_username.pack()
    entry_username = Entry(register_window)
    entry_username.pack()

    label_password = Label(register_window, text="비밀번호")
    label_password.pack()
    entry_password = Entry(register_window, show="*")
    entry_password.pack()

    empty_label2 = Label(register_window)
    empty_label2.pack()

    btn_save = Button(register_window, text="완료", command=save_user)
    btn_save.pack()

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username] == password:
        messagebox.showinfo("로그인 성공", "로그인에 성공했습니다.")
        mainwindow()
        win1.destroy()
    else:
        messagebox.showerror("로그인 실패", "잘못된 사용자 이름 또는 비밀번호입니다.")


def mainwindow():#메인 화면

    def exwindow():#운동 매칭

        def create_match():
            create_window = Toplevel(exwin)
            create_window.title("새로운 매치 생성")
            create_window.geometry("800x400")

            def add_new_button(place, date, activity, member, exwin):
                answer = messagebox.askquestion("확인", "생성하시겠습니까?")
                if answer == "yes":
                    button_text = f"장소: {place} \n 날짜, 시간: {date} \n 활동내용: {activity} \n 참여인원: 1/{member}"
                    button = Button(exwin, text=button_text, width=70, height=7, command=lambda: increase_count(button))
                    button.pack()
                    create_window.destroy()
                else:
                    create_window.destroy()

            # Entry 위젯 생성
            place_label = Label(create_window, text="장소:", font=("배달의민족 주아 OTF", 20))
            place_label.place(x=100, y=100)

            entry_place = Entry(create_window, width=50)
            entry_place.place(x=200, y=100)

            date_label = Label(create_window, text="날짜, 시간:", font=("배달의민족 주아 OTF", 20))
            date_label.place(x=100, y=140)

            entry_date = Entry(create_window, width=50)
            entry_date.place(x=200, y=140)

            activity_label = Label(create_window, text="활동내용:", font=("배달의민족 주아 OTF", 20))
            activity_label.place(x=100, y=180)

            entry_activity = Entry(create_window, width=50)
            entry_activity.place(x=200, y=180)

            member_label = Label(create_window, text="참여인원:", font=("배달의민족 주아 OTF", 20))
            member_label.place(x=100, y=220)

            entry_member = Entry(create_window, width=10)
            entry_member.place(x=200, y=220)

            member_label2 = Label(create_window, text="명", font=("배달의민족 주아 OTF", 20))
            member_label2.place(x=300, y=220)

            # 완료 버튼 생성
            btn_done = Button(create_window, text="완료", command=lambda: add_new_button(entry_place.get(), entry_date.get(), entry_activity.get(), entry_member.get(), exwin))
            btn_done.place(x=350, y=300)

        def increase_count(btn):
            members = btn["text"].split("\n")[3].split(":")[1].split("/")
            current_count = int(members[0])
            total_count = int(members[1])

            if current_count == total_count:
                messagebox.showerror("실패", "마감된 매치입니다.")

            elif current_count < total_count:
                # 확인 메시지 띄우기
                answer = messagebox.askquestion("확인", "신청하시겠습니까?")
                if answer == "yes":
                    current_count += 1
                    btn_text = btn["text"].split("\n")
                    btn_text[3] = f" 참여인원: {current_count}/{total_count}"
                    btn["text"] = "\n".join(btn_text)
            


        # 메인 창 생성
        exwin = Tk()
        exwin.title("운동 매칭")
        exwin.geometry("1200x700")
        exwin.resizable(False, False)

        empty_label1 = Label(exwin)
        empty_label1.pack()

        # 초기 버튼 생성
        create_match_button = Button(exwin, width=10, height=2, text="새로운 매치 생성", command=create_match)
        create_match_button.pack()

        empty_label2 = Label(exwin)
        empty_label2.pack()

        # 이벤트 루프 시작
        exwin.mainloop()



    def volwindow():#봉사활동 매칭

        def create_match():
            create_window = Toplevel(volwin)
            create_window.title("새로운 활동 생성")
            create_window.geometry("800x400")

            def add_new_button(place, date, activity, member, volwin):
                answer = messagebox.askquestion("확인", "생성하시겠습니까?")
                if answer == "yes":
                    button_text = f"장소: {place} \n 날짜, 시간: {date} \n 활동내용: {activity} \n 참여인원: 1/{member}"
                    button = Button(volwin, text=button_text, width=70, height=7, command=lambda: increase_count(button))
                    button.pack()
                    create_window.destroy()
                else:
                    create_window.destroy()

            # Entry 위젯 생성
            place_label = Label(create_window, text="장소:", font=("배달의민족 주아 OTF", 20))
            place_label.place(x=100, y=100)

            entry_place = Entry(create_window, width=50)
            entry_place.place(x=200, y=100)

            date_label = Label(create_window, text="날짜, 시간:", font=("배달의민족 주아 OTF", 20))
            date_label.place(x=100, y=140)

            entry_date = Entry(create_window, width=50)
            entry_date.place(x=200, y=140)

            activity_label = Label(create_window, text="활동내용:", font=("배달의민족 주아 OTF", 20))
            activity_label.place(x=100, y=180)

            entry_activity = Entry(create_window, width=50)
            entry_activity.place(x=200, y=180)

            member_label = Label(create_window, text="참여인원:", font=("배달의민족 주아 OTF", 20))
            member_label.place(x=100, y=220)

            entry_member = Entry(create_window, width=10)
            entry_member.place(x=200, y=220)

            member_label2 = Label(create_window, text="명", font=("배달의민족 주아 OTF", 20))
            member_label2.place(x=300, y=220)

            # 완료 버튼 생성
            btn_done = Button(create_window, text="완료", command=lambda: add_new_button(entry_place.get(), entry_date.get(), entry_activity.get(), entry_member.get(), volwin))
            btn_done.place(x=350, y=300)

        def increase_count(btn):
            members = btn["text"].split("\n")[3].split(":")[1].split("/")
            current_count = int(members[0])
            total_count = int(members[1])

            if current_count == total_count:
                messagebox.showerror("실패", "마감된 활동입니다.")

            elif current_count < total_count:
                # 확인 메시지 띄우기
                answer = messagebox.askquestion("확인", "신청하시겠습니까?")
                if answer == "yes":
                    current_count += 1
                    btn_text = btn["text"].split("\n")
                    btn_text[3] = f" 참여인원: {current_count}/{total_count}"
                    btn["text"] = "\n".join(btn_text)
            


        # 메인 창 생성
        volwin = Tk()
        volwin.title("봉사활동 매칭")
        volwin.geometry("1200x700")
        volwin.resizable(False, False)

        empty_label1 = Label(volwin)
        empty_label1.pack()

        # 초기 버튼 생성
        create_match_button = Button(volwin, width=10, height=2, text="새로운 활동 생성", command=create_match)
        create_match_button.pack()

        empty_label2 = Label(volwin)
        empty_label2.pack()

        # 이벤트 루프 시작
        volwin.mainloop()



    def studywindow():#스터디 매칭

        def create_match():
            create_window = Toplevel(stwin)
            create_window.title("새로운 스터디 생성")
            create_window.geometry("800x400")

            def add_new_button(place, date, activity, member, stwin):
                answer = messagebox.askquestion("확인", "생성하시겠습니까?")
                if answer == "yes":
                    button_text = f"장소: {place} \n 날짜, 시간: {date} \n 활동내용: {activity} \n 참여인원: 1/{member}"
                    button = Button(stwin, text=button_text, width=70, height=7, command=lambda: increase_count(button))
                    button.pack()
                    create_window.destroy()
                else:
                    create_window.destroy()

            # Entry 위젯 생성
            place_label = Label(create_window, text="장소:", font=("배달의민족 주아 OTF", 20))
            place_label.place(x=100, y=100)

            entry_place = Entry(create_window, width=50)
            entry_place.place(x=200, y=100)

            date_label = Label(create_window, text="날짜, 시간:", font=("배달의민족 주아 OTF", 20))
            date_label.place(x=100, y=140)

            entry_date = Entry(create_window, width=50)
            entry_date.place(x=200, y=140)

            activity_label = Label(create_window, text="활동내용:", font=("배달의민족 주아 OTF", 20))
            activity_label.place(x=100, y=180)

            entry_activity = Entry(create_window, width=50)
            entry_activity.place(x=200, y=180)

            member_label = Label(create_window, text="참여인원:", font=("배달의민족 주아 OTF", 20))
            member_label.place(x=100, y=220)

            entry_member = Entry(create_window, width=10)
            entry_member.place(x=200, y=220)

            member_label2 = Label(create_window, text="명", font=("배달의민족 주아 OTF", 20))
            member_label2.place(x=300, y=220)

            # 완료 버튼 생성
            btn_done = Button(create_window, text="완료", command=lambda: add_new_button(entry_place.get(), entry_date.get(), entry_activity.get(), entry_member.get(), stwin))
            btn_done.place(x=350, y=300)

        def increase_count(btn):
            members = btn["text"].split("\n")[3].split(":")[1].split("/")
            current_count = int(members[0])
            total_count = int(members[1])

            if current_count == total_count:
                messagebox.showerror("실패", "마감된 스터디입니다.")

            elif current_count < total_count:
                # 확인 메시지 띄우기
                answer = messagebox.askquestion("확인", "신청하시겠습니까?")
                if answer == "yes":
                    current_count += 1
                    btn_text = btn["text"].split("\n")
                    btn_text[3] = f" 참여인원: {current_count}/{total_count}"
                    btn["text"] = "\n".join(btn_text)
            


        # 메인 창 생성
        stwin = Tk()
        stwin.title("스터디 매칭")
        stwin.geometry("1200x700")
        stwin.resizable(False, False)

        empty_label1 = Label(stwin)
        empty_label1.pack()

        # 초기 버튼 생성
        create_match_button = Button(stwin, width=10, height=2, text="새로운 스터디 생성", command=create_match)
        create_match_button.pack()

        empty_label2 = Label(stwin)
        empty_label2.pack()

        # 이벤트 루프 시작
        stwin.mainloop()


    mainwin = Tk()
    mainwin.title("SSULINK")
    mainwin.geometry("1200x700")
    mainwin.resizable(False, False)
    
    mainwin_label_1 = Label(mainwin)
    mainwin_label_1.config(text = "SSU LINK",font=("배달의민족 주아 OTF", 60))
    mainwin_label_1.pack()
    
    mainwin_button_1 = Button(mainwin,text = "운동 매칭", width=15, height=5, font=("배달의민족 주아 OTF",30),command=exwindow)
    mainwin_button_1.place(x = 30, y = 250)
    
    mainwin_button_2 = Button(mainwin,text = "봉사 활동 매칭", width=15, height=5, font=("배달의민족 주아 OTF",30), command=volwindow)
    mainwin_button_2.place(x =430, y = 250)
    
    mainwin_button_3 = Button(mainwin,text = "스터디 매칭", width=15, height=5, font=("배달의민족 주아 OTF",30), command=studywindow)
    mainwin_button_3.place(x = 830, y = 250)


# 메인 창 생성
win1 = Tk()
win1.title("로그인 및 회원가입")
win1.geometry("400x250")
win1.resizable(False, False)

empty_label1 = Label(win1)
empty_label1.pack()

label_username = Label(win1, text="ID")
label_username.pack()
entry_username = Entry(win1)
entry_username.pack()

label_password = Label(win1, text="비밀번호")
label_password.pack()
entry_password = Entry(win1, show="*")
entry_password.pack()

empty_label2 = Label(win1)
empty_label2.pack()

btn_login = Button(win1, text="로그인", width=5, height=1, command=login)
btn_login.pack()

btn_register = Button(win1, text="회원가입", width=5, height=1, command=register)
btn_register.pack()


win1.mainloop()


