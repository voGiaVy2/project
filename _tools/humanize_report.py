# -*- coding: utf-8 -*-
"""Sửa văn phong (bớt giọng AI) và các chỗ sai lệch nội dung trực tiếp trong
baocao_GayThongMinh.docx. Thay thế ở mức cụm từ, giữ nguyên định dạng run,
hình ảnh, bảng, mục lục. Bản gốc đã sao lưu: baocao_GayThongMinh_BACKUP_truoc_sua.docx
"""
import sys
from docx import Document

sys.stdout.reconfigure(encoding="utf-8")
PATH = r"d:\doan\baocao_GayThongMinh.docx"

R = [
    # ---------------- MỞ ĐẦU ----------------
    ("Bước sang thế kỷ 21, nhân loại đang chứng kiến một bước chuyển dịch nhân khẩu học lịch sử chưa từng có: tốc độ già hóa dân số diễn ra nhanh chóng trên quy mô toàn cầu.",
     "Dân số thế giới đang già đi nhanh chóng."),
    ("Xuất phát từ thực tiễn cấp bách đó, ", "Từ thực tế đó, "),
    ("được lựa chọn nghiên cứu và triển khai thực hiện nhằm biến cây gậy quen thuộc thành một trợ lý công nghệ tin cậy, chủ động bảo vệ người cao tuổi.",
     "được nhóm lựa chọn thực hiện, với mong muốn bổ sung cho cây gậy quen thuộc khả năng tự phát hiện té ngã và báo tin cho người thân."),
    ("Cung cấp giải pháp tối ưu hóa thuật toán xử lý gia tốc đa trục trên vi điều khiển chi phí thấp mà vẫn đảm bảo độ chính xác cao.",
     "Đề tài cũng cho thấy có thể chạy thuật toán phát hiện té ngã dựa trên gia tốc ngay trên một vi điều khiển giá rẻ với độ chính xác chấp nhận được."),
    ("đồng thời tạo nên sợi dây kết nối vô hình nhưng bền chặt, giúp con cháu dù ở xa vẫn luôn đồng hành và bảo vệ cha mẹ kịp thời trong mọi tình huống nguy cấp.",
     "đồng thời giúp con cháu ở xa biết được khi cha mẹ gặp sự cố để kịp thời hỗ trợ."),

    # ---------------- CHƯƠNG 1 ----------------
    ("Bước sang thế kỷ 21, già hóa dân số đã và đang trở thành một trong những biến đổi nhân khẩu học quan trọng và phức tạp nhất trên quy mô toàn cầu.",
     "Già hóa dân số hiện là một trong những thay đổi nhân khẩu học lớn nhất trên thế giới."),
    ("đang gia tăng với tốc độ nhanh chưa từng thấy trong lịch sử văn minh nhân loại", "đang tăng rất nhanh"),
    ("Đây là phương pháp bị người cao tuổi từ chối sử dụng nhiều nhất trong thực tế.",
     "Trên thực tế, đây là loại thiết bị mà người cao tuổi hay bỏ không dùng nhất."),
    ("Bảo vệ tuyệt đối quyền riêng tư cá nhân:", "Bảo đảm quyền riêng tư:"),
    ("ngăn chặn triệt để tình trạng", "tránh tình trạng"),
    ("Bảo vệ quyền riêng tư tuyệt đối", "Bảo vệ tốt quyền riêng tư"),
    ("Thân thiện và tự nhiên tuyệt đối:", "Thân thiện, tự nhiên:"),
    ("do đó giải quyết triệt để vấn đề", "do đó khắc phục được vấn đề"),
    ("Bảo vệ quyền riêng tư 100%:", "Bảo đảm quyền riêng tư:"),
    ("giúp giá thành sản phẩm cực kỳ cạnh tranh và dễ tiếp cận số đông", "giúp giảm đáng kể giá thành sản phẩm"),
    ("dạng chuẩn mực:", "dạng khá rõ:"),
    ("điểm yếu chí mạng của nó", "điểm yếu lớn nhất của nó"),
    ("vẫn là một thách thức kỹ thuật chưa thể khắc phục triệt để bằng camera đơn lẻ", "vẫn chưa khắc phục được hoàn toàn nếu chỉ dùng một camera"),
    ("Trên cơ sở phân tích thấu đáo các ưu điểm và hạn chế của các công trình đi trước, ", "Từ những ưu, nhược điểm của các công trình nêu trên, "),
    ("đã lựa chọn một hướng tiếp cận kỹ thuật đột phá, tối ưu hóa cả về mặt phần cứng lẫn phần mềm:", "chọn hướng tiếp cận như sau:"),
    ("với lõi kép 240 MHz mạnh mẽ", "với lõi kép 240 MHz"),
    ("trang bị còi hú công suất lớn 2000 Hz", "trang bị còi báo 2000 Hz"),
    ("chia sẻ tài nguyên thông minh", "chia sẻ tài nguyên"),
    ("cơ chế đếm ngược 15 giây thông minh:", "cơ chế đếm ngược 15 giây:"),

    # ---------------- CHƯƠNG 2 ----------------
    ("Trái tim của ESP32-S3 là bộ vi xử lý", "ESP32-S3 dùng bộ vi xử lý"),
    ("với thông lượng cực cao", "với tốc độ cao"),
    ("Điều này tạo điều kiện lý tưởng để triển khai", "Nhờ vậy có thể chạy"),
    ("được nâng cấp toàn diện trong Bluetooth 5.0", "được cải tiến trong Bluetooth 5.0"),
    ("đóng vai trò cực kỳ quan trọng, cho phép", "cho phép"),
    ("cảm biến tích hợp nguyên khối công nghệ vi cơ điện tử (MEMS) hàng đầu của hãng InvenSense",
     "cảm biến vi cơ điện tử (MEMS) của hãng InvenSense"),
    ("Để khắc phục triệt để lỗi này, nhóm nghiên cứu đã thiết kế một giải pháp thuật toán đo lường chuyên sâu:",
     "Để tránh lỗi này, nhóm viết lại hàm đo khoảng cách theo ba bước:"),
    ("để đảm bảo xung kích tuyệt đối sạch sẽ, không bị chia sẻ thời gian", "để xung kích không bị ngắt quãng bởi"),
    ("Cơ chế dự phòng thông minh (Fallback mechanism):", "Cơ chế dự phòng (fallback):"),
    ("ngăn chặn triệt để nguy cơ vi điều khiển bị treo vô hạn", "tránh việc vi điều khiển bị treo"),
    ("bảo vệ an toàn tuyệt đối cho MOSFET và vi điều khiển", "bảo vệ MOSFET và vi điều khiển"),
    ("Mạch sạc tích hợp TP4056 hỗ trợ cổng cắm Type-C hiện đại,",
     "Mạch sạc (TP4056 trong thiết kế, module MH-CD42 trong nguyên mẫu thực nghiệm) dùng cổng Type-C,"),
    ("mạch tăng áp DC-DC Boost converter hiệu suất cao", "mạch tăng áp DC-DC (Boost)"),
    ("thời điểm phát sóng chính xác tuyệt đối từ đồng hồ nguyên tử", "thời điểm phát sóng lấy từ đồng hồ nguyên tử"),
    ("Để khắc phục triệt để rào cản này, đề tài đã áp dụng giải pháp", "Vì vậy, nhóm chọn cách dùng"),
    ("Công nghệ này kết hợp thông minh dữ liệu từ 3 nguồn:", "Dịch vụ này kết hợp dữ liệu từ 3 nguồn:"),
    ("liên kết Google Maps chuẩn mực dạng:", "liên kết Google Maps dạng:"),
    ("Một tính năng cực kỳ quan trọng được nhóm nghiên cứu khai thác là", "Nhóm cũng sử dụng"),
    ("Trái tim hiệu năng của Flutter, bao gồm", "Phần lõi của Flutter, gồm"),
    ("thực thi mã bytecode cực nhanh", "thực thi mã Dart"),
    ("Để giải quyết triệt để vấn đề sống còn này, nhóm nghiên cứu đã triển khai", "Để xử lý vấn đề này, nhóm dùng"),
    ("không bao giờ tự ý dừng tiến trình", "hạn chế việc tự dừng tiến trình"),

    # ---------------- CHƯƠNG 3 ----------------
    ("Tính thân thiện và dễ sử dụng tối đa:", "Dễ sử dụng:"),
    ("Cơ chế chống báo nhầm thông minh:", "Có cơ chế chống báo nhầm:"),
    ("Các chỉ tiêu kỹ thuật khắt khe được đặt ra cho toàn bộ hệ thống:", "Nhóm đặt ra các chỉ tiêu kỹ thuật sau cho hệ thống:"),
    ("trạm kết nối cổng (IoT Gateway) trung gian nhưng cực kỳ mạnh mẽ:", "trạm trung gian (IoT Gateway):"),
    ("Chạy Dịch vụ ngầm (Foreground Service) vĩnh viễn", "Chạy Dịch vụ ngầm (Foreground Service) liên tục"),
    ("đảm bảo đánh thức người giám hộ ngay cả khi họ đang ngủ say", "để người giám hộ nghe thấy kể cả khi đang ngủ"),
    ("Tổn hao công suất dẫn trên MOSFET là cực kỳ nhỏ:", "Tổn hao công suất dẫn trên MOSFET rất nhỏ:"),
    ("Các điểm nhấn nổi bật trong thiết kế cơ khí của gậy:", "Các điểm chính trong thiết kế cơ khí của gậy:"),
    ("hỗ trợ tối đa việc đi lại", "hỗ trợ việc đi lại"),
    ("phối hợp nhịp nhàng giữa", "lần lượt xử lý"),
    ("được tổ chức một cách khoa học và module hóa cao theo cấu trúc thư mục chuẩn:", "được chia thành các thư mục như sau:"),
    ("nền xám đen #121212 tinh tế", "nền xám đen #121212"),
    ("với nền đỏ rực rỡ", "với nền đỏ"),
    ("OpenStreetMap mượt mà", "OpenStreetMap"),
    ("với mức ưu tiên tuyệt đối", "với mức ưu tiên cao nhất"),

    # ---------------- CHƯƠNG 4 ----------------
    ("Giai đoạn thực nghiệm và đánh giá chất lượng đóng vai trò then chốt trong việc xác định", "Phần thực nghiệm nhằm kiểm tra"),
    ("Đo đạc chi tiết độ trễ", "Đo độ trễ"),
    ("Đánh giá tính khả thi và độ bền bỉ của cơ chế", "Đánh giá cơ chế"),
    ("ước lượng chính xác thời gian sử dụng", "ước lượng thời gian sử dụng"),
    ("được kiểm thử nghiêm ngặt thông qua", "được kiểm thử qua"),
    ("ta rút ra các nhận xét chuyên sâu về hiệu năng thuật toán:", "nhóm có một số nhận xét sau:"),
    ("nhưng bộ lọc thông thấp số (Digital Low-Pass Filter) trên MPU6050 cùng điều kiện kiểm tra pha rơi tự do (Free Fall phase < 0.6g) trước va đập đã triệt tiêu hoàn toàn các báo động giả này.",
     "nhưng phần lớn các xung này vẫn thấp hơn ngưỡng 25 m/s² nên không gây báo động. 8 lần báo nhầm còn lại xảy ra khi va chạm đủ mạnh để vượt ngưỡng; do firmware hiện chỉ dùng một ngưỡng gia tốc nên vẫn còn báo nhầm, đây là điểm cần cải thiện ở phiên bản sau."),
    ("là chỉ tiêu sống còn của", "là chỉ tiêu quan trọng của"),
    ("chỉ mất vỏn vẹn 1.31 giây", "khoảng 1.31 giây"),
    ("Đây là con số ấn tượng, đảm bảo thông tin tai nạn được truyền đi gần như tức thì.",
     "Như vậy phần lớn thời gian là khoảng chờ 15 giây có chủ đích, còn độ trễ kỹ thuật chỉ hơn 1 giây."),
    ("Một trong những tính năng vượt trội nhất của hệ thống là", "Một tính năng quan trọng của hệ thống là"),
    ("và hú còi đếm ngược 15 giây chính xác 100%.", "và bắt đầu đếm ngược 15 giây."),
    ("so sánh toàn diện các tính năng", "so sánh các tính năng"),
    ("đã chứng minh được sự hoàn thiện xuất sắc.", "đã hoạt động ổn định ở mức nguyên mẫu."),
    ("đã được kiểm chứng hoạt động chính xác 100% trên thiết bị thực tế.", "đều đã được thử trên mạch thật và chạy đúng chức năng."),
    ("sản phẩm mở ra cơ hội tiếp cận công nghệ bảo vệ sức khỏe to lớn cho hàng triệu gia đình có người cao tuổi tại Việt Nam.",
     "sản phẩm phù hợp với điều kiện kinh tế của nhiều gia đình có người cao tuổi."),

    # ---------------- KẾT LUẬN ----------------
    ("Sau thời gian nghiên cứu, thiết kế, chế tạo và thử nghiệm nghiêm ngặt,", "Sau thời gian nghiên cứu, thiết kế, chế tạo và thử nghiệm,"),
    ("đã hoàn thành toàn diện tất cả các mục tiêu kỹ thuật và yêu cầu thực tiễn đề ra.", "về cơ bản đã đạt được các mục tiêu đặt ra ban đầu."),
    ("Thiết kế thành công nguyên mẫu gậy thông minh với kết cấu cơ khí công thái học in 3D chắc chắn, trọng lượng nhẹ (~420g), cân đối trọng tâm, tay cầm vừa vặn với thể trạng người cao tuổi Việt Nam.",
     "Thiết kế mô hình 3D cho thân gậy, tay cầm và khoang chứa mạch; lắp ráp nguyên mẫu phần cứng để phục vụ thử nghiệm."),
    ("motor rung cảnh báo xúc giác điều khiển qua MOSFET công suất AOD4184.", "motor rung cảnh báo điều khiển qua mạch MOSFET."),
    ("Xây dựng khối quản lý nguồn điện an toàn sử dụng cell pin Lithium-ion 18650 dung lượng 2500 mAh, mạch sạc thông minh TP4056 tích hợp cổng Type-C và mạch tăng áp DC-DC Boost 5V hiệu suất 92%, cho phép gậy hoạt động liên tục trên 26 giờ sau mỗi lần sạc đầy.",
     "Xây dựng khối nguồn gồm một cell pin Li-ion 18650 2000 mAh và module sạc – tăng áp MH-CD42 (sạc qua cổng Type-C, xuất 5 V). Theo kết quả đo ở mục 4.6, gậy dùng được khoảng 21 giờ sau mỗi lần sạc đầy."),
    ("Nghiên cứu và tối ưu hóa thành công thuật toán phát hiện té ngã dựa trên vector độ lớn gia tốc tổng SVM (Signal Vector Magnitude) kết hợp với bộ lọc số thông thấp IIR và điều kiện kiểm tra góc nghiêng không gian sau va chạm.",
     "Xây dựng thuật toán phát hiện té ngã dựa trên độ lớn vector gia tốc tổng hợp SVM với ngưỡng 25 m/s², chạy trực tiếp trên ESP32-S3."),
    ("triệt tiêu hiệu quả các xung động giả khi đi bộ hoặc gõ gậy xuống sàn.", "phần lớn các lần đi bộ, gõ gậy xuống sàn không gây báo nhầm."),
    ("tiết kiệm điện năng vượt trội và", "tiêu thụ điện thấp và"),
    ("Xây dựng hoàn chỉnh ứng dụng di động", "Xây dựng ứng dụng di động"),
    ("với giao diện Dark Theme trực quan, hiện đại,", "với giao diện sáng/tối,"),
    ("Làm chủ kỹ thuật Dịch vụ nền", "Triển khai được Dịch vụ nền"),
    (", đem lại độ tin cậy an toàn tuyệt đối 100%.", ", giúp cảnh báo vẫn được gửi đi khi mất Internet."),
    ("Mặc dù hệ thống đã hoạt động rất ổn định và đáp ứng tốt các yêu cầu kiểm thử,", "Mặc dù hệ thống đã chạy được các chức năng chính,"),
    ("các định hướng nâng cấp chuyên sâu cho hệ thống", "một số hướng nâng cấp cho hệ thống"),
    ("trở thành một thiết bị độc lập 100%,", "hoạt động độc lập,"),

    # ---------------- PHỤ LỤC ----------------
    ("nhằm cấp phép cho ứng dụng hoạt động vĩnh viễn dưới nền", "để ứng dụng có thể chạy nền lâu dài"),
    ("chạy ngầm 24/7 trên Android", "chạy ngầm liên tục trên Android"),
]


