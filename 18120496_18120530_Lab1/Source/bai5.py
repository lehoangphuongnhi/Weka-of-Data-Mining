from function_support import create_list, create_file
import sys

#Hàm xóa các cột bị thiếu dữ liệu với tỉ lệ thiếu cho trước
#fileout: file lưu dữ liệu sau khi xóa các cột, percent: tỉ lệ thiếu
def delete_row(data, fileout, percent):
    #temp: lưu lại các cột cần xóa
    temp = []
    #Duyệt tất cả các cột
    for i in range(len(data)):
        #Nếu bất cứ tập giá trị trên các dòng của cột nào không có giá trị (hay 'nan') thì sẽ tiến hành kiểm tra xem nó có bị thiếu 
        #vượt ngưỡng cho phép hay không
        if 'nan' in str(data[i][1]):
            #dem: số lượng giá trị bị thiếu của các cột
            dem = 0
            #Duyệt tất cả các phần tử của tập giá trị trên các dòng của cột
            for j in range(len(data[i][1])):
                #Nếu phần tử nào bị thiếu dữ liệu thì tăng biến dem lên
                if str(data[i][1][j]) == 'nan':
                    dem = dem + 1
            #Nếu dem lớn hơn ngưỡng cho phép thì lưu cột đó vào temp
            if dem > int(len(data[i][1])*int(percent)/100):
                temp.append(data[i])
    #Duyệt tất cả phần tử của temp
    for i in range(len(temp)):
        #Loại bỏ các cột bị thiếu dữ liệu vượt ngưỡng cho phép
        data.remove(temp[i])
    #Ghi dữ liệu của data vào fileout
    create_file(data, fileout)
    pass

if __name__ == '__main__':

    """
        Chạy trên cmd. Cú pháp: `python bai5.py percent filename fileout`
    """

    print('Number of arguments:', len(sys.argv), 'arguments. Argument List:', str(sys.argv))

    #Kiểm tra xem đủ tham số đầu vào chưa
    if len(sys.argv) < 4:
        print("To run: `python bai5.py percent filename fileout`")
        print("WARMING: Must be provided enough argument!\n")

    #fileout: file lưu dữ liệu sau khi xóa các cột bị thiếu dữ liệu với tỉ lệ thiếu cho trước
    fileout = str(sys.argv[3])
    #filename: file dữ liệu đầu vào
    filename = str(sys.argv[2])
    #percent: tỉ lệ thiếu dữ liệu
    percent = str(sys.argv[1])
    #data: list lưu lại data trong filename
    data = create_list(filename)
    #Gọi hàm xóa các cột thiếu dữ liệu với tỉ lệ thiếu cho trước
    delete_row(data, fileout, percent)

