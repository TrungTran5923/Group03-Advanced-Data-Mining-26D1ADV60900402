# Group03 - Advanced Data Mining - 26D1ADV60900402

**Môn học:** Khai phá dữ liệu nâng cao (UEH) – Nhóm 3
**Bộ dữ liệu:** Dunnhumby *The Complete Journey*

**Thành viên:** Nguyễn Duy Hiếu, Đỗ Thu Huyền, Nguyễn Thị Thanh Tâm, Nguyễn Thị Thu Thảo, Nguyễn Thị Hồng Trang, Trần Lê Minh Trung

Khai phá luật kết hợp và ứng dụng vào bài toán phân lớp khả năng phản hồi chiến dịch marketing tại chuỗi siêu thị.

## Cấu trúc

| Thư mục / file | Nội dung |
|---|---|
| `data/` | Đặt 7 file CSV của bộ dữ liệu vào đây (không đưa lên GitHub, xem `data/README.txt`) |
| `notebooks/01_eda.ipynb` | Bước 1 – Phân tích thăm dò dữ liệu |
| `notebooks/02_preprocessing.ipynb` | Bước 1 – Làm sạch, bảng giỏ hàng, Bộ dữ liệu 1, xếp hạng và lọc thuộc tính, chia train/test (`split.csv`) |
| `notebooks/03_data_warehouse.ipynb` | Bước 2 – Kho dữ liệu SQLite (fact constellation), kiểm tra chất lượng, 2 khối OLAP, các phép OLAP |
| `notebooks/04_association_rules.ipynb` | Bước 3 – Apriori và Multilevel AR, 3 luật tốt nhất, coverage, thuộc tính mới từ luật |
| `notebooks/05_classification.ipynb` | Bước 4 – Phân lớp 3 bộ dữ liệu × 3 mô hình, kiểm định chéo, thí nghiệm đối chứng chọn luật theo lift |
| `src/style.py` | Cấu hình biểu đồ dùng chung |
| `figures/` | Hình của notebook 01, 02, 04, 05 (H1–H16) và sơ đồ quy trình H00; `figures/dw/` là hình của notebook 03 |
| `outputs/` | Bảng kết quả; `outputs/dw/` là bảng kết quả của kho dữ liệu |

## Cách chạy
0. Tải bộ dữ liệu The Complete Journey (https://www.dunnhumby.com/source-files/ hoặc bản trên Kaggle) và chép 7 file CSV vào thư mục `data/`.
1. `pip install -r requirements.txt` (trên Colab chỉ cần `!pip install mlxtend`).
2. Chạy lần lượt `01` → `02` → `03` → `04` → `05` (Restart & Run All). Notebook 03 cần khoảng 1–2 phút và tạo file SQLite khoảng 340 MB (`outputs/dunnhumby_dw.sqlite`, hoặc `/content/` khi chạy trên Colab).
3. Trên Google Colab: tải cả thư mục dự án lên `My Drive` và đặt tên `DM_Nhom3_Final` (hoặc sửa đường dẫn trong ô đầu tiên của mỗi notebook). Ô đầu tiên sẽ mount Drive và chuyển vào thư mục `notebooks`.

Mọi bước ngẫu nhiên dùng `random_state = 42`. Luật chỉ được tìm và chọn trên dữ liệu không thuộc tập test.

## Số liệu kiểm tra nhanh
- Sau tiền xử lý: 2.543.426 dòng, 250.942 giỏ, doanh số 7.372.071 $ (notebook 02 và notebook 03 phải ra cùng số này).
- Apriori (commodity, 2%): 737 luật. Multilevel (10% / 2% / 0,5%): 1.469 luật, loại 212 luật dư thừa còn 1.257.
- Coverage bộ 3 luật: Apriori 6,41%, Multilevel 33,49%.
- ROC-AUC trên tập test (LR / DT / RF): D1 0,800 / 0,769 / 0,780; D2 0,808 / 0,773 / 0,782; D3 0,805 / 0,763 / 0,776.
