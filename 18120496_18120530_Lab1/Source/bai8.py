import sys 
from function_support import create_list, create_file
def KtThuocTinhNum(table, attr):
    j = 0 #bien dem thuoc tinh
    while j < (len(attr) - 3):
        i = 0
        while i < len(table): #duyet cac cot
            t = 0#bien dem dong
            while t < len(table[i][1]):#duyet tung dong
                if type(table[i][1][t]) == str and attr[j + 2] == str(table[i][0]) and str(table[i][1][t])!='nan':#neu kieu du lieu co cai nào la string thi thoat
                    print('truyen thuoc tinh dua vao khong phai la thuoc tinh numeric')
                    return False
                t += 1
            i += 1
        j += 2
    return True
#ham tinh toan thuoc tinh theo mot bieu thuc cho truoc
#table: la bang du lieu
#attr: danh sach chua thuoc tinh va cac toan tu
def TinhThuocTinh(table, attr):
    i = 0 #bien dem 
    a = []#mang luu gia tinh toan cac thuoc tinh
    j = 0
    while j < (len(attr) - 3):
        i = 0
        while i < len(table):#duyet cac cot
            if attr[j + 2] == str(table[i][0]) and j == 0:#neu ten cot trung thi thuc hien phep tinh, va day la so hang dau
                t = 0 #bien dem dong
                while t < len(table[i][1]):#duyet tung dong
                    if(str(table[i][1][t])=='nan'):#bi thieu du lieu
                        a.append(str(table[i][1][t]))
                    else:
                        a.append(table[i][1][t])#them dong vao mang a
                    t += 1
            elif attr[j + 2] == str(table[i][0]):#neu ten cot trung, thi thuc hien phep tinh
                t = 0
                while t < len(table[i][1]):#duyet tung dong
                    if((str(table[i][1][t]) == 'nan') or (a[t] == 'nan') or(a[t] == '')):#bi thieu du lieu
                        a[t] = ''#cho gia tri tai dong bang rong
                        t += 1
                        continue
                    if str(attr[3]) == '*':
                        a[t] = a[t]* table[i][1][t]
                    elif str(attr[3]) == '/':
                        if  table[i][1][t] != 0:#neu chia cho /0 thi sai
                            a[t] = a[t] / table[i][1][t]
                        else:
                            a[t] = ''
                    elif str(attr[3]) == '+':
                        a[t] = a[t] + table[i][1][t]
                    else:
                        a[t] = a[t] - table[i][1][t]
                    t += 1
            i +=1
        j +=1

    #them cot vua tinh vao bang du lieu
    table.append(['Tinh', a])
    return table

if __name__ == '__main__':

    print('Number of arguments:', len(sys.argv), 'arguments. Argument List:', str(sys.argv))

    if len(sys.argv) < 4:
        print("To run: `python filename.csv`")
        print("WARMING: Must be provided enough argument!\n")
    else:
        filename = str(sys.argv[1])#lay ten file csv can doc
        table = []
        table = create_list(filename)#tao bang du lieu
        if KtThuocTinhNum(table, sys.argv):
            #print("sdifhsdkj")
            table = TinhThuocTinh(table, sys.argv)
            #print(table)
            create_file(table, sys.argv[len(sys.argv) - 1])
    