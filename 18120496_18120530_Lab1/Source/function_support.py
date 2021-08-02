import pandas as pd 

#Hàm tạo list lưu lại data trong file csv. Lưu theo cấu trúc [['Cột 1',[Các giá trị trên các dòng của cột 1]],.....['Cột n',[Các giá trị của cột n]]]
#Truy xuất tên các cột bằng cách: list[i][0] với i là thứ tự cột cần lấy
#Truy xuất tập giá trị trên các dòng của các cột bằng cách: list[i][1] với i là thứ tự cột cần lấy
#Truy xuất giá trị trên từng dòng của cột bằng cách: list[i][1][j] với i là thứ tự cột cần lấy, j là thứ tự dòng cần lấy
def create_list(filename):
    #Sử dụng pandas để đọc file csv vào data
    data = pd.read_csv(filename)
    #l là list gồm các tên cột
    l = (list)(data)
    #li là list lưu lại data theo cấu trúc đã nêu ở trên
    li = [0]*len(l)
    for i in range(len(l)):
        li[i] = (list)([l[i],list(data[l[i]])])
    return li

#Hàm xuất dữ liệu trong data ra file csv (fileout)
def create_file(data, fileout):
    #Tạo 1 dataframe để hỗ trợ ghi file
    df = pd.DataFrame()
    i = 0
    while i < len(data):
        df[data[i][0]] = data[i][1]
        i += 1
    #Ghi dữ liệu vào fileout với index = False tức là bỏ đi cột đếm số thứ tự
    df.to_csv(fileout, index = False)
    pass