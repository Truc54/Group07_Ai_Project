# TÀI LIỆU KHẢO SÁT TOÀN DIỆN VÀ CHI TIẾT NHẤT: 3 BÀI THUYẾT TRÌNH CUỐI CỦA CVPR 2025 TUTORIAL
## ĐỀ TÀI: FROM VIDEO GENERATION TO WORLD MODEL

Tài liệu này được biên soạn dưới dạng khảo sát học thuật đầy đủ, chi tiết từng slide, từng khái niệm và từng công trình nghiên cứu được đề cập trong **3 bài phát biểu cuối cùng (Last 3 Talks)** của buổi Tutorial tại hội nghị CVPR 2025 diễn ra vào ngày 11 tháng 6, 2025. 

Tài liệu này được thiết kế đặc biệt nhằm phục vụ mục đích lập trình hoạt ảnh toán học và thuật toán chuẩn chỉ bằng **Manim**, bảo đảm tính chính xác học thuật 100%, không rút gọn hay bỏ sót bất kỳ chi tiết chuyên môn nào.

---

# BÀI THUYẾT TRÌNH SỐ 1 (TALK 4 TRONG TUTORIAL)
## DIỄN GIẢ: PENGFEI WAN (TRƯỞNG NHÓM KLING, KUAISHOU TECHNOLOGY)
### Chủ đề: An Introduction to Kling and Our Research towards More Powerful Video Generation Models
*(Giới thiệu về Kling và nghiên cứu của chúng tôi hướng tới các mô hình tạo video mạnh mẽ hơn)*

#### 1. Bối cảnh và Tầm nhìn của Kling
Kling được phát triển bởi Trung tâm Tương tác và Tạo hình ảnh/Video thuộc Kuaishou Technology. Mục tiêu tối thượng của Kling không chỉ là tạo ra hình ảnh động đẹp mắt để giải trí, mà là xây dựng các **Mô hình thế giới nền tảng (Foundation World Models)** có khả năng mô phỏng động học thế giới thực ở cấp độ vật lý và hỗ trợ tương tác đa phương thức thực tế cho hơn 20 triệu người dùng toàn cầu.

#### 2. Kiến trúc Kỹ thuật Cốt lõi của Kling
Kiến trúc của Kling được xây dựng trên sự kết hợp độc quyền của hai công nghệ cốt lõi: **Diffusion Transformer (DiT)** và **3D Variational Autoencoder (3D VAE)**.

##### A. Công nghệ 3D Variational Autoencoder (3D VAE)
*   **Hạn chế của phương pháp cũ (2D VAE):**
    Hầu hết các mô hình tạo video thế hệ đầu (như Sora giai đoạn đầu hoặc các bản build chạy thử) sử dụng 2D VAE để nén và giải nén từng khung hình độc lập. Phép nén 2D bỏ qua mối quan hệ nhân quả và liên tục giữa các khung hình kề nhau, dẫn đến hiện tượng nhấp nháy ánh sáng (flickering), biến dạng cấu trúc khi vật thể chuyển động, hoặc mất tính nhất quán thời gian (temporal inconsistency).
*   **Giải pháp 3D VAE của Kling:**
    Kling tự thiết kế và huấn luyện một mạng **3D VAE** để nén đồng thời cả chiều không gian (Spatial) và chiều thời gian (Temporal) của video.
    *   *Định nghĩa toán học:* Video đầu vào $V \in \mathbb{R}^{T \times C \times H \times W}$ (với $T$: số khung hình, $C$: số kênh màu, $H$: chiều cao, $W$: chiều rộng) được đưa qua Encoder 3D VAE để ánh xạ vào không gian ẩn (latent space):
        $$z = \text{Encoder}_{3D}(V) \in \mathbb{R}^{\hat{T} \times \hat{C} \times \hat{H} \times \hat{W}}$$
        Trong đó, $\hat{T} < T$ là số lượng token thời gian ẩn (thể hiện tỷ lệ nén thời gian), và $\hat{H} < H$, $\hat{W} < W$ thể hiện tỷ lệ nén không gian ẩn.
    *   *Tác dụng:* Nén không-thời gian đồng thời giúp giảm thiểu đáng kể chi phí tính toán khi đưa vào lõi Transformer, đồng thời giữ lại tối đa các chi tiết chuyển động mịn màng và phân phối ánh sáng liên tục giữa các khung hình kề nhau.

