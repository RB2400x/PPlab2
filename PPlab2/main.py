from tkinter import *
def wincheck():
    winner = ''
    # проверки:
    for r in range(3):
        if area[r][0]['text'] == area[r][1]['text'] == area[r][2]['text']!='': winner = area[r][0]['text'];break # строка
    for c in range(3):
        if area[0][c]['text'] == area[1][c]['text'] == area[2][c]['text']!='': winner = area[0][c]['text'];break # столбец
    if area[0][0]['text'] == area[1][1]['text'] == area[2][2]['text']!='': winner = area[0][0]['text']# основная диагональ
    if area[0][2]['text'] == area[1][1]['text'] == area[2][0]['text']!='': winner = area[0][2]['text']# побочная диагональ
    if winner=='x': return 1
    elif winner=='o': return 2
    else:
        return 0
def off():
    for r in range(3):
        for c in range(3):
            area[r][c].config(state="disabled")
def handler(btn: Button):
    global move
    if move%2!=0:
        sign = 'x'
        turn = "Ход ноликов"
    else:
        sign = 'o'
        turn = "Ход крестиков"
    btn.config(text=sign, font=("Arial", 100))
    btn.config(state="disabled")
    move += 1
    check = wincheck()
    if check==1:
        turn = "Крестики победили"
        off()
    elif check==2:
        turn = "Нолики победили"
        off()
    elif check==0 and move==10:
        turn = "Ничья"
    label.config(text=turn)
menu=Tk()
menu.title('Крестики-нолики')
menu.geometry('450x450')
label = Label(menu, text="Ход крестиков", font=("Arial", 14))
label.grid(row=0, column=0, columnspan = 3)
for r in range(1,4): menu.rowconfigure(index = r, weight = 1)
for c in range(3): menu.columnconfigure(index = c, weight = 1)
move = 1
area = [[1,2,3],[4,5,6],[7,8,9]]
for r in range(1,4):
    for c in range(3):
        btn = Button(height=10, width=30, font=("Arial", 100), state='normal',command=lambda lr=r, lc=c: handler(area[lr-1][lc]))# lr - lambda r, lc - lambda c
        btn.grid(row=r, column=c)
        area[r-1][c]=btn
menu.mainloop()