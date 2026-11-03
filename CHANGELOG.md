# Changelog

## [Unreleased]

## [1.1.0] - 2026-11-02
### Added
- Cart.sort_by_title(), Cart.sort_by_cost()
- search_by_category()

## [1.0.1] - 2026-11-03
### Fixed
- search_by_title bỏ qua khoảng trắng thừa quanh từ khóa (#22)

## [1.0.0] - 2026-11-05
### Added
- Cart.print_cart() và xử lý giỏ hàng trống
- search_by_title() trong aims/search.py
- Cart.apply_discount(percent)
- Thông báo tiếng Việt kèm tên đĩa khi thêm vào giỏ
- PR template, bộ test (tests/)

### Fixed
- Giỏ hàng nhận đĩa thứ 21 (#7)
- apply_discount trả sai tổng và không kiểm tra percent
