# Lab 03: Thảo luận

## 1. Merge base là gì?

- Merge base là commit tổ tiên chung gần nhất của hai nhánh, tức điểm mà hai nhánh bắt đầu tách ra.
- Git dùng merge base làm mốc để so sánh (3-way merge): so sánh từng nhánh với merge base để biết mỗi bên đã đổi gì.
- Nếu chỉ một bên đổi một dòng thì Git tự lấy bản đã đổi. Nếu cả hai bên cùng đổi một dòng khác nhau thì xảy ra xung đột (ví dụ dòng `print` trong `Cart.add_dvd` ở Phần C).
- Xem merge base bằng lệnh `git merge-base feature/show-added-title origin/master`.

## 2. Vì sao master/release/* phải dùng revert?

- `master` và `release/*` là lịch sử chung, nhiều người đã pull về. `git reset` viết lại lịch sử và buộc phải `push --force`, làm lịch sử của người khác bị lệch và có thể mất commit.
- `git revert` tạo thêm một commit đảo ngược, không viết lại lịch sử nên an toàn cho người khác và để lại dấu vết (ai hoàn tác, khi nào, vì sao).
- Các nhánh này có branch protection nên cũng không cho force push; revert đi qua nhánh + PR + review như mọi thay đổi khác.
- Với merge commit phải dùng `git revert -m 1 <sha>` để Git biết giữ nhánh chính (parent 1) làm mốc.
- `reset` chỉ dùng cho commit chưa push 