##### B. Cơ chế Spatiotemporal Attention (Chú ý Không-Thời gian toàn phần)
*   Để mô hình hóa chính xác các chuyển động phức tạp, sự tương tác giữa các vật thể, Kling sử dụng một module **Full Spatiotemporal Attention** (chú ý không-thời gian toàn phần) cực kỳ hiệu quả về mặt tính toán.
*   Cơ chế này cho phép mỗi token ẩn ở tọa độ $(\hat{x}, \hat{y}, \hat{t})$ tính toán trọng số chú ý với **tất cả** các token khác trong toàn bộ không gian và thời gian của đoạn video ẩn. Nhờ đó, Kling có thể xử lý hoàn hảo các trường hợp:
    *   Vật thể chuyển động với tốc độ cực nhanh mà không bị nhòe hình hoặc biến mất đột ngột.
    *   Các pha chuyển cảnh (shot transitions) và thay đổi góc quay camera (camera movements) có biên độ lớn mà không bị rách hình.
    *   Giữ được cấu trúc của các vật thể chuyển động phức tạp (ví dụ: khớp tay của con người khi múa).

#### 3. Mô hình Kling-Omni (Kling O1) & Multimodal Visual Language (MVL)
*   **Tầm nhìn thống nhất (Unified Vision):**
    Trước đây, các bài toán tạo video (Text-to-Video), chỉnh sửa video (Video Editing) và nhận thức video (Video Understanding) được giải quyết bởi các mô hình hoặc nhánh kiến trúc hoàn toàn độc lập. Kling-Omni (Kling O1) phá vỡ rào cản này bằng cách xây dựng một kiến trúc **End-to-End thống nhất**.
*   **Cơ chế hoạt động của Multimodal Visual Language (MVL):**
    MVL xem xét tất cả các định dạng dữ liệu đầu vào (Văn bản - Text, Hình ảnh tĩnh - Image, Video cũ - Video) dưới dạng một ngôn ngữ thị giác đa phương thức chung.
    *   *Quy trình:* Các dữ liệu đầu vào khác loại được đưa qua các bộ mã hóa chuyên biệt (tokenizers) tương ứng để chuyển đổi về chung một định dạng là các chuỗi token ẩn đại diện. Sau đó, chuỗi token thống nhất này được đưa thẳng vào lõi **Diffusion Transformer Core** để xử lý đồng thời, sinh ra đầu ra là video chất lượng cao $1080p$ ở tốc độ $30$ khung hình/giây (fps), dài tối đa lên tới 2 phút.

#### 4. Bốn (04) Hướng Nghiên cứu Trọng tâm của Đội ngũ Kling
Pengfei Wan chỉ ra 4 mũi nhọn nghiên cứu mà đội ngũ của ông đang thực hiện để nâng cấp Kling thành một mô hình thế giới mạnh mẽ hơn:
1.  **Nâng cấp Kiến trúc Mô hình và Thuật toán AI tạo sinh (Advancing Model Architecture & Generative Algorithms):** Nghiên cứu tối ưu hóa cấu trúc DiT, đẩy nhanh tốc độ hội tụ của quá trình khuếch tán mà không làm suy giảm chất lượng hiển thị.
2.  **Tăng cường khả năng Tương tác và Điều khiển mạnh mẽ (Enhancing Interactive & Control Capacities):** Cải tiến việc áp dụng các điều kiện camera (camera control) chính xác (Pan, Zoom, Tilt) và khả năng nhận biết lực tác động vật lý của tác nhân lên môi trường.
3.  **Tích hợp cơ chế Đánh giá và Căn chỉnh chính xác (Incorporating Accurate Evaluation & Alignment Mechanisms):** Xây dựng các thang đo nội bộ để đo lường độ chân thực vật lý và mức độ liên kết nội dung với prompt của người dùng.
4.  **Cải thiện Nhận thức và Suy luận Đa phương thức (Improving Multimodal Perception & Reasoning):** Giúp mô hình không chỉ tạo ra video mà còn có khả năng giải thích cấu trúc chuyển động và các hiện tượng xảy ra trong video đó.

