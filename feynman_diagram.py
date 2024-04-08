import tkinter as tk
import numpy as np
import feyn_function as fey

class fey_window(object):
    # 暂时不支持修改窗体大小
    def __init__(self):
        self.edge_info_list = []#储存边的信息
        self.list_item = []#储存listbox显示的信息 
        self.main_win_size=[600,600]
        self.theme_color="#fafafa"#窗口颜色
        self.font_size = 15
        self.win_width = 130#左边栏的大小
        self.win_alpha = .98#主窗体的透明度
        self.particle_height = 35#线型及相同frame1单选框的高度
        self.listbox_height = 470
        self.third_frame_height = 30 #sec4中控件的高label_height=30
        self.label_height=30#thirdfame1中控件的宽度
        self.label_font=('宋体',13)#thirdfame1中控件的字体
        self.entry_fontsize=('宋体',12)#listbox的文字大小
        self.scrollbar_width=20#滚动条的宽度
        self.button_width =int((self.main_win_size[0]-self.win_width)/4)-1#button宽度
        
        self.main_win=tk.Tk()
        self.var1=tk.StringVar()#储存entry1的内容
        self.var2=tk.StringVar()#储存entry2的内容
        self.var3=tk.IntVar()#储存方位的信息
        self.var_particle = tk.IntVar()#存储线型的变量
        self.list_b_size = tk.IntVar()#储存listbox的大小变量
        self.var_particle_ex = tk.IntVar()#储存圈的形状的变量
        self.var_particle_name_show=tk.IntVar()#储存是否显示名称的变量
        self.edge_info=tk.StringVar()#储存listbox的信息
        
        self.particle = ['plain',
                       'boson', 
                       'charged boson', 
                       'photon', 
                       'scalar', 
                       'charge scalar', 
                       'ghost', 
                       'fermion',
                       'majiorana',
                       'gloun']#线型的显示名称
        self.line_type_ex = ['basic line type',
                             'half',
                             'quarter']#圈的单选框名称
        self.line_type_name_show=['隐藏',
                                  '显示']#控制是否显示名称单选框的名称
        self.button_name=['添加',
                          '删除',
                          '清除',
                          '保存']#button的名称
        self.list_direction=[
                                '↑',
                                '↗',
                                '→',
                                '↘',
                                '↓',
                                '↙',
                                '←',
                                '↖', 
                                    ]#radiobutton显示的方向
        self.list_direction_chs=[
                                    '上',
                                    '右上',
                                    '右',
                                    '右下',
                                    '下',
                                    '左下',
                                    '左',
                                    '左上', 
                                ]#listbox显示的方向
        self.comm_list=[self.add_command,
                        self.delete_command,
                        self.clear_command,
                        self.save_command]#button初始化函数
        #控件

        # 创建菜单栏
        self.menu_bar = tk.Menu(self.main_win,
                                background=self.theme_color)
        ## 添加file菜单
        self.file_menu = tk.Menu(self.menu_bar, 
                            tearoff=False,
                            background=self.theme_color,
                            activebackground="#ffffff")
        ## 添加help菜单
        self.help_menu = tk.Menu(self.menu_bar, 
                                 tearoff=False,
                                 background=self.theme_color,
                                 activebackground="#ffffff")
        ##添加底层frame
        self.bottom_frame = tk.Frame(self.main_win,
                                     background=self.theme_color,
                                     height=self.main_win_size[0],
                                     width=self.main_win_size[1])
        ###添加第二层frame1
        self.sec_frame1 = tk.Frame(self.bottom_frame,
                                   background=self.theme_color,
                                   height=self.main_win_size[1]-1,
                                   width=self.win_width)
        ####基本线型的label
        self.particle_name_label=tk.Label(self.sec_frame1,
                                          text="基本线型   ",
                                          background="#f2f2f2",
                                          anchor='s')
        ####基本线型单选框
        for i in range(len(self.particle)):
            tk.Radiobutton(self.sec_frame1, 
                              text=self.particle[i], 
                              variable=self.var_particle, 
                              value=i, 
                              anchor='w',
                              #background='white',
                              background="#f5f5f7",
                              relief='solid',
                              borderwidth=1,
                              activebackground='#ffffff')
        ####圈所在的frame
        self.circle_frame=tk.Frame(self.sec_frame1,
                                    background="#ffffff")
        #####圈label
        self.label_circle=tk.Label(self.circle_frame,
                                   text="圈   ",
                                   background="#f2f2f2",
                                   anchor='s')
        #####圈的形状的单选框
        for i in range(len(self.line_type_ex)):
            tk.Radiobutton( self.circle_frame, 
                            text=self.line_type_ex[i], 
                            variable=self.var_particle_ex, 
                            value=i, 
                            anchor='w',
                            #background='white',
                            background="#f5f5f7",
                            relief='solid',
                            borderwidth=1,
                            activebackground='#ffffff')
        #####是否显示名称的标签
        self.label_point_name=tk.Label(self.circle_frame,
                                       text='名称')
        #####名称标签
        for i in range(len(self.line_type_name_show)):
            tk.Radiobutton(self.circle_frame, 
                                 text=self.line_type_name_show[i], 
                                 variable=self.var_particle_name_show, 
                                 value=i, 
                                 anchor='w',
                                 #background='white',
                                 background="#f5f5f7",
                                 relief='solid',
                                 borderwidth=1,
                                 activebackground='#ffffff')
        ###设置分割线frame2
        self.sec_frame2 = tk.Frame(self.bottom_frame,
                                   background=self.theme_color,
                                   height=self.main_win_size[1],
                                   width=1)
        ###设置listbox所在的frame3
        self.sec_frame3 = tk.Frame(self.bottom_frame,
                                   background=self.theme_color,
                                   height=self.listbox_height,
                                   width=self.main_win_size[0]-1-self.win_width)
        ####
        self.scr1=tk.Scrollbar(self.sec_frame3)
        ####创建在sframe3的listbox
        self.list_b=tk.Listbox(self.sec_frame3,
                               font=('宋体',15),
                               listvariable=self.edge_info, 
                               yscrollcommand=self.scr1.set,
                               selectbackground='#4facfe',
                               selectmode=tk.EXTENDED)
        ###设置frame4它有entry以及保存按钮等控件
        self.sec_frame4 = tk.Frame(self.bottom_frame,
                                   background=self.theme_color,
                                   height=self.main_win_size[1]-self.listbox_height,
                                   width=600-2-self.win_width,
                                   borderwidth=1,
                                   relief='sunken')
        ####创建thframe1在sframe4上
        self.third_frame1 = tk.Frame(self.sec_frame4,
                                     background=self.theme_color)
        #####设置起点label在thframe1
        self.start_point = tk.Label(self.third_frame1,
                                    text='起始点',
                                    width=10,
                                    font=self.label_font,
                                    background=self.theme_color,
                                     relief='solid',
                                    borderwidth=1)
        #####设置entry在thframe1
        self.start_point_entry=tk.Entry(self.third_frame1,
                                        textvariable=self.var1, 
                                        font=self.entry_fontsize)
        ####创建thframe3在sframe4上
        self.third_frame3 = tk.Frame(self.sec_frame4,
                                     background=self.theme_color)
        #####设置起点label在thframe3
        self.end_point = tk.Label(self.third_frame3,
                                    text='终点',
                                    width=10,
                                    font=self.label_font,
                                    background=self.theme_color,
                                     relief='solid',
                                    borderwidth=1)
        #####设置entry在thframe3
        self.end_point_entry=tk.Entry(self.third_frame3,
                                        textvariable=self.var2, 
                                        font=self.entry_fontsize)
        ####创建thframe2在sframe上
        self.third_frame2=tk.Entry(self.sec_frame4,
                                   textvariable=self.var1, 
                                   font=self.entry_fontsize)
        #####创建表示方向单选框在thframe2上
        for i in range(len(self.list_direction)):
            tk.Radiobutton(self.third_frame2, 
                           text=self.list_direction[i], 
                           variable=self.var3, 
                           value=i,
                           anchor='w',
                           background=self.theme_color,
                           font=10)
        ####创建thframe4在sframe上
            self.third_frame4 = tk.LabelFrame(self.sec_frame4,
                                              background=self.theme_color)
        #####创建功能保存等button在thframe4上
        for i in range(4):
            tk.Button(self.third_frame4,
                      text=self.button_name[i],
                      font=self.font_size,
                      background=self.theme_color,
                      command=self.comm_list[i],
                      anchor=tk.CENTER) 
        self._init_window()



    def _init_window(self):
        #初始化控件的放置及设置变量的初值
        #主窗体
        self.main_win.title('Feynman Diagram')
        self.main_win.geometry(f'{str(self.main_win_size[0])}x{str(self.main_win_size[1])}')#窗体大小
        self.main_win.attributes('-alpha',.98)#窗体透明度
        self.main_win.resizable(0,0)
        self.main_win.config(menu=self.menu_bar)
        ##file菜单
        self.menu_bar.add_cascade(label="文件", 
                                  menu=self.file_menu)
        self.file_menu.add_command(label="保存", 
                                   command=self.save_command)
        self.file_menu.add_separator()  # 添加分隔线
        self.file_menu.add_command(label="退出", 
                                   command=self.on_quit)
        ##help菜单
        self.menu_bar.add_cascade(label="帮助", 
                                  menu=self.help_menu)
        self.help_menu.add_command(label="帮助文档")
        ##最底层frame
        self.bottom_frame.place(x=0,y=0)
        ###sframe1
        self.sec_frame1.place(x=0,y=0)
        ####基本线型label
        self.particle_name_label.place(x=0,y=0,
                                       height=25,
                                       width=self.win_width)
        ####基本线型单选框
        self.list_b_size.set(0)
        self.var_particle.set(0)
        for i in range(len(self.sec_frame1.winfo_children()[:11])):
            if i !=0:
                self.sec_frame1.winfo_children()[i].place(x=0,
                                                          y=self.particle_height*(i-1)+25,
                                                          width=self.win_width+1,
                                                          height=self.particle_height)
        ####圈所在的frame
        self.circle_frame.place(x=0, y=self.particle_height*10+25,
                                height=self.main_win_size[1]-self.particle_height*len(self.particle)-15,
                                width=self.win_width)
        #####圈label
        self.label_circle.place(x=0,y=0,
                                height=25,
                                width=self.win_width)
        #####圈的形状
        for i in range(len(self.circle_frame.winfo_children()[:len(self.line_type_ex)+1])):
            if i !=0:
                self.circle_frame.winfo_children()[i].place(x=0, y=self.particle_height*(i-1)+25,
                                                            width=self.win_width+1,
                                                            height=self.particle_height)
                
        #####是否显示名称的标签
        self.label_point_name.place(x=0,y=self.particle_height*3+25,
                                    height=25,
                                    width=self.win_width)
        #####名称标签
        for i in range(len(self.circle_frame.winfo_children()[len(self.line_type_ex)+1:])):
            if i >0:
                self.circle_frame.winfo_children()[i+1+len(self.line_type_ex)].place(x=0, 
                                                                                   y=self.particle_height*(i+2)+25*2,
                                                                                   width=self.win_width+1,
                                                                                   height=self.particle_height)
        
        ###分割线sframe2
        self.sec_frame2.place(x=self.win_width+1,y=0)
        ###sframe3
        self.sec_frame3.place(x=self.win_width+2,y=0)
        ####
        self.scr1.place(x=450,y=0,
                        height=self.listbox_height,
                        width=self.scrollbar_width)
        ####sframe3的listbox
        self.list_b.place(x=0, y=0, 
                          height=self.listbox_height, 
                          width=self.main_win_size[0]-1-self.win_width)
        ###frame4
        self.sec_frame4.place(x=self.win_width+1,
                              y=self.listbox_height+1)
        ####thframe1在sframe4上
        self.third_frame1.place(x=0,y=0,
                                height=self.third_frame_height,
                                width=self.main_win_size[0]-1-self.win_width)
        #####起点label在thframe1
        self.start_point.place(x=0,y=0,
                               width=100,
                               height=self.label_height)
        #####entry在thframe1
        self.var1.set('请输入起始点')
        self.start_point_entry.place(x=100,y=0,
                                     height=self.label_height,
                                     width=self.main_win_size[0]-self.win_width-4)
        ####thframe3在sframe4上
        self.third_frame3.place(x=0,y=self.third_frame_height*2,
                                height=self.third_frame_height,
                                width=self.main_win_size[0]-1-self.win_width)
        #####起点label在thframe3
        self.end_point.place(x=0,y=0,
                               width=100,
                               height=self.label_height)
        #####entry在thframe3
        self.var2.set('请输入终点')
        self.end_point_entry.place(x=100,y=0,
                                     height=self.label_height,
                                     width=self.main_win_size[0]-self.win_width-4)
        ####thframe2在sframe
        self.third_frame2.place(x=0,y=self.third_frame_height,
                                height=self.third_frame_height,
                                width=self.main_win_size[0]-self.win_width)
        #####表示方向单选框在thframe2
        for i in range(len(self.third_frame2.winfo_children())):
            self.third_frame2.winfo_children()[i].place(x=0+58*(i),
                                                        y=0,
                                                        width=62,
                                                        height=self.label_height)
        ####thframe4在sframe
        self.third_frame4.place(x=0,y=self.third_frame_height*3,
                                height=self.third_frame_height+10,
                                width=self.main_win_size[0]-1-self.win_width)
        #####功能保存等button在thframe4
        for i in range(len(self.third_frame4.winfo_children())):
            self.third_frame4.winfo_children()[i].place(x=self.button_width*i,y=0,
                                                        height=self.label_height+5,
                                                        width=self.button_width)
        try:
            edge_init=np.load('data.npy')
            for i in range(len(edge_init)):
                print_s=f'点{edge_init[i][2]}在点{edge_init[i][0]}的'+\
                        f'{self.list_direction_chs[int(edge_init[i][1])]}方,'+\
                        f'线型为{self.particle[int(edge_init[i][3])]}'
                self.list_b.insert('end',print_s)
                self.edge_info_list.append([edge_init[i][0],
                                            int(edge_init[i][1]),
                                            edge_init[i][2],
                                            int(edge_init[i][3]),
                                            int(edge_init[i][4])])
        except:
            print('没有找到data.npy文件')
        
        self.main_win.mainloop()
            
    def on_quit(self):
        # 退出菜单的函数
        self.main_win.quit()

    def add_command(self):
        # 排除latex内置的符号防止因字符引起的报错
        for s in str(self.var1.get()):
            if s in ['$','&','%','#','_','{','}','^','\\','～','|',',',';']:
                self.var1.set('请检查输入')
                return 0
        for s in str(self.var2.get()):
            if s in ['$','&','%','#','_','{','}','^','\\','～','|',',',';']:
                self.var2.set('请检查输入')
                return 0
        self.list_b_size=self.list_b.size()
        if self.list_b_size>=24:
            self.list_b.config(width=self.main_win_size[0]-self.win_width-self.scrollbar_width)
            self.scr1.place(x=450,y=0,
                            height=self.listbox_height,
                            width=self.scrollbar_width)
            self.scr1.update()
        edge=[str(self.var1.get()),
              self.var3.get(),
              str(self.var2.get()),
              self.var_particle.get(),
              self.var_particle_ex.get()]
        print_s=f'点{edge[2]}在点{edge[0]}的{self.list_direction_chs[edge[1]]}方,线型为{self.particle[edge[3]]}'
        self.edge_info_list.append(edge)
        self.list_b.insert('end',print_s)
    
    def delete_command(self):
        element_number=self.list_b.size()
        for i in range(element_number):
            if(self.list_b.select_includes(element_number-1-i)==True):
                self.list_b.delete(element_number-1-i)
                del self.edge_info_list[element_number-1-i]
    
    def clear_command(self):
        element_number=self.list_b.size()
        for i in range(element_number):
            self.list_b.delete(element_number-i-1)
            del self.edge_info_list[element_number-1-i]
        self.var1.set('')
        self.var2.set('')
    
    def save_command(self):
        fey.gene_latex_code(edge_info=self.edge_info_list,
                            show=self.var_particle_name_show.get())

if __name__ == "__main__":
    ob=fey_window()