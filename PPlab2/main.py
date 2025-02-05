from tkinter import *
def wincheck(area):
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
def off(area):# выключение оставшихся кнопок поля при победе
    for r in range(3):
        for c in range(3):
            area[r][c].config(state="disabled")
def handler(btn: Button, label, area, move):# обработчик для кнопок поля
    if move[0]%2!=0:
        sign = 'x'
        turn = "Ход ноликов"
    else:
        sign = 'o'
        turn = "Ход крестиков"
    btn.config(text=sign, font=("Arial", 100))
    btn.config(state="disabled")
    move[0] += 1
    check = wincheck(area)
    if check==1:
        turn = "Крестики\n победили"
        off(area)
    elif check==2:
        turn = "Нолики\n победили"
        off(area)
    elif check==0 and move[0]==10:
        turn = "Ничья"
    label.config(text=turn)
def replay(area, label, move):
    for r in range(3):
        for c in range(3):
            area[r][c].config(text='' ,state="normal")
    move[0] = 1
    label['text']="Ход крестиков" # - можно обращаться напрямую, а не делать label.config(text="Ход крестиков")
def play():
    game=Tk()
    game.title('Крестики-нолики')
    game.geometry('450x600')
    label = Label(game, text="Ход крестиков", font=("Arial", 14))
    label.grid(row=0, column=1)
    for r in range(1,4): game.rowconfigure(index = r, weight = 1)
    for c in range(3): game.columnconfigure(index = c, weight = 1)
    move = [1]
    area = [[1,2,3],[4,5,6],[7,8,9]]
    for r in range(1,4):
        for c in range(3):
            btn = Button(height=10, width=30, font=("Arial", 100), state='normal',command=lambda lr=r, lc=c: handler(area[lr-1][lc], label, area, move))# lr - lambda r, lc - lambda c
            btn.grid(row=r, column=c)
            area[r-1][c]=btn
    restart = Button(height=4, width=9, font=("Arial", 12), state='normal', text='Перезапуск', command=lambda: replay(area, label, move))
    restart.grid(row=0, column=0, sticky=W)
    close = Button(height=4, width=9, font=("Arial", 12), state='normal', text='Выход', command=lambda: game.destroy())
    close.grid(row=0, column=2, sticky=E)
    game.mainloop()
play()