#### 5. Các dự án vệ tinh tiêu biểu của Kling
*   **LivePortrait:** Mô hình sinh chuyển động chân dung (portrait animation) cực kỳ hiệu quả, cho phép chuyển đổi một bức ảnh tĩnh của khuôn mặt thành một video động dựa trên chuyển động của một người dẫn đường (driving video), giữ nguyên được các biểu cảm vi mô (micro-expressions).
*   **Kling-Avatar:** Hệ thống tạo và điều khiển avatar số 3D có độ chân thực cao từ dữ liệu tối thiểu.

---

# BÀI THUYẾT TRÌNH SỐ 2 (TALK 5 TRONG TUTORIAL)
## DIỄN GIẢ: ANGJOO KANAZAWA (TRỢ LÝ GIÁO SƯ TẠI UC BERKELEY)
### Chủ đề: Streaming Perception: Towards Learning Structured Models of the World
*(Nhận thức dòng chảy: Hướng tới việc học các mô hình có cấu trúc của thế giới)*

#### 1. Sự phê phán đối với các mô hình tạo video hiện tại (The Critique of Current Video Models)
*   **Hiện tượng Uncanny Realism (Độ chân thực kỳ quái):**
    Các mô hình tạo video ngày nay đạt đến mức độ chân thực trực quan đáng kinh ngạc. Chúng tạo ra các làn sóng nước lấp lánh, phản chiếu ánh sáng và chuyển động bóng đổ hoàn hảo. Người xem có cảm giác như mô hình thực sự hiểu sâu sắc về thế giới thực.
*   **Bản chất thực tế (The Reality):**
    Angjoo Kanazawa chỉ ra rằng các mô hình này thực chất chỉ là những **bộ kết xuất pixel (renderers) siêu việt**. Chúng học cách phân phối các pixel màu trên bề mặt 2D một cách thông minh để đánh lừa thị giác con người, nhưng hoàn toàn **không có biểu diễn cấu trúc hình học 3D/4D bền vững bên trong**. Khi góc quay thay đổi hoặc vật thể bị che khuất, mô hình không có một "bộ nhớ vật lý" nào để giữ nguyên trạng thái cũ của vật thể, dẫn đến sự trôi dạt cấu trúc (structural drift) hoặc hiện tượng vật thể tự biến đổi hình dạng (morphing).
*   **Giải pháp - Nhận thức dòng chảy (Streaming Perception):**
    Để các mô hình thế giới có thể thực sự hỗ trợ robot đưa ra các hành động và lập kế hoạch lâu dài, chúng phải hoạt động như dòng nhận thức của con người: **xây dựng và cập nhật liên tục một mô hình cấu trúc 3D/4D nội bộ bền vững (persistent, structured internal representations) từ luồng dữ liệu hình ảnh liên tục (continuous streaming inputs)**. Sự quan sát này được bà đúc rút và định hình từ chính kinh nghiệm thực tế khi quan sát cách một đứa trẻ sơ sinh lớn lên, quan sát và tương tác liên tục với thế giới để xây dựng các mô hình cấu trúc vật thể trong đầu.

#### 2. Dự án CUT3R (Continuous Updating Transformer for 3D Reconstruction)
*   **Định nghĩa:**
    CUT3R là một khung cấu trúc thống nhất (unified framework) cho phép nhận thức hình học 3D liên tục từ một luồng khung hình video (image streams).
*   **Cơ chế hoạt động hồi quy (Stateful Recurrent Mechanism):**
    CUT3R không xử lý độc lập từng khung hình hay chạy tối ưu hóa toàn cục đắt đỏ. Nó duy trì một **Trạng thái Bộ nhớ 3D (Recurrent 3D Memory State)** dưới dạng một bản đồ điểm 3D mật độ cao (dense 3D pointmap) hoặc một thể tích đặc trưng ẩn (feature volume).
    *   *Quy trình cập nhật thời gian thực:*
        Tại mỗi bước thời gian $t$, khi camera nhận khung hình mới $I_t$, Transformer của CUT3R sẽ so sánh thông tin trực quan mới với Trạng thái Bộ nhớ 3D hiện có $S_{t-1}$. Nó chỉ tính toán và cập nhật phần thông tin mới hoặc thay đổi, bồi đắp vào trạng thái bộ nhớ để sinh ra Trạng thái Bộ nhớ 3D mới $S_t$:
        $$S_t = \text{Transformer\_Update}(S_{t-1}, I_t)$$
    *   *Xử lý Che khuất (Occlusion Handling) và Tự suy luận (Hallucination):*
        Khi camera quay đi nơi khác hoặc một vật thể đi ngang che khuất hậu cảnh, CUT3R sử dụng Transformer để tự động dự đoán và giữ nguyên hình học của phần bị che khuất trong bộ nhớ trạng thái. Khi camera quay trở lại, phần hình học đó được tái dựng nguyên vẹn mà không bị biến dạng.

