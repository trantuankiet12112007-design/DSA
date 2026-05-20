# PHẦN A - HIỂU THUẬT TOÁN

## Bài 1. Trình bày ý tưởng

Tìm kiếm tuyến tính là thuật toán duyệt lần lượt từng phần tử trong mảng từ đầu đến cuối.

Nếu tìm thấy phần tử bằng giá trị cần tìm `x` thì trả về vị trí của phần tử đó.

Nếu duyệt hết mảng mà không tìm thấy thì trả về `-1`.

**Input:** mảng `a` và giá trị cần tìm `x`.

**Output:** vị trí của `x` trong mảng, hoặc `-1` nếu không tìm thấy.

Thuật toán dừng khi:

- Tìm thấy `x`.
- Duyệt hết mảng nhưng không tìm thấy `x`.

---

## Bài 2. Mô phỏng từng bước

Cho mảng:

```python
A = [7, 3, 9, 12, 5, 8, 1]
x = 5
```

| i   | A[i] | So sánh     | Kết luận |
| --- | ---- | ----------- | -------- |
| 0   | 7    | 7 == 5 sai  | Tiếp tục |
| 1   | 3    | 3 == 5 sai  | Tiếp tục |
| 2   | 9    | 9 == 5 sai  | Tiếp tục |
| 3   | 12   | 12 == 5 sai | Tiếp tục |
| 4   | 5    | 5 == 5 đúng | Trả về 4 |

Kết quả: hàm trả về `4`.

---

## Bài 3. Đếm số phép so sánh

Với mảng:

```python
A = [7, 3, 9, 12, 5, 8, 1]
```

### a. Tìm `x = 7`

`7` nằm ở vị trí đầu tiên nên cần `1` phép so sánh.

### b. Tìm `x = 1`

`1` nằm ở vị trí cuối cùng nên cần `7` phép so sánh.

### c. Tìm `x = 100`

`100` không có trong mảng nên phải duyệt hết mảng, cần `7` phép so sánh.

**Nhận xét:** phần tử càng gần đầu mảng thì số phép so sánh càng ít. Nếu phần tử ở cuối mảng hoặc không tồn tại thì phải duyệt hết mảng.

---

## Bài 4. Phân tích độ phức tạp

Giả sử mảng có `n` phần tử.

- Trường hợp tốt nhất: cần `1` phép so sánh, độ phức tạp `O(1)`.
- Trường hợp xấu nhất: cần `n` phép so sánh, độ phức tạp `O(n)`.
- Trường hợp trung bình: cần khoảng `(n + 1) / 2` phép so sánh, độ phức tạp `O(n)`.

Kết luận: độ phức tạp thời gian của tìm kiếm tuyến tính là `O(n)`.

---

## Bài 5. Điều kiện áp dụng

Tìm kiếm tuyến tính không bắt buộc mảng phải được sắp xếp trước.

Lý do: thuật toán chỉ duyệt lần lượt từng phần tử và so sánh với giá trị cần tìm.

| Tiêu chí          | Tìm kiếm tuyến tính | Tìm kiếm nhị phân         |
| ----------------- | ------------------- | ------------------------- |
| Điều kiện áp dụng | Không cần sắp xếp   | Cần mảng đã sắp xếp       |
| Cách tìm          | Duyệt từng phần tử  | Chia đôi phạm vi tìm kiếm |
| Độ phức tạp       | O(n)                | O(log n)                  |

Kết luận: tìm kiếm tuyến tính dễ áp dụng hơn, nhưng tìm kiếm nhị phân nhanh hơn khi mảng đã được sắp xếp.
