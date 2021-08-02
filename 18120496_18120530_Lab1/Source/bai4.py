import sys
from function_support import create_list, create_file
#ham kiem tra dong du lieu co thieu du lieu vuot qua nguong cho phep khong
#tham so truyen vao:
#table: mang du lieu
#i : dong thu i
#MAXPT: số thuộc tính được thiếu của dữ liệu khong duoc vuot qua MAXPT
def KTSoCotThieuTrenDong(table , i , MaxPT):
    dem_thieu = 0 #dem gia tri thuoc tinh thieu cua moi cot
    j = 0 
    while j < len(table): #duyet tung gia tri trong dong
        if str(table[j][1][i]) == 'nan':#kiem tra gia tri tren dong co rong khong
            dem_thieu += 1
        j += 1
    return dem_thieu > MaxPT
   
#ham xoa dong du lieu bi thieu vuot qua bao nhieu phan tram do cho truoc
def XoaDong(table, phantram):
    i = 0#bien dem
    while i < len(table[0][1]):#duyet tung dong
        if KTSoCotThieuTrenDong(table, i, phantram*len(table)) ==  True:#neu so dong vuot qua nguong cho phep
            j = 0
            while j < len(table): #duyet cac cot cua mot dong
                table[j][1].remove(table[j][1][i])#thuc hien xoa
                j += 1
        else:#vi lenh xoa se day phan tu phia sau len, nen chi khi khong xoa moi tang chi so len 
            i += 1
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
        table = XoaDong(table,float(sys.argv[2]))
        create_file(table, sys.argv[3])
    
