from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry("1030x780")
root.title("Quiz")
root.config(bg="lightblue")
Label(root,text=" Programming Quiz  ",font='impack 28 bold',fg="blue",bg="lightblue").place(x=300,y=2)


java = (
    (
        "1. Who is known as the Father of win?",
        ("Dennis Ritchie", "James Gosling", "Bjarne Stroustrup", "Guido van Rossum"),
        "James Gosling"
    ),
    (
        "2. What is the full form of JVM?",
        ("win Variable Machine", "win Virtual Machine", "win Verified Machine", "win Vendor Machine"),
        "win Virtual Machine"
    ),
    (
        "3. Which keyword is used for inheritance in win?",
        ("implements", "extends", "inherit", "super"),
        "extends"
    ),
    (
        "4. Which company originally developed win?",
        ("Microsoft", "Oracle", "Sun Microsystems", "IBM"),
        "Sun Microsystems"
    ),
    (
        "5. win is a _____ language.",
        ("Procedural", "Machine", "Object Oriented", "Assembly"),
        "Object Oriented"
    ),
    (
        "6. Which method starts a win program?",
        ("start()", "run()", "main()", "execute()"),
        "main()"
    ),
    (
        "7. Which keyword creates an object?",
        ("create", "new", "class", "object"),
        "new"
    ),
    (
        "8. Which package is imported automatically?",
        ("java.io", "java.util", "java.lang", "java.net"),
        "java.lang"
    ),
    (
        "9. win source file extension is?",
        (".class", ".exe", ".java", ".jar"),
        ".java"
    )
)
python = (
    (
        "1. Who developed Python?",
        ("Dennis Ritchie", "James Gosling", "Guido van Rossum", "Bjarne Stroustrup"),
        "Guido van Rossum"
    ),
    (
        "2. Python was released in?",
        ("1989", "1991", "1995", "2000"),
        "1991"
    ),
    (
        "3. Which symbol is used for comments?",
        ("//", "#", "/*", "--"),
        "#"
    ),
    (
        "4. Which function prints output?",
        ("echo()", "display()", "print()", "show()"),
        "print()"
    ),
    (
        "5. Which function takes input?",
        ("scan()", "input()", "get()", "read()"),
        "input()"
    ),
    (
        "6. Python is a _____ language.",
        ("Compiled", "Assembly", "Interpreted", "Machine"),
        "Interpreted"
    ),
    (
        "7. List is represented by?",
        ("{}", "()", "[]", "<>"),
        "[]"
    ),
    (
        "8. Tuple is represented by?",
        ("[]", "{}", "()", "<>"),
        "()"
    ),
    (
        "9. Dictionary is represented by?",
        ("[]", "{}", "()", "<>"),
        "{}"
    ),
    (
        "10. Which keyword defines a function?",
        ("function", "fun", "def", "define"),
        "def"
    )
)
javascript = (
    (
        "1. Who developed JavaScript?",
        ("Brendan Eich", "James Gosling", "Guido van Rossum", "Dennis Ritchie"),
        "Brendan Eich"
    ),
    (
        "2. JavaScript was created in?",
        ("1995", "1991", "2000", "1985"),
        "1995"
    ),
    (
        "3. JavaScript file extension is?",
        (".java", ".py", ".js", ".jsx"),
        ".js"
    ),
    (
        "4. Which tag is used for JavaScript in HTML?",
        ("<java>", "<script>", "<js>", "<javascript>"),
        "<script>"
    ),
    (
        "5. Which function prints output in browser?",
        ("print()", "console.log()", "echo()", "show()"),
        "console.log()"
    ),
    (
        "6. Which keyword declares a variable?",
        ("var", "int", "string", "float"),
        "var"
    ),
    (
        "7. Modern variable keyword is?",
        ("let", "int", "float", "char"),
        "let"
    ),
    (
        "8. Constant variable keyword?",
        ("let", "var", "const", "fixed"),
        "const"
    ),
    (
        "9. Which symbol is used for comments?",
        ("#", "//", "--", "**"),
        "//"
    ),
    (
        "10. JavaScript is a _____ language.",
        ("Compiled", "Interpreted", "Assembly", "Machine"),
        "Interpreted"
    ),
    (
        "11. Which function shows alert box?",
        ("alert()", "message()", "show()", "popup()"),
        "alert()"
    )
)


def start_quiz(questions, title):
    win = Toplevel(root)
    win.config(bg="lightblue")
    win.geometry("1050x790")
    win.title(title)
#Timer set===================================================================================================================================
    def countdown():
     nonlocal time_left

     if time_left > 0:
        timer_label.config(text=f"Time Left: {time_left}")
        time_left -= 1
        win.after( 1000,countdown)

     else:
      win.destroy()
      show_result(score, len(questions))
      
#===========================================================================================================================================
    current_question = 0
    score = 0
    time_left = 120
    
#frame-----------------------------------------------------------------------------------------
    top_frame = Frame(win, bg="lightblue")
    top_frame.pack(fill="x")
#--------------------------------------------------------------------------------------------------
    timer_label = Label(top_frame,text="Time Left: 60",font=("Arial",16,"bold"),fg="black",bg="lightblue")
    timer_label.pack(side="right",anchor="n")
#total questions====================================================================================================================
    total=Label(top_frame,text=f"Total Questions:{len(questions)}",fg="black",font=("Arial",16,"bold"),bg="lightblue")
    total.pack(side="right",anchor="n")
