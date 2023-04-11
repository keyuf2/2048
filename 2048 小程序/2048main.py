import tkinter as tk
import numpy as np      
import random          

win = tk.Tk() #创建窗口
win.title("2048")  
win.geometry("410x600")  
win.resizable(width=True, height=True) 
# 创建画布
canvas = tk.Canvas(win, width=410, height=410, bg="tan")  
num_color = ['bisque','peru', 'moccasin', 'cyan', 'deepskyblue', 'dodgerblue', 'blue', 'coral','gold', 'fuchsia','purple','pink']       
num = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]  
a = [[0, 2, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] #初始化

# 把matrix 放到 Canvas 上
for i in range(0,4):
    for j in range(0,4):
        num_index=num.index(a[i][j])
        if a[i][j] == 0: #0 的时候
            canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100, fill='bisque',
                                    outline='wheat')
        else:#有值赋颜色和number
            canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100, fill=num_color[num_index],
                                    outline='wheat') 
            canvas.create_text(100 * j + 55, 100 * i + 55, text=a[i][j], font=('Time New Roman', 35),
                               fill='maroon')
canvas.pack()
def up():
    global a
    b=[]#将向上转化为二维数组
    print(a)
    for i in range(0,4):
        b.append([])
        for j in range(0,4):
            b[i].append(a[j][i])

    
    #剔除0
    for i in range(0,4):
        for j in range(0,4):
            if b[i][j] == 0:
                b[i].remove(0)
                b[i].append(0)
    #计算
    for i in range(0,4):
        if b[i][0] == b[i][1]:
            b[i][0] = 2 * b[i][0]
            if b[i][2] == b[i][3]:
                b[i][1] = 2 * b[i][2]
                b[i][2] = 0
                b[i][3] = 0
            else:
                b[i][1]=b[i][2]
                b[i][2]=b[i][3]
                b[i][3] = 0
        elif  b[i][1] == b[i][2]:
            b[i][1] = 2 * b[i][1]
            b[i][2] = b[i][3]
            b[i][3] = 0

        elif b[i][2] == b[i][3]:
            b[i][2] = 2 * b[i][2]
            b[i][3] = 0
          
    a=[]

   #装回去    
    for i in range(0,4):
        a.append([])
        for j in range(0,4):
            a[i].append(b[j][i])

    
    #随机生成新的元素
    r_i = []
    r_j = []
    for i in range(0, 4):
        for j in range(0, 4):
            if a[i][j] == 0:
                r_i.append(i)
                r_j.append(j)
    index_random = random.randint(0, len(r_i) - 1) 
    index_num = random.choice([2, 4]) 
    a[r_i[index_random]][r_j[index_random]] = index_num 

    #渲染颜色+放到 canvas 上
    for i in range(0,4):
        for j in range(0,4):
            num_index=num.index(a[i][j])
            if a[i][j] == 0: #0 的时候
                canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100, fill='bisque',
                                    outline='wheat')
            else:#有值赋颜色和number
                canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100, fill=num_color[num_index],
                                        outline='wheat') 
                canvas.create_text(100 * j + 55, 100 * i + 55, text=a[i][j], font=('Time New Roman', 35),
                               fill='maroon')

def down():
    global a
    b=[]#将向上转化为二维数组
    for i in range(0,4):
        b.append([])
        for j in range(0,4):
            b[i].append(a[3-j][i])
    
    #剔除0
    for i in range(0,4):
        for j in range(0,4):
            if b[i][j] == 0:
                b[i].remove(0)
                b[i].append(0)

   #计算
    for i in range(0,4):
        if b[i][0] == b[i][1]:
            b[i][0] = 2 * b[i][0]
            if b[i][2] == b[i][3]:
                b[i][1] = 2 * b[i][2]
                b[i][2] = 0
                b[i][3] = 0
            else:
                b[i][1]=b[i][2]
                b[i][2]=b[i][3]
                b[i][3] = 0
        elif  b[i][1] == b[i][2]:
            b[i][1] = 2 * b[i][1]
            b[i][2] = b[i][3]
            b[i][3] = 0

        elif b[i][2] == b[i][3]:
            b[i][2] = 2 * b[i][2]
            b[i][3] = 0
          
    a=[]

    #装回去    
    for i in range(0,4):
        a.append([])
        for j in range(0,4):
            a[i].append(b[3-j][i])
    
    #随机生成新的元素
    r_i = []
    r_j = []
    for i in range(0, 4):
        for j in range(0, 4):
            if a[i][j] == 0:
                r_i.append(i)
                r_j.append(j)
    index_random = random.randint(0, len(r_i) - 1) 
    index_num = random.choice([2, 4])  
    a[r_i[index_random]][r_j[index_random]] = index_num 

    #渲染颜色+放到 canvas 上
   #渲染颜色+放到 canvas 上
    for i in range(0,4):
        for j in range(0,4):
            num_index=num.index(a[i][j])
            if a[i][j] == 0: #0 的时候
                canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100, fill='bisque',
                                    outline='wheat')
            else:#有值赋颜色和number
                canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100, fill=num_color[num_index],
                                        outline='wheat') 
                canvas.create_text(100 * j + 55, 100 * i + 55, text=a[i][j], font=('Time New Roman', 35),
                               fill='maroon')

