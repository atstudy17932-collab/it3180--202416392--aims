Thảo luận : Vì sao dùng git mv? release/lab01 có phải baseline? Vì sao không commit thẳng master dù làm một mình?
1. Vì sao dùng git mv?
git mv di chuyển file và đưa thay đổi vào staging trong một lệnh. Khi chỉ đổi vị trí mà không sửa nội dung trong cùng commit, Git nhận diện là rename, nên lịch sử file được giữ nguyên (git log --follow vẫn truy ngược được) và diff trong PR hiển thị “renamed” thay vì xóa + thêm.
2. release/lab01 có phải baseline không?
Có. Đó là mốc ổn định được đặt tên, đánh dấu trạng thái hoàn thành Lab 01 của master (origin/master và origin/release/lab01 có cùng mã băm), dùng để đối chiếu hoặc quay lại về sau.
3. Vì sao không commit thẳng vào master dù làm một mình?
Để giữ master luôn ở trạng thái chạy được, mọi thay đổi được làm và kiểm thử trên nhánh riêng rồi mới merge. Qua Pull Request, thay đổi được mô tả và review rõ ràng, dễ truy vết và dễ hoàn tác (bỏ nhánh hoặc revert merge).