#### 3. Dự án ST4rtrack (Simultaneous 4D Reconstruction and Tracking in the World)
*   **Hạn chế của phương pháp thị giác máy tính truyền thống (Traditional Disjoint Approach):**
    Từ trước đến nay, cộng đồng Computer Vision chia bài toán nhận thức cảnh động làm hai bước độc lập chạy nối tiếp:
    1.  *Bước 1 (Pixel Tracking - Theo dõi điểm ảnh):* Sử dụng các thuật toán Optical Flow (Dòng quang học) 2D để theo dõi vết của các pixel trên mặt phẳng ảnh 2D.
    2.  *Bước 2 (3D Reconstruction - Tái dựng 3D):* Sử dụng các thuật toán Structure from Motion (SfM) hoặc SLAM để từ các điểm 2D dựng thành mô hình 3D.
    *   *Lỗi tích lũy (Error Propagation):* Hai bước này hoạt động hoàn toàn độc lập và không chia sẻ thông tin. Nếu bước 1 (Optical Flow) chỉ cần sai lệch vài pixel do nhiễu hoặc ánh sáng thay đổi, bước 2 (SfM) sẽ nhận dữ liệu đầu vào sai và tính toán ra các tọa độ 3D hoàn toàn méo mó, thậm chí làm sụp đổ toàn bộ mô hình tái dựng.
*   **Giải pháp mang tính cách mạng của ST4rtrack:**
    ST4rtrack (được giới thiệu tại hội nghị danh giá ICCV 2025) là một mô hình truyền thẳng (feed-forward) giải quyết **đồng thời và nhất quán cả hai bài toán: Theo dõi quỹ đạo điểm (Tracking) và Tái dựng hình học (Reconstruction)** trong một hệ tọa độ thế giới thống nhất (World Coordinate Frame).
    *   *Biểu diễn toán học:*
        ST4rtrack dự đoán trực tiếp một **Bản đồ điểm 4D (Spatiotemporal Pointmap)**. Với mỗi điểm $i$ trên bề mặt của bất kỳ vật thể nào (cả tĩnh lẫn động), mô hình dự đoán tọa độ 3D của nó chuyển động liên tục theo thời gian $t$:
        $$P_i(t) = \begin{bmatrix} X_i(t) \\ Y_i(t) \\ Z_i(t) \end{bmatrix} \in \mathbb{R}^3 \quad \forall t \in T$$
    *   *Tác dụng:* Việc tích hợp chung một mô hình feed-forward duy nhất giúp thông tin hình học 3D bổ trợ ngược lại cho thuật toán bám vết điểm ảnh, triệt tiêu hoàn toàn sự tích lũy sai số và tạo ra quỹ đạo chuyển động mịn màng, nhất quán vật lý tuyệt đối trong không gian 4D.

---

# BÀI THUYẾT TRÌNH SỐ 3 (TALK 6 TRONG TUTORIAL)
## DIỄN GIẢ: SHERRY YANG (TRỢ LÝ GIÁO SƯ TẠI NYU COURANT / ĐỒNG TRƯỞNG NHÓM GOOGLE DEEPMIND)
### Chủ đề: Scaling World Models for Agents
*(Mở rộng quy mô các mô hình thế giới cho các tác nhân)*