def left():
    global a
    b=[]#将向上转化为二维数组
    b = a
    
    #剔除0
    for i in range(0,4):
        for j in range(0,4):
            if b[i][j] == 0:
                b[i].remove(0)
                b[i].append(0)

       #计算
    for i in range(0,4):
        if b[i][0] == b[i][1]:
            b[i][0] = 2 * b[i][0]
            if b[i][2] == b[i][3]:
                b[i][1] = 2 * b[i][2]
                b[i][2] = 0
                b[i][3] = 0
            else:
                b[i][1]=b[i][2]
                b[i][2]=b[i][3]
                b[i][3] = 0
        elif  b[i][1] == b[i][2]:
            b[i][1] = 2 * b[i][1]
            b[i][2] = b[i][3]
            b[i][3] = 0

        elif b[i][2] == b[i][3]:
            b[i][2] = 2 * b[i][2]
            b[i][3] = 0
          
    a=[]

    #装回去    
    a = b

    #随机生成新的元素
    r_i = []
    r_j = []
    for i in range(0, 4):
        for j in range(0, 4):
            if a[i][j] == 0:
                r_i.append(i)
                r_j.append(j)
    index_random = random.randint(0, len(r_i) - 1) 
    index_num = random.choice([2, 4])  
    a[r_i[index_random]][r_j[index_random]] = index_num 

    #渲染颜色+放到 canvas 上
    for i in range(0,4):
        for j in range(0,4):
            num_index=num.index(a[i][j])
            if a[i][j] == 0: #0 的时候
                canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100, fill='bisque',
                                    outline='wheat')
            else:#有值赋颜色和number
                canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100, fill=num_color[num_index],
                                        outline='wheat') 
                canvas.create_text(100 * j + 55, 100 * i + 55, text=a[i][j], font=('Time New Roman', 35),
                               fill='maroon')


def right():
    global a
    b=[]#将向上转化为二维数组
    for i in range(0,4):
        b.append([])
        for j in range(0,4):
            b[i].append(a[i][3-j])
    
    #剔除0
    for i in range(0,4):
        for j in range(0,4):
            if b[i][j] == 0:
                b[i].remove(0)
                b[i].append(0)

    #计算
   #计算
    for i in range(0,4):
        if b[i][0] == b[i][1]:
            b[i][0] = 2 * b[i][0]
            if b[i][2] == b[i][3]:
                b[i][1] = 2 * b[i][2]
                b[i][2] = 0
                b[i][3] = 0
            else:
                b[i][1]=b[i][2]
                b[i][2]=b[i][3]
                b[i][3] = 0
        elif  b[i][1] == b[i][2]:
            b[i][1] = 2 * b[i][1]
            b[i][2] = b[i][3]
            b[i][3] = 0

        elif b[i][2] == b[i][3]:
            b[i][2] = 2 * b[i][2]
            b[i][3] = 0
          
    a=[]

    #装回去    
    for i in range(0,4):
        a.append([])
        for j in range(0,4):
            a[i].append(b[i][3-j])
    
    #随机生成新的元素
    r_i = []
    r_j = []
    for i in range(0, 4):
        for j in range(0, 4):
            if a[i][j] == 0:
                r_i.append(i)
                r_j.append(j)
    index_random = random.randint(0, len(r_i) - 1) 
    index_num = random.choice([2, 4])  
    a[r_i[index_random]][r_j[index_random]] = index_num 

    #渲染颜色+放到 canvas 上


    for i in range(0,4):
        for j in range(0,4):
            num_index=num.index(a[i][j])
            if a[i][j] == 0: #0 的时候
                canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100, fill='bisque',
                                    outline='wheat')
            else:#有值赋颜色和number
                canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100, fill=num_color[num_index],
                                        outline='wheat') 
                canvas.create_text(100 * j + 55, 100 * i + 55, text=a[i][j], font=('Time New Roman', 35),
                               fill='maroon')



    canvas.pack()
             


button1 = tk.Button(win, text="上", font=('楷体', 20), command=lambda:up())
button1.pack()
button2 = tk.Button(win, text="下", font=('楷体', 20), command=lambda:down())
button2.pack()
button1.bind("up", lambda:up())
button3 = tk.Button(win, text="左", font=('楷体', 20), command=lambda:left())
button3.pack()
button4 = tk.Button(win, text="右", font=('楷体', 20), command=lambda:right())
button4.pack()
win.mainloop()
