from function_support import create_list, create_file
import bai3
import sys
import math

#Hàm chuẩn hóa thuộc tính numeric bằng phương pháp min-max
#data_attribute: Dữ liệu của thuộc tính numeric cần chuẩn hóa
def _min_max(data_attribute):
    #oldmin: giá trị min của thuộc tính cần chuẩn hóa
    oldmin = min(data_attribute)
    #oldmax: giá trị max của thuộc tính cần chuẩn hóa 
    oldmax = max(data_attribute)
    #newmax: giá trị max mới, ở đây cho bằng 1
    newmax = 1
    #newmin: giá trị min mới, ở đây cho bằng 0
    newmin = 0
    #Duyệt tất cả các giá trị của thuộc tính cần chuẩn hóa
    for i in range(len(data_attribute)):
        #Nếu nó không bị thiếu thì cập nhật lại
        if str(data_attribute[i]) != 'nan':
            #Cập nhật lại các giá trị
            data_attribute[i] = ((data_attribute[i] - oldmin)/(oldmax - oldmin))*(newmax-newmin) + newmin
    pass

#Hàm chuẩn hóa thuộc tính numeric bằng phương pháp z-score
#data_attribute: Dữ liệu của thuộc tính numeric cần chuẩn hóa
def z_score(data_atrribute):
    #mean: giá trị trung bình
    mean = 0
    #d: đếm số giá trị không bị thiếu
    d = 0
    #Duyệt tất cả các giá trị của thuộc tính cần chuẩn hóa
    for i in range(len(data_atrribute)):
        #Nếu nó là giá trị không bị thiếu thì tính tổng và tăng biến d lên
        if str(data_atrribute[i]) != 'nan':
            d = d + 1
            mean = mean + data_atrribute[i]
    #Giá trị mean sẽ bằng tổng chia cho số lượng
    mean = mean / d  
    #std: Độ lệch chuẩn của thuộc tính cần chuẩn hóa
    std = 0
    #dem: số lượng các thuộc tính không bị thiếu dữ liệu
    dem = 0
    #Duyệt tất cả các giá trị của thuộc tính cần chuẩn hóa
    for i in range(len(data_atrribute)):
        #Nếu nó là giá trị không bị thiếu thì tính std và tăng biến dem lên
        if ((str(data_atrribute[i]) != 'nan') and (data_atrribute[i] != mean)):
            std = std + (data_atrribute[i] - mean)**2
            dem = dem + 1
    #Giá trị std của thuộc tính cần chuẩn hóa
    std = math.sqrt(std/(dem-1))
    #Duyệt tất cả các giá trị của thuộc tính cần chuẩn hóa
    for i in range(len(data_atrribute)):
        #Nếu nó không bị thiếu thì cập nhật lại
        if str(data_atrribute[i]) != 'nan':
            data_atrribute[i] = (data_atrribute[i]-mean)/std
    pass

#Hàm chuẩn hóa thuộc tính numeric bằng phương pháp method (min-max or z-score)
#data_attribute: dữ liệu của thuộc tính numeric cần chuẩn hóa
#method: phương pháp dùng để chuẩn hóa (min-max or z-score)
#fileout: file lưu dữ liệu sau khi chuẩn hóa
def nomalization(data, data_atrribute, method, fileout):
    #Kiểm tra xem có phải là thuộc tính numeric không
    for i in range(len(data_atrribute)):
        if (type(data_atrribute[i]) == str) and (str(data_atrribute[i]) != 'nan'):
            print("Day khong phai la thuoc tinh numeric")
            return
    #Nếu method = min-max thì chuẩn hóa theo phương pháp min-max
    if method == 'min-max':
        _min_max(data_atrribute)
    #Nếu method = z-score thì chuẩn hóa theo phương pháp z-score
    elif method == 'z-score':
        z_score(data_atrribute)
    #Ghi dữ liệu của data vào fileout
    create_file(data, fileout)
    pass   

if __name__ == '__main__':

    """
        Chạy trên cmd. Cú pháp: `python bai7.py filename atrribute method fileout`
    """
    print('Number of arguments:', len(sys.argv), 'arguments. Argument List:', str(sys.argv))

    #Kiểm tra xem đủ tham số đầu vào chưa
    if len(sys.argv) < 5:
        print("To run: `python bai7.py filename atrribute method fileout`")
        print("WARMING: Must be provided enough argument!\n")

    #fileout: file lưu dữ liệu sau khi chuẩn hóa
    fileout = str(sys.argv[4])
    #method: phương pháp chuẩn hóa (min-max or z-score)
    method = str(sys.argv[3])
    #attribute: thuộc tính cần chuẩn hóa
    attribute = str(sys.argv[2])
    #filename: file dữ liệu đầu vào
    filename = str(sys.argv[1])
    #data: list lưu lại data trong filename
    data = create_list(filename)
    #Duyệt tất cả các cột của data
    for i in range(len(data)):
        #Nếu cột nào là cột thuộc tính cần phải chuẩn hóa thì tiến hành chuẩn hóa
        if data[i][0] == attribute:
            nomalization(data, data[i][1], method, fileout)
            break
    


