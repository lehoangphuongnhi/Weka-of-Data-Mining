from function_support import create_list
import sys

#Hàm in ra các cột bị thiếu dữ liệu
def list_missing(data):
    print('Cac cot bi thieu du lieu: ')
    #Duyệt tất cả các cột
    for i in range(len(data)):
        #Nếu bất cứ tập giá trị trên các dòng của cột nào không có giá trị (hay 'nan') thì sẽ in ra tên cột đó
        if 'nan' in str(data[i][1]):
            print(data[i][0])
            continue

if __name__ == '__main__':

    """
        Chạy trên cmd. Cú pháp: `python bai1.py filename`
    """
    print('Number of arguments:', len(sys.argv), 'arguments. Argument List:', str(sys.argv))

    #Kiểm tra xem đủ tham số đầu vào chưa
    if len(sys.argv) < 2:
        print("To run: `python bai1.py filename`")
        print("WARMING: Must be provided enough argument!\n")

    #filename: tệp dữ liệu csv để ta thực hiện trên nó
    filename = str(sys.argv[1])
    #data: list lưu lại data trong filename
    data = create_list(filename)
    #In ra tên các cột bị thiếu dữ liệu
    list_missing(data)