# Labeling-Enhancement
### Phương pháp cải tiến
So sánh các đoạn text trong file excel. Nếu 2 đoạn text đó giống nhau về mặt nội dung -> có cùng một label
### Cách hoạt động của code
1. Chạy 1 lượt qua list content được input
2. Biến eval_ratio dùng để xét xem tỉ lệ giống nhau trên bao nhiêu % thì đánh dấu là content giống nhau
2. So sánh text similarity (sử dụng SequenceMatcher của difflib) giữa content đang xét với các content trong 1 dictionary (content được đánh dấu = index dưới dạng key). 
- Nếu giống nhau > eval_ratio % với 1 key thì thêm index vào value của key đó
- Nếu không thì thêm vào dict thành 1 key mới
4. Xuất thành 1 list rồi điền vào file excel (những content giống nhau sẽ được đánh cùng 1 số)
