Giải thích thuật toán bài 3: lonely_numbers

**Version 1: Thuật toán Đếm
1. Tạo Mảng Đếm count:
Mảng count có kích thước max_num + 2 để đảm bảo có thể lưu trữ số và các số liền kề của chúng (từ 0 đến 1,000,000). Chúng ta sử dụng max_num + 2 để tránh lỗi chỉ số khi kiểm tra num + 1.
Đếm Số Lần Xuất Hiện:
Duyệt qua từng số trong mảng nums và cộng dồn vào mảng count tại chỉ số tương ứng với số đó.
2. Kiểm Tra Điều Kiện:
Duyệt qua tất cả các chỉ số từ 0 đến max_num.
Nếu số tại chỉ số đó xuất hiện đúng 1 lần (count[num] == 1), kiểm tra hai điều kiện:
Số liền kề trước (num - 1) không tồn tại (count[num - 1] == 0).
Số liền kề sau (num + 1) không tồn tại (count[num + 1] == 0).
3. Lưu Số Cô Đơn:
Nếu cả hai điều kiện trên đều đúng, thêm số đó vào danh sách lonely_numbers.
4. Trả Về Danh Sách:
Trả về danh sách các số cô đơn.

**Version 2: Thuật toán Sử Dụng HashSet
1. Đếm số lần xuất hiện của từng số**
Ta sẽ sử dụng một dictionary để đếm số lần xuất hiện của mỗi số trong danh sách.
2. Tạo danh sách để chứa các số cô đơn**
Khởi tạo danh sách trống để lưu các số cô đơn và tạo một tập (set) để lưu các số duy nhất từ dictionary.
3. Kiểm tra từng số duy nhất trong dictionary**
Lặp qua từng số trong `num_set` và xác định số nào là số cô đơn.
4. Trả về danh sách các số cô đơn**
Kết thúc việc kiểm tra, chúng ta có danh sách các số cô đơn.