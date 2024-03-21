from tkinter import *
from tkinter import messagebox  
import random
import time

INITIAL_BALANCE = 1000000     

def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

def display_dice_images():
    for i in range(10):  
        dice_results = [random.randint(1, 6) for _ in range(3)]  
        for j in range(3):
            small_dice_labels[j].config(image=dice_images[dice_results[j] - 1])
            window.update()
            time.sleep(0.1) 
    total = sum(dice_results)
    result_text.set(f"Dice 1: {dice_results[0]}\nDice 2: {dice_results[1]}\nDice 3: {dice_results[2]}\nTotal: {total}")
    if 4 <= total <= 10:
        result_text.set(result_text.get() + "\nXỉu")
        return "Xỉu"
    elif 11 <= total <= 17:
        result_text.set(result_text.get() + "\nTài")
        return "Tài"
    else:
        result_text.set(result_text.get() + "\nBộ ba đồng nhất")
        return "Bộ ba đồng nhất"

def play_game(is_tai):
    global balance  
    bet_amount = bet_entry.get()
    try:
        bet_amount = int(bet_amount)
    except ValueError:
        messagebox.showerror("Lỗi", "Số tiền cược không hợp lệ!")
        return
    if bet_amount <= 0:
        messagebox.showerror("Lỗi", "Số tiền cược phải lớn hơn 0!")
        return
    if bet_amount > balance:
        messagebox.showerror("Lỗi", "Số tiền cược lớn hơn số dư của bạn!")
        return
    result = display_dice_images()
    if (is_tai and result == "Tài") or (not is_tai and result == "Xỉu"):
        balance += bet_amount  
        show_result_message(True)
    else:
        balance -= bet_amount 
        show_result_message(False)
    update_balance_label()  
    
def update_balance_label():
    balance_label.config(text=f"Số dư: {balance} đồng")

def show_result_message(is_win):
    result_message = Toplevel(window)
    result_message.title("Kết quả")
    screen_width = result_message.winfo_screenwidth()
    screen_height = result_message.winfo_screenheight()
    result_message.geometry(f"{screen_width}x{screen_height}")
    bg_image = PhotoImage(file="bg.png")
    bg_label = Label(result_message, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)
    if is_win:
        photo = PhotoImage(file="upsocial.png")
        result_label = Label(result_message, image=photo)
        result_label.image = photo
        result_label.pack(pady=10)
        message = "Bạn đã đoán đúng!"
    else:
        photo = PhotoImage(file="downsocial.png")
        result_label = Label(result_message, image=photo)
        result_label.image = photo
        result_label.pack(pady=10)
        message = "Bạn đã đoán sai!"
    message_label = Label(result_message, text=message, font=("Arial", 14), bg="white", fg="black")
    message_label.pack(pady=10)
    exit_button = Button(result_message, text="Thoát", command=result_message.destroy)
    exit_button.pack(pady=10)

window = Tk()
window.title("Tài xỉu")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.config(bg="white")

bg_image = PhotoImage(file="bg.png")
bg_label = Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

balance = INITIAL_BALANCE  

result_text = StringVar()
result_label = Label(window, textvariable=result_text, font=("Arial", 20), bg="white")
result_label.grid(row=0, column=0, padx=20, pady=20, rowspan=3)

bet_frame = Frame(window, bg="white")
bet_frame.grid(row=0, column=1, padx=20, pady=20) 

Label(bet_frame, text="Số tiền cược:", font=("Arial", 14), bg="white").pack(side=LEFT, padx=10)
bet_entry = Entry(bet_frame, font=("Arial", 14), width=10)
bet_entry.pack(side=LEFT, padx=5)

tai_button = Button(window, text="Chọn Tài", font=("Arial", 16), command=lambda: play_game(True))
tai_button.grid(row=1, column=1, padx=20, pady=10) 
xiu_button = Button(window, text="Chọn Xỉu", font=("Arial", 16), command=lambda: play_game(False))
xiu_button.grid(row=2, column=1, padx=20, pady=10)

balance_label = Label(window, text=f"Số dư: {balance} đồng", font=("Arial", 16), bg="white")
balance_label.grid(row=3, column=1, padx=20, pady=20)  

dice_images = [PhotoImage(file=f"dice{i} (Custom).png") for i in range(1, 7)]

small_dice_labels = [Label(window) for _ in range(3)]
for j, label in enumerate(small_dice_labels):
    label.config(image=dice_images[0])
    label.place(relx=(j + 1) / 4, rely=0.5, anchor=CENTER)

window.mainloop()
