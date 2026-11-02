# Lab 04: Thảo luận

## 1. Vì sao release/* không merge vào master?

- `master` là dòng phát triển liên tục; `release/lab04` là baseline đã đóng băng, chỉ nhận hotfix quan trọng.
- Mọi sửa đổi làm trên `master` trước, rồi mới đưa vào release nếu cần. Vì vậy `master` chứa mọi thứ release có (`git log master..release/lab04` rỗng), không cần merge ngược.
- Merge release vào master chỉ tạo merge commit thừa và rủi ro kéo thay đổi riêng của release vào dòng phát triển.
- Phiên bản được định danh bằng tag (v1.0.0), không phụ thuộc việc merge.

## 2. So sánh với GitFlow

- GitFlow có `develop` và `master`: `release/*` rẽ từ `develop`, xong thì merge vào cả `master` (gắn tag) và `develop`.
- Mô hình ở lab gọn hơn: chỉ có `master` làm dòng chính, `release/*` rẽ từ master rồi đóng băng, không merge ngược; tag xác định phiên bản.
- GitFlow hợp với phần mềm có nhiều phiên bản bảo trì song song; mô hình lab ít nhánh, ít merge, hợp nhóm nhỏ.

## 3. Vì sao lên 1.0.0 mà không phải 0.4.0?

- Theo Semantic Versioning, `0.y.z` là giai đoạn đầu, API chưa ổn định (v0.1.0 đến v0.3.0 là Lab 01 đến 03).
- `1.0.0` tuyên bố bản phát hành ổn định đầu tiên, cam kết tương thích: sửa lỗi tăng PATCH, thêm tính năng tăng MINOR, phá vỡ tương thích tăng MAJOR.
