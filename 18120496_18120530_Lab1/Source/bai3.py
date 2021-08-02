from function_support import create_list, create_file
import sys

#Hàm trả về giá trị mean của data
def mean(data):
    #dem: số phần tử không bị thiếu dữ liệu
    dem = 0
    #m: tổng giá trị các phần tử không bị thiếu dữ liệu
    m = 0
    #Duyệt tất cả các phần tử trong data
    for i in range(len(data)):
        #Nếu phần tử nào không bị thiếu dữ liệu thì cộng dồn chúng lại với nhau và tăng biến dem lên
        if str(data[i]) != 'nan':
                   dem = dem + 1
                   m = m + data[i]
    #Giá trị mean cần tìm
    mean = m/dem
    #Duyệt tất cả các phần tử trong data
    for i in range(len(data)):
        #Nếu phần tử nào bị thiếu dữ liệu thì cập nhật giá trị của chúng = mean
        if str(data[i]) == 'nan':
                   data[i] = mean
    return mean

#Hàm trả về giá trị median của data
def median(data):
    #dem: số phần tử không bị thiếu dữ liệu
    dem = 0
    #temp: Lưu các phần tử không bị thiếu dữ liệu
    temp = []
    #Duyệt tất cả các phần tử của data
    for i in range(len(data)):
        #Nếu phần tử nào không bị thiếu dữ liệu thì tăng biến dem lên và đưa nó vào temp
        if str(data[i]) != 'nan':
            dem = dem + 1
            temp.append(data[i])
    #median: giá trị median cần tìm
    median = 0
    #Sắp xếp lại temp để tính đúng giá trị median
    temp.sort()
    #Duyệt tất cả các phần tử của temp
    for i in range(dem):
        #Nếu số lượng phần tử là 1 số chẵn thì median sẽ bằng trung bình cộng của 2 phần tử chính giữa
        if (dem%2 == 0):
            median = (temp[int(dem/2 - 1)] + temp[int(dem/2)])/2
        #Nếu số lượng phần tử là 1 số lẻ thì median sẽ bằng giá trị của phần tử chính giữa
        else:
            median = temp[int(dem//2)]
    #Duyệt qua tất cả các phần tử của data
    for i in range(len(data)):
        #Nếu phần tử nào bị thiếu dữ liệu thì cập nhật lại giá trị = median
        if str(data[i]) == 'nan':
            data[i] = median
    return median

#Hàm trả về giá trị mode của data
def mode(data):
    #temp: lưu lại các giá trị riêng biệt của data. Ví dụ: data = [nhi, quynh, nhi] thì temp = [nhi, quynh]
    temp = []
    #max: số lượng của phần tử xuất hiện nhiều nhất trong data
    max = 0
    #mode: giá trị mode cần tìm
    mode = 0
    #dem: số lượng các phần tử của temp trong data
    dem = 0
    #Duyệt tất cả các phần tử của data
    for i in range(len(data)):
        #Nếu data chưa có trong temp thì tiếp tục, thao tác này để giảm thiếu việc đếm số lượng các phẩn tử giống nhau
        if data[i] not in temp:
            dem = 0
            #Nếu phần tử này không bị thiếu dữ liệu thì thêm nó vào temp
            if str(data[i]) != 'nan':
                temp.append(data[i])
                #Duyệt tất cả các phần tử của data
                for j in range(len(data)):
                    #Nếu có giá trị bằng nhau thì tăng biến dem lên
                    if data[j] == data[i]:
                        dem = dem + 1
            #Nếu số lượng phần tử nào lớn hơn max thì cập nhật max bằng số lượng phần tử đó và cập nhật mode bằng phần tử đó
            if dem > max:
                max = dem
                mode = data[i]
    #Duyệt tất cả các phần tử của data
    for i in range(len(data)):
        #Phần tử nào bị thiếu dữ liệu thì cập nhật giá trị bằng mode
        if str(data[i]) == 'nan':
            data[i] = mode
    return mode

#Hàm điền giá trị bị thiếu, method: phương pháp điền giá trị bị thiếu cho thuộc tính numeric (mean or median), fileout: file lưu lại 
#dữ liệu sau khi đã điền giá trị bị thiếu
def impute(method, data, fileout):
    #Duyệt tất cả các cột của data
    for i in range(len(data)):
        #Nếu bất cứ tập giá trị trên các dòng của cột nào không có giá trị (hay 'nan') thì sẽ tiến hành điền giá trị vào
        if 'nan' in str(data[i][1]):
            #Duyệt tất cả các phần tử của tập giá trị đó
            for j in range(len(data[0][1])):
                #Xét kiểu của 1 phần tử bất kỳ không bị thiếu dữ liệu
                if str(data[i][1][j]) != 'nan':
                    #Nếu kiểu của phần tử đó là int hoặc float thì sẽ là thuộc tính numeric và tiến hành điền giá trị bị thiếu bằng
                    #phương pháp mean hoặc median
                    if((type(data[i][1][j]) == int) or (type(data[i][1][j]) == float)):
                        if method == 'mean':
                            mean(data[i][1])
                        elif method == 'median':
                            median(data[i][1])
                    #Nếu kiểu của phần tử đó là string thì sẽ là thuộc tính categorical và tiến hành điền giá trị bị thiếu bằng
                    #phương pháp mode
                    elif type(data[i][1][j]) == str:
                        mode(data[i][1])
                    break
    #Ghi dữ liệu của data vào fileout
    create_file(data, fileout)
    pass

if __name__ == '__main__':

    """
        Chạy trên cmd. Cú pháp: `python bai3.py filename method fileout`
    """
    print('Number of arguments:', len(sys.argv), 'arguments. Argument List:', str(sys.argv))

    #Kiểm tra xem đủ tham số đầu vào chưa
    if len(sys.argv) < 4:
        print("To run: `python bai3.py filename method fileout`")
        print("WARMING: Must be provided enough argument!\n")

    #fileout: file lưu dữ liệu sau khi điền các giá trị bị thiếu
    fileout = str(sys.argv[3])
    #method: phương pháp điền giá trị bị thiếu cho thuộc tính numeric (mean or median)
    method = str(sys.argv[2])
    #filename: dữ liệu đầu vào
    filename = str(sys.argv[1])
    #data: list lưu lại data trong filename
    data = create_list(filename)
    #Gọi hàm điền giá trị bị thiếu
    impute(method, data, fileout)

    