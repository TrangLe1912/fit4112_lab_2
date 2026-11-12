# FIT4112 – Phiếu thực hành Lab 2

**Chủ đề:** FP-Growth và so sánh Apriori – FP-Growth  
**Tiền đề:** Biết basket 0/1 và support, confidence, lift ở Lab 1.  
**Hình thức:** Cá nhân; làm việc với 2 notebook; không cần Papermill, Streamlit, lập trình thuật toán từ đầu.

## Kết quả học tập

1. Chạy FP-Growth và tạo luật kết hợp.
2. Dùng cùng một basket và tham số để so sánh với Apriori.
3. Kiểm tra tính tương đương về các tập mục, support và luật (không chỉ đếm số lượng).
4. Biết vì sao một phép đo thời gian trên dữ liệu nhỏ chưa đủ để kết luận thuật toán nào tối ưu.
5. Diễn giải luật và đề xuất áp dụng.

## Phần A – Làm theo hướng dẫn (40 điểm)

1. Chạy `notebooks/01_fpgrowth.ipynb`; kiểm tra kích thước basket và tệp xuất `data/processed/fpgrowth_rules.csv`.
2. Tìm **5 luật** và ghi tiền đề, kết quả, support, confidence, lift.
3. Trả lời: FP-Growth và Apriori cùng tìm gì? Khác nhau về phương pháp tìm tập mục như thế nào?
4. Chạy `notebooks/02_compare_apriori_fpgrowth.ipynb`; ghi kết quả kiểm tra tương đương.

## Phần B – Thử nghiệm và so sánh (40 điểm)

1. Với dữ liệu demo, chạy cả hai thuật toán tại `min_support = 0.10` và `0.20`, giữ nguyên `MAX_LEN = 3`, `MIN_CONFIDENCE = 0.30`.
2. Ghi **số tập mục phổ biến và số luật** cho hai thuật toán ở mỗi ngưỡng.
3. Giải thích: tại sao kết quả khai phá cần trùng nhau khi dùng cùng dữ liệu/tham số?
4. Ghi thời gian đo của hai thuật toán và giải thích **vì sao chưa thể khẳng định FP-Growth luôn nhanh hơn Apriori**, nhất là với bộ demo nhỏ.

## Phần C – Phân tích và ứng dụng (20 điểm)

1. Giải thích 2 luật bằng tiếng Việt, chú ý support/confidence/lift.
2. Đề xuất 1 hoạt động bán kèm hoặc trưng bày sản phẩm có căn cứ.
3. Chỉ ra ít nhất 1 hạn chế (dữ liệu giả lập, tính tổng quát, không phải nhân quả...).

## Rubric (100 điểm)

| Tiêu chí | Điểm |
|---|---:|
| Notebook 01 chạy, thu được bảng FP-Growth và tệp luật | 15 |
| Ghi 5 luật đầy đủ chỉ số và giải thích được FP-Growth | 25 |
| Đối chiếu đúng kết quả Apriori và FP-Growth | 15 |
| Thí nghiệm hai ngưỡng support, so sánh số itemsets/luật | 15 |
| So sánh runtime, nêu giới hạn đo trên dữ liệu nhỏ | 10 |
| Diễn giải 2 luật, đề xuất ứng dụng và giới hạn | 20 |
| **Tổng** | **100** |

**Không yêu cầu FP-Growth phải chạy nhanh hơn, không yêu cầu web dashboard hay vẽ FP-tree.** Điểm tối đa dựa trên năng lực thực hiện và phân tích, không phụ thuộc phần nâng cao.

## Sản phẩm nộp

- Hai file `.ipynb` có output/nhận xét.
- `LAB02_REPORT.md` (hoặc PDF) tối đa khoảng 2 trang theo mẫu [REPORT_TEMPLATE.md](REPORT_TEMPLATE.md).
- Có thể nộp repo cá nhân chứa notebook và báo cáo. Không commit `.venv/`, dữ liệu thật lớn hoặc `data/processed/`.

## Nâng cao – tự chọn

Thử với basket từ Lab 1 trên dữ liệu Online Retail thật; chạy nhiều lần, dùng môi trường đo nhất quán; tìm hiểu FP-tree hoặc phân tích ngưỡng support thấp. Không bắt buộc để đạt điểm tối đa.
