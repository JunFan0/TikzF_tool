import copy
import random
import time
import numpy as np

def get_type_num(data):
    num_liste=1
    # judge whether data has been in number list
    num_list=[str(i) for i in range(10)]
    for i in range(len(data)):
        if data[i] not in num_list:
            num_liste=0
    return num_liste

def reform_list_str(data_s):
    data_F=copy.deepcopy(data_s)
    for e in range(len(data_F)):
        if get_type_num(data_F[e][0]) or (data_F[e][0] in [str(i) for i in range(10)]):
            data_F[e][0]="a"+data_F[e][0]
    for e in range(len(data_F)):
        if get_type_num(data_F[e][2]) or (data_F[e][2] in [str(i) for i in range(10)]):
            data_F[e][2]="a"+data_F[e][2]
    return data_F
            
def trans_txt(list_toplo):
    #####################################################
    #
    #该函数将list的数字转化为可运行的latex代码
    #
    #####################################################
    # initial parameters
    # this variable is used saving latex code of direction
    direction = [f'\\vertex ({str(list_toplo[0][0])});']
    # this variable is used saving what the point name is
    direction_point = [f'\\vertex ({str(list_toplo[0][0])})' + '{'+f"{list_toplo[0][0]}"+'};']
    
    # this variable is used saving latex code of line
    latex_code=[]
    # this variable is used saving latex code of line name    
    latex_code2=[]
    # direction 
    direct_str=['above',
                'above right',
                'right',
                'below right',
                'below',
                'below left',
                'left',
                'above left']
    
    line_style=['plain',
               'boson',
               'charged boson',
               'photon',
               'scalar',
               'charge scalar',
               'ghost', 
               'fermion',
               'majiorana',
               'gloun']
    loop_style=['half left','quarter left']
    # count_num
    line_num=1
    label_p=[]#储存已经被标记的点，防止出现重复标示改点。
    
    for ele in list_toplo:
        if len(ele)<4:
            tx = f"({(ele[0])}) --[fermion] ({ele[2]}),"
            txl = f"({(ele[0])}) --[plain, edge label'=l{line_num}] ({ele[2]}),"
        else:
            if ele[4]!=0:
                tx = f"({(ele[0])}) --[{line_style[ele[3]]},{loop_style[ele[4]-1]}] ({ele[2]}),"  
                txl = f"({(ele[0])}) --[plain,{loop_style[ele[4]-1]},edge label'=l{line_num}] ({ele[2]}),"
            else:
                tx = f"({(ele[0])}) --[{line_style[ele[3]]}] ({ele[2]}),"
                txl = f"({(ele[0])}) --[plain, edge label'=l{line_num}] ({ele[2]}),"       
        dr = f"\\vertex [{direct_str[ele[1]]} =of {(ele[0])}] ({(ele[2])});"
        latex_code.append(tx)
        latex_code2.append(txl)
        direction.append(dr)
        line_num+=1
        label_p.append(ele[2])
    l=len(label_p)-1

    for i in range(l):
        if(label_p[i] in label_p[i+1:]):
            drp = f"\\vertex [{direct_str[list_toplo[i][1]]} =of {(list_toplo[i][0])}] ({(list_toplo[i][2])});"
        else:
            drp = f"\\vertex [{direct_str[list_toplo[i][1]]} =of {(list_toplo[i][0])}] ({(list_toplo[i][2])})"+\
            '{'+f"{list_toplo[i][2]}"+'};'
        direction_point.append(drp)
            
    drp = f"\\vertex [{direct_str[list_toplo[l][1]]} =of {(list_toplo[l][0])}] ({(list_toplo[l][2])})"\
            +'{'+f"{list_toplo[l][2]}"+'};'        
    direction_point.append(drp)
    return latex_code,latex_code2,direction,direction_point

def arrange_list(data):
    # 该函数将实际连线的写法转化为Tizk-feynman里面的书写习惯
    # 将给定的列表转化为1位置的元素必定在前方0位置元素的列表。
    # new_list储存原始的edge
    # real_list储存实际画的线，因为有些线可能写反，假设初始点为1，[2，1]很可能不被加入，因为2可能只是1的后续点。
    new_list=[]
    real_new_list=[]
    judge_list=[data[0][0]]
    for i in range(len(data)):
        for j in range(len(data)):
            if((data[j][0] in judge_list) and (data[j] not in new_list)):
                new_list.append(data[j])
                judge_list.append(data[j][2])
                real_new_list.append(data[j])
            elif((data[j][2] in judge_list) and (data[j] not in new_list)):
                  data_mid=copy.deepcopy(data[j])
                  data_mid[0]=data[j][2]
                  data_mid[2]=data[j][0]
                  data_mid[1]=output_direction(data[j][1])
                  judge_list.append(data[j][0])
                  new_list.append(data[j])
                  real_new_list.append(data_mid)
    return  real_new_list    

def gene_latex_code(edge_info=[],show=1):
    try:
        strq=np.load('data.npy')
        for s in strq:
            print(type(s[1]))
    except:
        print('please check your file and input.')
    # 输出latexcode的函数,show控制是否显示名称
    s1=["\\documentclass{standalone}",
        "\\usepackage{graphicx}",
        "\\usepackage{tikz-feynman}",
        "\\begin{document}",
        "\\begin{tikzpicture}",
        "\\begin{feynman}"]
    
    s2=["\\diagram*",
        "{"]
    
    s3=["};",
        "\\end{feynman};",
        "\\end{tikzpicture}",
        "\\end{document}"]
    #测试用fenyman diagram
    if (len(edge_info)==0):
        edge_info=[['1',3,'2',1,1],['2',4,'4',1,1],['2',3,'3',1,1],['3',2,'6',1,1],['6',1,'7',1,1],['3',5,'4',1,1],['4',5,'5',1,1],['6',3,'8',1,1],['8',1,'9',1,1],['9',4,'10',1,1],['8',3,'10',1,1],['9',1,'11',1,1],['10',3,'12',1,1]]    
        random.shuffle(edge_info)
    edge_info=arrange_list(edge_info)
    edge_info=reform_list_str(edge_info)
    re=trans_txt(edge_info)
    if show==0:
        a=re[0]
        b=re[2]
    elif show==1:
        a=re[1]
        b=re[3]

    with open(f'图{int(time.time())%1000000}.tex','w') as file:
        for sn in s1+b+s2+a+s3:
            file.write(sn+'\n')
    np.save('data.npy',edge_info)

def output_direction(num):
    num1=((num+4)%7)-1
    if num1>=0:
        return num1
    else:
        return num1+8
        
if __name__ == "__main__":
    
    gene_latex_code(show=0)