#========================================================================================================================================
    answer = StringVar()
    question_label = Label(win,text="",font=("Arial", 20, "bold"),bg="lightblue",wraplength=900)
    question_label.pack(pady=40)

    r1 = Radiobutton(win, variable=answer, font=("Arial", 16),bg="lightblue")
    r2 = Radiobutton(win, variable=answer, font=("Arial", 16),bg="lightblue")
    r3 = Radiobutton(win, variable=answer, font=("Arial", 16),bg="lightblue")
    r4 = Radiobutton(win, variable=answer, font=("Arial", 16),bg="lightblue")

    r1.pack(anchor="w", padx=50, pady=5)
    r2.pack(anchor="w", padx=50, pady=5)
    r3.pack(anchor="w", padx=50, pady=5)
    r4.pack(anchor="w", padx=50, pady=5)

    def load_question():

        question_label.config(text=questions[current_question][0])

        r1.config(text=questions[current_question][1][0],value=questions[current_question][1][0] )
        r2.config(text=questions[current_question][1][1],value=questions[current_question][1][1])
        r3.config(text=questions[current_question][1][2],value=questions[current_question][1][2])
        r4.config(text=questions[current_question][1][3],value=questions[current_question][1][3])

        answer.set("")


#next button===============================================================================================================================        

    def next_question():

        nonlocal current_question
        nonlocal score

        if answer.get() == "":
            messagebox.showerror("Error","Please select an answer")
            return

        if answer.get() == questions[current_question][2]:
            score += 1

        current_question += 1

        if current_question < len(questions):
            load_question()

        else:
            win.destroy()
            show_result(score, len(questions))

    def exit_quiz():
     value = messagebox.askyesno("Exit","Are you sure you want to exit the quiz?")
     if value:
        win.destroy()

    Button(top_frame,text="Exit Quiz",bg="red",command=exit_quiz).pack(side=RIGHT, padx=15,anchor="n")

#bottom Frame
    bottom_frame = Frame(win,bg="lightblue")
    bottom_frame.pack(pady=20)
    Button(bottom_frame,text="Save",font=("Arial",16,"bold"),bg="yellow").pack(side=LEFT,padx=10)
    Button(bottom_frame,text="Next",font=("Arial",16,"bold"),bg="red",command=next_question).pack(side=LEFT,padx=10)
   
    load_question()
    countdown()

#==================================================================================================================================================
def open_quiz():

    quiz = Toplevel(root)
    quiz.geometry("1050x790")
    quiz.config(bg="lightblue")
    quiz.title("Quiz Test")

    Button(quiz,text='JAVA',font='impack 18 bold',bg='blue',fg='white',width=36,height=2,bd=5,command=lambda: start_quiz(java, "win Quiz")).place(x=300,y=200)
    Button(quiz,text='PYTHON',font='impack 18 bold',bg='green',fg='white',width=36,height=2,bd=5,command=lambda: start_quiz(python, "Python Quiz")).place(x=300,y=300)
    Button(quiz,text='JAVASCRIPT',font='impack 18 bold',bg='red',fg='white',width=36,height=2,bd=5,command=lambda: start_quiz(javascript, "JavaScript Quiz")).place(x=300,y=400)

#------------------------------------------------------------------------------------------------------------------------------------------------    

#Registration ------------------------------------------------------------------------==========================================================
f1=LabelFrame(root,text='Registration',borderwidth=4,font='impack 28 bold',bg="grey",bd=5)
f1.place(x=250,y=50, width=500, height=700)
Label(f1,text="Name:",font='impack 20 bold',bg="grey").place(x=0,y=45)
Label(f1,text="D.O.B:",font='impack 20 bold',bg="grey").place(x=0,y=145)
Label(f1,text="Email:",font='impack 20 bold',bg="grey").place(x=0,y=245)
Label(f1,text="Mobile No.:",font='impack 20 bold',bg="grey").place(x=0,y=345)
Label(f1,text="Password:",font='impack 20 bold',bg="grey").place(x=0,y=445)

#entry
e1=Entry(f1,bd=1,font='impack 20 bold',width=20)
e1.place(x=130,y=45)
e2=Entry(f1,bd=1,font='impack 20 bold',width=20)
e2.place(x=130,y=145)
e3=Entry(f1,bd=1,font='impack 20 bold',width=20)
e3.place(x=130,y=245)
e4=Entry(f1,bd=1,font='impack 20 bold',width=18)
e4.place(x=160,y=345)
e5=Entry(f1,bd=1,font='impack 20 bold',width=18,show="*")

e5.place(x=160,y=445)




def submit():
    if e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="":
     messagebox.showerror("Error","Please fill all details")
    else:
       value=messagebox.askyesno("Information","Are all details correct?")
       if value:
          messagebox.showinfo("Information","Student Added Successfully")
          ready=value=messagebox.askyesno("Info","Are you ready for exam?")
          if ready:
             open_quiz()
             root.withdraw()
             
Button(f1,text="Sumbit",font='impack 20 bold',bg="lightblue",command=submit).place(x=150,y=580,width=200)

#result---------------------------------------------------------------------------------

def show_result(score, total):
    result = Toplevel(root)
    result.geometry("500x400")
    result.title("Quiz Result")
    result.config(bg="lightgreen")

    percentage = (score / total) * 100

    Label(result,text="QUIZ RESULT",font=("Arial", 24, "bold"),bg="lightgreen",fg="blue").pack(pady=20)

    Label(result,text=f"Score: {score}/{total}",font=("Arial", 18, "bold"),bg="lightgreen").pack(pady=10)

    Label(result,text=f"Percentage: {percentage:.2f}%",font=("Arial", 18, "bold"),bg="lightgreen").pack(pady=10)

    if percentage >= 40:
        result_text = "PASS "
        color = "green"
    else:
        result_text = "FAIL "
        color = "red"

    Label(result,text=result_text,font=("Arial", 22, "bold"),fg=color,bg="lightgreen"
    ).pack(pady=20)

    Button(result,text="Close",command=result.destroy,bg="red",fg="white").pack(pady=20)
root.mainloop()


















