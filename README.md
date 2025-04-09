Giải thích thuật toán Bài 2: Palindrome_Number
**Version 1:
- Kiểm Tra Số Âm:
Kiểm tra xem số x có phải là số âm không. Nếu x nhỏ hơn 0, nó không thể là số đối xứng, vì dấu âm ở đầu số sẽ không có trong phiên bản đảo ngược của nó. Ví dụ: số -121 khi đảo ngược sẽ thành 121-, không giống với -121.
Nếu x là số âm, trả về false ngay lập tức.
- Kiểm Tra Số Kết Thúc Bằng 0:
Kiểm tra xem số có kết thúc bằng 0 hay không (trừ 0). Nếu số kết thúc bằng 0 thì số đó không thể là số đối xứng (trừ trường hợp số 0). Ví dụ: số 10 khi đảo ngược sẽ là 01, không phải là 10.
Nếu số kết thúc bằng 0 và không phải là 0, trả về false.
- Đảo Ngược Số:
Khởi tạo biến reversed_num bằng 0 và sử dụng vòng lặp while để đảo ngược các chữ số của x.
Trong mỗi lượt của vòng lặp:
Lấy chữ số cuối cùng của x (bằng x % 10) và thêm vào reversed_num sau khi đã nhân với 10 (để đẩy các chữ số đã có sang bên trái).
Cập nhật x bằng cách loại bỏ chữ số cuối cùng (bằng phép chia nguyên x //= 10).
Vòng lặp này tiếp tục cho đến khi x nhỏ hơn hoặc bằng reversed_num. Điều này giúp giảm số lượng chữ số cần đảo ngược.
- So Sánh Cuối Cùng:
Sau khi vòng lặp kết thúc, ta sẽ có reversed_num chứa nửa số đã được đảo ngược. Để xác nhận xem số ban đầu có phải là số đối xứng hay không, chúng ta sử dụng một so sánh như sau:
return x == reversed_num or x == reversed_num // 10  
x == reversed_num: Kiểm tra xem số ban đầu có bằng số đảo ngược hay không.
x == reversed_num // 10: Điều này cho phép chúng ta xử lý các số có số chữ số lẻ (ví dụ như 121), khi chúng ta có thể bỏ qua chữ số giữa.

**Version 2: 
- Kiểm tra xem số có phải là số âm hay không; nếu có, trả về False.
- Chuyển đổi số thành chuỗi và so sánh chuỗi gốc với chuỗi được đảo ngược. Nếu giống nhau, số là đối xứng.