#### 1. Sự khác biệt của Mô hình thế giới dựa trên sinh video ngày nay
*   **Lịch sử:** Ý tưởng về mô hình thế giới (World Model/Dynamics Model) thực tế đã tồn tại từ lâu trong ngành Reinforcement Learning (ví dụ: nghiên cứu kinh điển *World Models* của Ha & Schmidhuber 2018, hoặc loạt công trình *Dreamer* của Hafner từ 2020). Các mô hình cũ học động học trong không gian ẩn (latent dynamics) từ các môi trường nhỏ như game Atari hoặc mô phỏng vật lý đơn giản (MuJoCo).
*   **Bước ngoặt hiện tại:**
    Sự khác biệt của các mô hình thế giới sinh video hiện nay so với quá khứ nằm ở hai yếu tố mở rộng cốt lõi:
    1.  **Dữ liệu quy mô Internet (Internet-Scale Dataset):** Học từ lượng video khổng lồ và cực kỳ đa dạng của thế giới thực chứ không bó hẹp trong môi trường giả lập.
    2.  **Kiến trúc tạo video có khả năng mở rộng mạnh mẽ (Scalable Architectures):** Sử dụng các kiến trúc Diffusion Transformer (DiT) lớn, bộ hướng dẫn Classifier-Free Guidance, hệ thống siêu độ phân giải chồng chất (Cascade Models) và kỹ thuật sinh tự hồi quy theo khối ảnh (Block-wise Autoregressive Rollouts) giúp giả lập một mô hình thế giới duy nhất hoạt động xuyên suốt qua nhiều môi trường cực kỳ khác biệt.

#### 2. Dữ liệu quy mô lớn cho Mô hình thế giới: 21 Triệu cặp Video-Hành động
*   **Đề xuất nghiên cứu:** Công trình *Video as the New Language for Real-World Decision Making* (ICML 2024) của Sherry Yang và các đồng nghiệp chỉ ra rằng: Có thể biến video thành một "ngôn ngữ chung" cho mọi tác vụ ra quyết định của Robot bằng cách sử dụng các dữ liệu video được căn chỉnh theo thời gian với hành động (time-aligned video-action data).
*   **Bốn loại hành động điều khiển (Control Actions) được hợp nhất:**
    Mô hình thế giới được huấn luyện trên tập dữ liệu khổng lồ **21 triệu cặp video-hành động** bao gồm 4 nguồn dữ liệu đa dạng:
    1.  *Text-Video Pairs (Cặp Chữ - Video):* Các video con người làm việc đi kèm mô tả hành động (ví dụ: "Một người đang dùng dao cắt quả ớt chuông").
    2.  *Camera Control (Điều khiển Camera):* Các video quay quét đi kèm thông tin điều khiển camera thực tế (ví dụ: "Quay 360 độ theo chiều kim đồng hồ").
    3.  *Robot Control (Điều khiển Robot):* Video thao tác của robot đi kèm các lệnh điều khiển khớp thực tế (vector vận tốc hoặc tọa độ dịch chuyển $\Delta x, \Delta y$).
    4.  *Keyboard Control (Điều khiển Bàn phím):* Video chơi game đi kèm lịch sử nhấn phím của người chơi (ví dụ: gameplay Minecraft).

#### 3. Kỹ thuật đưa hành động vào mô hình (Action Conditioning)
*   **Thách thức cốt lõi:** Làm sao để biểu diễn hành động điều khiển liên tục (continuous control actions) của robot vào mô hình khuếch tán video một cách chính xác nhất?
*   **Khảo sát hai phương pháp:**
    *   *Phương pháp A (Dùng mã hóa chữ/Rời rạc hóa):* Đưa hành động qua các bộ nhúng văn bản (Text Embeddings của CLIP, T5) hoặc rời rạc hóa hành động thành các token rời rạc.
        *   *Kết quả thực nghiệm:* Thử nghiệm trong môi trường lưới gridworld (di chuyển khối hộp bằng vận tốc liên tục) cho thấy: Sử dụng Text Embedding (TinyLlama/CLIP) khiến robot ảo di chuyển rất giật cục, sai lệch vị trí nghiêm trọng và mô phỏng vật lý bị trôi dạt hoàn toàn.
    *   *Phương pháp B (Chiếu tuyến tính vector liên tục - Đề xuất):* Giữ nguyên vector hành động liên tục thô $\vec{a}$ và đưa qua một bộ chiếu tuyến tính (Linear Projection).
        *   *Công thức:* Với vector hành động $\vec{a} \in \mathbb{R}^d$, bộ chiếu sử dụng ma trận trọng số $W \in \mathbb{R}^{c \times d}$ để ánh xạ trực tiếp thành vector đặc trưng hành động $\vec{h}_a \in \mathbb{R}^c$:
            $$\vec{h}_a = W \cdot \vec{a}$$
            Đặc trưng $\vec{h}_a$ này sau đó được cộng thẳng vào không gian ẩn (latent space) của mô hình video diffusion (DiT/3D UNet).
        *   *Kết quả thực nghiệm:* Duy trì sự nhất quán vật lý hoàn hảo, khối hộp di chuyển mượt mà bám sát hoàn toàn vector vận tốc thực tế của robot.

