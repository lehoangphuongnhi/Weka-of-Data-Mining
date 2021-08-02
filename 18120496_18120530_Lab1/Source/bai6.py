import pandas as pd 
import sys 
from function_support import create_list

#ham xoa nhung dong co du lieu trung nhau
#table: truyen bang du lieu
#tra ve bang khong con du lieu trung
def XoaDongTrungDulieu(table):
    #set luu bang du lieu khong trung lap
    notloop = set()
    i = 0
    a = []
    #a = [0]*len(table[0][1])#mot mang luu gia tri thuoc tinh tung dong
    while i < len(table[0][1]): #duyet tungdong
        j = 0
        while j < len(table):#duyet thuoc tinh tung dong
            if str(table[j][1][i]) == 'nan':
                a.append(str(table[j][1][i]))
                j += 1
            else:
                a.append(table[j][1][i])
                j += 1
        i += 1
        b = a
        notloop.add(tuple(b))
        a = []
        j = 0
    return notloop

if __name__ == '__main__':

    print('Number of arguments:', len(sys.argv), 'arguments. Argument List:', str(sys.argv))

    if len(sys.argv) < 3:
        print("To run: `python filename.csv`")
        print("WARMING: Must be provided enough argument!\n")
    else:
        filename = str(sys.argv[1])#lay ten file csv can doc
        table = []
        table = create_list(filename)#tao bang du lieu
        #ghi du lieu vao file
        data = pd.read_csv(filename)
        l = (list)(data)
        df = pd.DataFrame(XoaDongTrungDulieu(table), columns = l)
        df.to_csv(sys.argv[2], index = False)