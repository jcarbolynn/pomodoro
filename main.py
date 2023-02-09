from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
  window.after_cancel(timer)
  timer_label.config(text="Timer", fg=GREEN)
  canvas.itemconfig(timer_text, text="00:00")
  check_marks.configure(text="")
  global reps
  reps = 0
  # timer text to 00:00
  # title_label to "Timer"
  # reset check marks

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
  # * 60 to get time in seconds
  global reps
  reps += 1
  
  work_sec = WORK_MIN *60
  long_break_sec = LONG_BREAK_MIN *60
  short_break_sec = SHORT_BREAK_MIN *60

  if reps % 8 == 0:
    count_down(long_break_sec)
    timer_label.config(text="Break", fg=RED)
  elif reps % 2 == 0:
    count_down(short_break_sec)
    timer_label.config(text="Break", fg=PINK)
  else:
    count_down(work_sec)
    timer_label.config(text="Work", fg=GREEN)

  # if reps % 2 != 0:
  #   count_down(work_sec)
  # if reps % 2 == 0:
  #   if reps % 8 == 0:
  #     count_down(long_break_sec)
  #   else:
  #     count_down(short_break_sec)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math
def count_down(count):
  global reps
  minutes = math.floor(count / 60)
  seconds = count % 60
  if minutes < 10:
    minutes = f"0{minutes}"
  if seconds < 10:
    seconds = f"0{seconds}"

  canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
  if (count > 0):
    global timer
    timer = window.after(1000, count_down, count-1)
  else:
    # so that timer starts coiunting down again at next work/short break/long break
    timer_start()
    print(reps)
    marks = ""
    # need to round down because anything divided becomes a float
    work_sessions = math.floor(reps/2)
    for _ in range(0,work_sessions):
      marks += "✔"
    check_marks.configure(text=marks)
    # if reps%2 != 0:
    #   for _ in range(1,reps):
    #     check_marks.configure(text="✔")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height = 224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img)
# *args unlimited positional arguments, **kwargs unlimited key word arguments
timer_text = canvas.create_text(103,130,text="00:00", fill ="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1,row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer_label.grid(column=1,row=0)

check_marks = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
check_marks.grid(column=1,row=3)

start = Button(text="Start", command=timer_start)
start.grid(column=0,row=2)

reset = Button(text="Reset", command=timer_reset)
reset.grid(column=2,row=2)




window.mainloop()