#### 4. Lập kế hoạch dài hạn với Video Language Planning (VLP)
*   **Thách thức:** Sinh một video dài phức tạp biểu diễn toàn bộ quá trình robot thực hiện một nhiệm vụ dài hạn (Long Horizon Task) trong một lượt là cực kỳ khó và dễ bị suy giảm chất lượng theo thời gian.
*   **Công trình VLP (ICLR 2024):** Đề xuất cơ chế lập kế hoạch phân cấp kết hợp chặt chẽ giữa ngôn ngữ và video:
    1.  *Bước 1 (High-level):* Robot nhận nhiệm vụ dài hạn (ví dụ: "Dọn dẹp bàn ăn và cất quả táo vào ngăn kéo"). Một mô hình ngôn ngữ lớn (LLM) sẽ phân rã nhiệm vụ này thành một chuỗi các hành động chữ ngắn hạn (Language Plan):
        *   *Hành động 1:* Mở ngăn kéo tủ phía trên (Open the top drawer).
        *   *Hành động 2:* Bỏ quả táo vào ngăn kéo (Put the apple in the top drawer).
        *   *Hành động 3:* Đóng ngăn kéo lại (Close the top drawer).
    2.  *Bước 2 (Mid-level):* Với mỗi hành động chữ ngắn hạn, mô hình Text-to-Video đóng vai trò là một **Chính sách phổ quát (Universal Policy)** để sinh ra một đoạn video ngắn tương ứng thể hiện trạng thái robot hoàn thành bước đó thành công.
    3.  *Bước 3 (Low-level):* Đoạn video sinh ra được đưa vào một mô hình động học ngược (Inverse Dynamics Model) dựa trên dòng quang học (optical flow) hoặc chính sách hướng mục tiêu (goal-conditioned policy) để dịch các chuyển động trực quan trong video thành các vector hành động lực/vận tốc thực tế gửi đến các khớp của robot thật để thực thi ngoài đời thực.

#### 5. Đánh giá chính sách Robot trong Mô hình thế giới (Policy Evaluation)
*   **Vấn đề của phương pháp đánh giá cũ:**
    Đánh giá chính sách robot (Robot Policy) ngoài đời thực cực kỳ đắt đỏ và tốn thời gian ("robot bị hỏng"). Đánh giá trong các bộ giả lập vật lý truyền thống (software simulators) thì có mức độ tương quan cực kỳ kém so với kết quả thực tế ngoài đời thực do khoảng cách thực-ảo (sim-to-real gap).
*   **Quy trình đánh giá bằng Mô hình thế giới:**
    Chạy trực tiếp các hành động do chính sách của robot đưa ra vào trong mô hình thế giới để mô hình thế giới sinh ra các video giả lập (virtual rollouts). Sau đó, sử dụng một mô hình ngôn ngữ thị giác lớn (VLM) đóng vai trò làm bộ chấm điểm (VLM reward/evaluator) để đánh giá xem nhiệm vụ có hoàn thành thành công hay không.
