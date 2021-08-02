from function_support import create_list
import sys 

def DemSoDongThieu(table):
    dem_thieu = 0#bien dem nhung dong thieu
    i = 0#bien dem 
    while i < len(table[0][1]):#duyet tung dong
        j = 0
        while j < len(table): #duyet tung gia tri trong dong
            if str(table[j][1][i]) == 'nan':#kiem tra gia tri tren dong co rong khong
                dem_thieu += 1 #tang bien dem
                break
            j += 1
        i += 1
    print("So dong bi thieu :" , dem_thieu , end =  "\n")#in so bi thieu

if __name__ == '__main__':

    print('Number of arguments:', len(sys.argv), 'arguments. Argument List:', str(sys.argv))

    if len(sys.argv) < 2:
        print("To run: `python filename.csv`")
        print("WARMING: Must be provided enough argument!\n")
    else:
        filename = str(sys.argv[1])#lay ten file csv can doc
        table = []
        table = create_list(filename)#tao bang du lieu
        DemSoDongThieu(table)#thuc hien ham
