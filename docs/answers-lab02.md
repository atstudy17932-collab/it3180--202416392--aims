# Lab 02: Thảo luận

## 1. Vì sao phải đồng bộ master trước khi tạo PR?

- Phát hiện xung đột sớm trên nhánh của mình, không để dồn đến lúc merge.
- Chạy thử code đã tích hợp: sau khi `git merge origin/master`, `python main.py` cho thấy `print_cart` (Dev 1) hoạt động cùng `search_by_title` (Dev 2).
- Diff của PR chỉ chứa thay đổi của nhánh, reviewer dễ đọc.
- Giữ cho `master` luôn chạy được.

## 2. Khi nào không được rebase?

- Khi nhánh đã push và người khác đang dùng: rebase đổi SHA, phải force push, lịch sử của họ bị lệch.
- Với nhánh dùng chung như `master`, `release/*`.
- Khi cần giữ SHA và dấu vết gộp nhánh để sau này `git revert -m 1` cả tính năng.
- Quy tắc: chỉ rebase nhánh cá nhân chưa chia sẻ (ví dụ `topic/pr-template`, dùng `--force-with-lease`).

## 3. `feature/*` khác `topic/*` ra sao?

- `feature/*`: tính năng của sản phẩm (`cart-print`, `search-by-title`), review kỹ, merge bằng merge commit hoặc squash.
- `topic/*`: thay đổi phụ trợ, không phải tính năng (`pr-template`, `use-case-diagram`), nhẹ hơn, thường rebase để lịch sử thẳng.