*   **Hai (02) Loại Lỗi Sai lệch Chí mạng cần lưu ý:**
    Nghiên cứu *Evaluating Robot Policies in a World Model* (Arxiv 2025) chỉ ra hai loại sai lệch nghiêm trọng xảy ra do sự không hoàn hảo của mô hình thế giới:
    1.  **False Negative (Sai sót giả):**
        *   *Hiện tượng:* Robot thực tế đưa ra các quyết định hành động hoàn toàn chính xác và an toàn. Tuy nhiên, do mô hình thế giới chưa được huấn luyện tốt ở phân phối này, nó sinh ra một video giả lập bị lỗi hiển thị, méo mó vật lý hoặc vật thể tự biến mất. VLM đọc video lỗi này và đánh giá robot thất bại.
    2.  **False Positive (Chính xác giả):**
        *   *Hiện tượng:* Robot thực tế đưa ra hành động sai lệch, vụng về hoặc gây nhiễu (noisy policy). Tuy nhiên, mô hình thế giới có một "bộ lọc ưu tiên thành công" quá mạnh (strong success prior) hoặc gặp dữ liệu lạ ngoài phân phối (out-of-distribution), nó tự động "sửa sai" hành động của robot để kết xuất ra một video ảo cực kỳ hoàn hảo và thành công. VLM đọc video đẹp đẽ này và đánh giá robot thành công xuất sắc, dẫn đến việc đánh giá sai lệch năng lực thực tế của robot.

#### 6. Vòng lặp tự cải tiến Mô hình thế giới (Self-Improving loops)
Sherry Yang đề xuất hai cơ chế phản hồi để mô hình thế giới tự học và nâng cao năng lực:
*   **Cơ chế 1: AI Feedback (Phản hồi từ AI)**
    *   Sử dụng mô hình ngôn ngữ thị giác (VLM) để đánh giá và chấm điểm trực tiếp chất lượng các video sinh ra.
    *   Huấn luyện mô hình tạo video tự sửa lỗi và tự gỡ lỗi (Self-Correct / Self-Debug) thông qua kỹ thuật học tăng cường từ phản hồi (ví dụ: áp dụng thuật toán DPO cho mô hình sinh video như trong công trình *VideoAgent 2025*).
*   **Cơ chế 2: Execution Feedback (Phản hồi thực thi thực tế)**
    *   Thu thập dữ liệu phản hồi từ chính quá trình robot thực thi thất bại hoặc thành công ngoài đời thực.
    *   Sử dụng các thuật toán học lặp trực tuyến và tạo sinh dữ liệu (như DAgger, STaR) để cập nhật và tinh chỉnh trực tiếp mô hình thế giới, giúp bộ giả lập ảo ngày càng tiệm cận sát với các phản ứng vật lý thực tế.

---

### Tóm tắt các công trình nghiên cứu và liên kết quan trọng được đề cập:

#### Các bài báo chính được nghiên cứu trong video:
1.  **CUT3R — Continuous 3D Perception Model with Persistent State:** arXiv [https://arxiv.org/abs/2501.12387](https://arxiv.org/abs/2501.12387) | Trang dự án [https://cut3r.github.io/](https://cut3r.github.io/) | CVPR 2025
2.  **St4RTrack — Simultaneous 4D Reconstruction and Tracking in the World:** arXiv [https://arxiv.org/abs/2504.13152](https://arxiv.org/abs/2504.13152) | Trang dự án [https://st4rtrack.github.io/](https://st4rtrack.github.io/) | ICCV 2025
3.  **Video as the New Language for Real-World Decision Making:** arXiv [https://arxiv.org/abs/2402.17139](https://arxiv.org/abs/2402.17139) | ICML 2024

#### Các liên kết tham khảo khác:
4.  **Awesome-From-Video-Generation-to-World-Model:** Danh sách tổng hợp nghiên cứu [https://github.com/ziqihuangg/Awesome-From-Video-Generation-to-World-Model](https://github.com/ziqihuangg/Awesome-From-Video-Generation-to-World-Model)
5.  **Inductive Moment Matching (IMM):** Mã nguồn Luma AI [https://github.com/lumalabs/imm](https://github.com/lumalabs/imm)
6.  **Ideas in Inference-time Scaling:** [https://arxiv.org/abs/2503.07154](https://arxiv.org/abs/2503.07154)
7.  **Universal Simulator:** Dự án thử nghiệm [https://universal-simulator.github.io](https://universal-simulator.github.io)
8.  **World Model Policy Evaluation:** Đánh giá robot [https://world-model-eval.github.io](https://world-model-eval.github.io)
