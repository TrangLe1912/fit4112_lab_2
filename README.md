# FIT4112 – Lab 2: FP-Growth và so sánh với Apriori

**Học phần:** Khai phá dữ liệu (Data Mining) · **Chủ đề:** Frequent Pattern Mining  
**Mức độ:** Cơ bản → vận dụng · **Thực hành:** 2 Jupyter notebooks, **không Papermill**.

> Phiên bản sinh viên, phát triển từ [shopping_cart_advanced_analysis](https://github.com/TrangLe1912/shopping_cart_advanced_analysis). Lab 2 tiếp nối [FIT4112 Lab 1](https://github.com/TrangLe1912/fit4112_lab_1): đã biết basket 0/1, support, confidence, lift và Apriori.

## 1. Học xong lab, sinh viên làm được gì?

1. Giải thích FP-Growth khai phá tập mục phổ biến khác Apriori ở cách xử lý tìm kiếm (không yêu cầu tự cài FP-tree).
2. Chạy `fpgrowth` và `association_rules` từ `mlxtend`; giải thích luật được chọn.
3. Chạy **cả Apriori và FP-Growth trên cùng basket, cùng ngưỡng**, xác nhận tập mục phổ biến, độ hỗ trợ và luật là tương đương.
4. So sánh thời gian chạy có nhận thức về độ nhiễu đo đạc; **không mặc định FP-Growth luôn nhanh hơn**.
5. Thử hai ngưỡng `min_support` và đề xuất một cách áp dụng kết quả trong bán lẻ.

## 2. Cấu trúc

```text
fit4112_lab_2/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── basket_demo.csv          # basket 0/1, 40 hóa đơn, 9 sản phẩm
│   └── input/
│       └── README.md            # tùy chọn đưa basket từ Lab 1 vào
├── notebooks/
│   ├── 01_fpgrowth.ipynb
│   └── 02_compare_apriori_fpgrowth.ipynb
├── docs/
│   ├── LAB02_STUDENT.md
│   └── REPORT_TEMPLATE.md
└── tests/
    └── smoke_test.py
```

**Khác repo nghiên cứu gốc:** bỏ `run_papermill.py`, dashboard Streamlit, báo cáo dài và đồ thị mạng tương tác; không yêu cầu sinh viên chạy lại EDA hoặc làm sạch dữ liệu từ đầu.

## 3. Chuẩn bị môi trường

Yêu cầu Python **3.11 hoặc 3.12**.

```bash
git clone https://github.com/TrangLe1912/fit4112_lab_2.git
cd fit4112_lab_2
python -m venv .venv
```

Kích hoạt môi trường:
- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

```bash
python -m pip install -r requirements.txt
jupyter lab
```

Trong JupyterLab hoặc VS Code (có Jupyter extension), mở hai notebook theo thứ tự:

| Thứ tự | Notebook | Kết quả |
|---|---|---|
| 1 | [01_fpgrowth.ipynb](notebooks/01_fpgrowth.ipynb) | Tập mục phổ biến, luật FP-Growth, `fpgrowth_rules.csv` |
| 2 | [02_compare_apriori_fpgrowth.ipynb](notebooks/02_compare_apriori_fpgrowth.ipynb) | Đối chiếu itemsets/luật, bảng thí nghiệm 2 ngưỡng, đo thời gian |

Có thể chọn **Run All**, nhưng nên chạy từng cell để trả lời câu hỏi quan sát. Notebook 02 tự đọc basket và **không phụ thuộc file xuất từ notebook 01** để tránh kết quả cũ.

## 4. Dữ liệu

- **Mặc định:** `data/basket_demo.csv` – ma trận giả lập (40 hóa đơn × 9 mặt hàng), chạy ngay cả khi chưa làm Lab 1. Bộ dữ liệu này được dựng từ `transactions_demo.csv` của Lab 1, có thêm bước lọc giao dịch không hợp lệ theo hướng dẫn Lab 1.
- **Tự chọn:** sao chép `data/processed/basket_bool.csv` từ repo Lab 1 vào `data/input/basket_lab1.csv` của repo này, rồi ở **cả hai notebook** đổi `BASKET_FILE = "data/input/basket_lab1.csv"`. Không cam kết hai bộ dữ liệu sẽ giống nhau nếu ở Lab 1 bạn đã đổi giới hạn dữ liệu/tham số.

**Lưu ý:** demo là dữ liệu giảng dạy, không phải bằng chứng về hành vi mua thực tế.

## 5. Việc phải nộp

Chi tiết ở [phiếu thực hành và rubric](docs/LAB02_STUDENT.md). Tóm tắt:

- Hai notebook đã chạy, gồm bảng kết quả và nhận xét.
- **5 luật FP-Growth** có support, confidence, lift.
- Bảng so sánh Apriori – FP-Growth cùng dữ liệu và ngưỡng.
- So sánh `MIN_SUPPORT = 0.10` và `0.20` (trên demo) và nêu nhận xét.
- Giải thích 2 luật, đề xuất 1 cách bán kèm/trưng bày, nêu một hạn chế.
- Báo cáo ngắn theo [mẫu](docs/REPORT_TEMPLATE.md).

**Nâng cao tự chọn:** kiểm tra trên basket lớn hơn từ dữ liệu Online Retail, khảo sát độ nhạy thời gian và bộ nhớ hoặc nghiên cứu cấu trúc FP-tree. Không cần cho điểm tối đa.

## 6. Kiểm tra nhanh (đặc biệt hữu ích cho giảng viên)

```bash
python tests/smoke_test.py
```

Script sẽ so sánh tập mục phổ biến và luật của hai thuật toán trên dữ liệu demo. Script **không thay thế** việc Run All hai notebook để kiểm tra phần trình bày và kết quả trực quan.

## 7. Sự cố thường gặp

- `ModuleNotFoundError: mlxtend`: cài lại requirements trong đúng Python/kernel.
- `FileNotFoundError`: mở notebook từ `notebooks/` hoặc repo gốc; hàm tìm root dựa vào `data/basket_demo.csv`.
- Giỏ hàng là `0/1`, không phải bảng dữ liệu giao dịch thô; có thể dùng `basket_bool.csv` từ Lab 1.
- Không xuất hiện luật: thử giảm `MIN_SUPPORT` / `MIN_CONFIDENCE`; không ghi số liệu giả.
- Thời gian Apriori nhỏ hơn FP-Growth trên demo: **không coi là lỗi**. Với bộ dữ liệu nhỏ, khác biệt do overhead và môi trường có thể lấn át khác biệt thuật toán.

**Nguồn phát triển:** [TrangLe1912/shopping_cart_advanced_analysis](https://github.com/TrangLe1912/shopping_cart_advanced_analysis).  
