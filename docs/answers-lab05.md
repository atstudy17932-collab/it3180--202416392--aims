# Lab 05: Thảo luận

## 1. Ưu, nhược điểm của upstream first so với release first?

- Upstream first (sửa trên master trước, rồi cherry-pick xuống release): bản sửa chắc chắn có ở dòng phát triển chính nên không bị quay lại ở bản sau; nhược điểm là master đã đi xa, cherry-pick xuống bản cũ dễ xung đột và chậm.
- Release first (như học phần): nhanh, sát bản đã phát hành, ít xung đột; nhược điểm là dễ quên lan truyền về master và các release khác, khiến lỗi tái xuất ở bản sau.

## 2. Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F phát hiện?

- `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"` chỉ ra 1 kết quả thay vì 2.
- Vòng lặp kiểm tra hành vi in `0` cho v1.1.0 thay vì `1`.
- `git cherry -v origin/master origin/release/lab05` cho thấy commit còn thiếu.