def iter_paragraphs(doc):
    for p in doc.paragraphs:
        yield p
    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    yield p


def replace_in_par(p, old, new):
    runs = p.runs
    if not runs:
        return 0
    n = 0
    search_from = 0
    while True:
        full = "".join(r.text for r in runs)
        start = full.find(old, search_from)
        if start < 0:
            return n
        end = start + len(old)
        pos, first = 0, True
        for r in runs:
            t = r.text
            rs, re_ = pos, pos + len(t)
            pos = re_
            if re_ <= start or rs >= end:
                continue
            a, b = max(start, rs) - rs, min(end, re_) - rs
            if first:
                r.text = t[:a] + new + t[b:]
                first = False
            else:
                r.text = t[:a] + t[b:]
        n += 1
        search_from = start + len(new)


def main():
    doc = Document(PATH)
    counts = {old: 0 for old, _ in R}
    paras = list(iter_paragraphs(doc))
    for old, new in R:
        for p in paras:
            if old[:12] in p.text or old in p.text:
                counts[old] += replace_in_par(p, old, new)
    doc.save(PATH)
    ok = sum(1 for v in counts.values() if v)
    print(f"Da sua {ok}/{len(R)} cum tu, tong {sum(counts.values())} vi tri.")
    for old, v in counts.items():
        if not v:
            print("KHONG TIM THAY:", old[:90])


if __name__ == "__main__":
    main()
