# import random

# while True:
#     choice = input('Roll the dice? (Y/N)').lower()
#     if choice == 'y':
#         die1 = random.randint(1,6)
#         die2 = random.randint(1,6)
#         print(f'{die1} , {die2}')
#     elif choice == 'n':
#         print('Thanks for playing!')
#         break
#     else:
#         print('Invalid chioce!')
# end Code
# 

from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title("Dice Roll Simulator")
root.geometry("300x250")

# قائمة الصور
lis = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']

# إنشاء عناصر واجهة المستخدم
label1 = Label(root, text="اختر رقم (1-6):", font=('Helvetica', 10))
label1.place(x=5, y=5)

label2 = Label(root, text="رمي النرد؟ (Y/N)", font=('Helvetica', 10))
label2.place(x=150, y=5)

Entry1 = Entry(root)
Entry1.place(x=5, y=30)

Entry2 = Entry(root)
Entry2.place(x=150, y=30)

label3 = Label(root, text="🎲")  # عنصر الصورة الافتراضي
label3.place(x=200, y=160)

label4 = Label(root, text="🎲")  # عنصر الصورة الافتراضي
label4.place(x=5, y=160)

def photo_numbers():
    """تحديث الصورة بناءً على الإدخال"""
    try:
        number = int(Entry1.get())  # الحصول على الرقم المدخل
        yn = Entry2.get().lower()  # تحويل الإدخال إلى lowercase

        if yn == 'y' and 1 <= number <= 6:  # التحقق من صحة الإدخال
            image_path = lis[number - 1]  # الحصول على الصورة المناسبة
            image = Image.open(image_path)
            image = image.resize((80, 80))  # تغيير الحجم
            photo = ImageTk.PhotoImage(image)
            label3.config(image=photo)
            label3.image = photo  # الاحتفاظ بالصورة في الذاكرة
        elif yn == 'n':
            label3.config(text="Thanks for playing!", image="")
        else:
            label3.config(text="Invalid choice!", image="")
    except ValueError:
        label3.config(text="❌ أدخل رقم صحيح!", image="")

def chioces():
    """اختيار صورة عشوائية"""
    choice = random.choice(lis)
    image = Image.open(choice)
    image = image.resize((80, 80))  # تغيير الحجم
    photo = ImageTk.PhotoImage(image)
    label4.config(image=photo)
    label4.image = photo  # الاحتفاظ بالصورة في الذاكرة

def roll():
    photo_numbers()
    chioces()

# زر تشغيل اللعبة
button0 = Button(root, text='Play', bg='green', command=roll)
button0.place(x=125, y=60)

# تشغيل الواجهة الرسومية
root.mainloop()






