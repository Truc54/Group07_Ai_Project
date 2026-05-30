import asyncio
import os
import edge_tts

SCRIPTS = {
    "scene_01": "Xin chào các bạn. Chào mừng đến với video kiến thức về trí tuệ nhân tạo. Trong video hôm nay, chúng ta sẽ cùng khám phá một trong những xu hướng nghiên cứu đang được quan tâm nhất hiện nay trong lĩnh vực AI — đó là hành trình từ tạo video bằng trí tuệ nhân tạo đến xây dựng các mô hình thế giới thông minh. Đây là một chủ đề nằm ở giao điểm của nhiều lĩnh vực: Computer Vision, Deep Learning, và Robotics.",
    
    "scene_02": "Tại sao chủ đề này lại quan trọng? Hãy tưởng tượng một ngày nào đó, bạn chỉ cần gõ một câu mô tả, và AI sẽ tạo ra một đoạn video chân thực đến mức không thể phân biệt với thực tế. Nhưng câu hỏi sâu hơn là: Liệu AI có thực sự hiểu thế giới khi tạo ra video đó? Hay nó chỉ đang sao chép các mẫu pixel? Đây chính là câu hỏi mà các nhà nghiên cứu hàng đầu đang cố gắng trả lời.",
    
    "scene_03": "Video sẽ được chia thành 3 phần chính. Phần thứ nhất: Kiến trúc tạo video AI thế hệ mới, chúng ta sẽ tìm hiểu 3D VAE, Spatiotemporal Attention, và kiến trúc MVL. Phần thứ hai: Streaming Perception, với hai phương pháp đột phá là CUT3R và ST4rtrack. Và phần thứ ba: Mở rộng mô hình thế giới cho robot, bao gồm dữ liệu lớn, Action Conditioning, và vòng lặp tự cải tiến. Nào, bắt đầu thôi!",
    
    "scene_04": "Phần 1: Kiến trúc tạo video AI thế hệ mới. Trong những năm gần đây, các mô hình tạo video bằng AI đã đạt được những bước tiến đáng kinh ngạc. Từ những đoạn video ngắn, nhòe mờ, đến các video dài tới 2 phút ở chất lượng 1080p với 30 khung hình mỗi giây. Vậy đằng sau sự tiến bộ này là những đột phá kỹ thuật nào? Hãy cùng tìm hiểu.",
    
    "scene_05": "Để hiểu tại sao kiến trúc mới lại cần thiết, trước tiên chúng ta cần biết phương pháp cũ gặp vấn đề gì. Các mô hình tạo video thế hệ đầu sử dụng 2D VAE. 2D VAE nén và giải nén từng khung hình một cách hoàn toàn độc lập với nhau. Nó coi mỗi khung hình như một bức ảnh riêng lẻ, không hề biết khung hình trước và sau trông như thế nào.",
    
    "scene_06": "Hệ quả của việc nén từng khung hình độc lập là gì? Đầu tiên là hiện tượng flickering, khi ánh sáng và màu sắc thay đổi đột ngột giữa hai khung hình liên tiếp. Tiếp theo là biến dạng cấu trúc khi vật thể chuyển động — ví dụ, khuôn mặt người bị méo khi quay đầu. Và nghiêm trọng nhất là hiện tượng temporal inconsistency, khi một vật thể có thể tự thay đổi hình dạng hoặc biến mất rồi xuất hiện lại giữa các khung hình.",
    
    "scene_07": "Giải pháp cho vấn đề này là 3D VAE. Ý tưởng cốt lõi rất trực quan: Thay vì nén từng khung hình riêng lẻ, hãy nén toàn bộ video cùng một lúc. 3D VAE xem video không phải là tập hợp các ảnh 2D rời rạc, mà là một khối dữ liệu 3D liên tục — bao gồm chiều ngang, chiều dọc, và chiều thời gian. Bằng cách nén đồng thời cả 3 chiều, mô hình giữ lại được mối liên hệ mượt mà giữa các khung hình liên tiếp.",
    
    "scene_08": "Hãy nhìn vào biểu diễn toán học. Video đầu vào V là một tensor 4 chiều: T khung hình, C kênh màu — thường là 3 kênh RGB, chiều cao H, và chiều rộng W. Khi đưa qua Encoder của 3D VAE, video được ánh xạ vào latent space z. Kết quả z có kích thước T mũ nhân C mũ nhân H mũ nhân W mũ. Trong đó, T mũ nhỏ hơn T thể hiện tỷ lệ nén thời gian, còn H mũ nhỏ hơn H và W mũ nhỏ hơn W thể hiện tỷ lệ nén không gian. Nhờ nén đồng thời không-thời gian, chi phí tính toán giảm đáng kể trong khi vẫn giữ được chuyển động mịn màng.",
    
    "scene_09": "Để hình dung rõ hơn, hãy tưởng tượng video gốc có 16 khung hình, mỗi khung 256 nhân 256 pixel. Sau khi đi qua 3D VAE với tỷ lệ nén thời gian 4 lần và tỷ lệ nén không gian 8 lần, ta thu được chỉ 4 token thời gian, mỗi token có kích thước 32 nhân 32. Lượng dữ liệu giảm đi 256 lần, nhưng thông tin quan trọng — đặc biệt là sự liên tục giữa các chuyển động — vẫn được bảo toàn.",
    
    "scene_10": "Bên cạnh 3D VAE, một cơ chế quan trọng khác giúp mô hình xử lý chuyển động phức tạp là Full Spatiotemporal Attention. Trong cơ chế Self-Attention thông thường, mỗi token chỉ tính attention với các token trong cùng một khung hình. Nhưng với Spatiotemporal Attention, mỗi latent token ở tọa độ x, y và t bất kỳ có thể tính attention với tất cả các token khác, bất kể ở khung hình hay vị trí nào.",
    
    "scene_11": "Nhờ cơ chế này, mô hình có thể xử lý hoàn hảo nhiều tình huống khó. Ví dụ: Vật thể chuyển động tốc độ cực nhanh mà không bị nhòe hình hay biến mất đột ngột. Các pha chuyển cảnh và thay đổi góc quay camera biên độ lớn mà không bị rách hình. Và đặc biệt, giữ được cấu trúc vật thể phức tạp — chẳng hạn các ngón tay khi múa, hay lông chim khi vỗ cánh — điều mà các mô hình cũ thường xuyên thất bại.",
    
    "scene_12": "Lõi xử lý trung tâm của các mô hình tạo video hiện đại là Diffusion Transformer, viết tắt là DiT. DiT kết hợp hai ý tưởng mạnh mẽ: quá trình Diffusion để sinh ra dữ liệu mới từ noise, và kiến trúc Transformer để mô hình hóa mối quan hệ giữa các token. Quá trình hoạt động như sau: bắt đầu từ random noise trong latent space, DiT lặp đi lặp lại việc denoising, mỗi bước tạo ra hình ảnh rõ nét hơn một chút, cho đến khi thu được video sạch hoàn chỉnh.",
    
    "scene_13": "Trước đây, mỗi tác vụ thị giác đều cần một mô hình riêng biệt. Muốn tạo video từ chữ? Dùng mô hình A. Muốn chỉnh sửa video? Dùng mô hình B. Muốn AI hiểu nội dung video? Dùng mô hình C. Ba mô hình độc lập, ba bộ trọng số riêng, không chia sẻ kiến thức với nhau. Điều này gây lãng phí tài nguyên và hạn chế khả năng tổng quát hóa.",
    
    "scene_14": "Xu hướng hiện nay là xây dựng một kiến trúc thống nhất duy nhất cho tất cả các tác vụ. Ý tưởng là sử dụng Multimodal Visual Language, viết tắt là MVL. Tất cả dữ liệu đầu vào như văn bản, hình ảnh, hay video đều được chuyển đổi thành chuỗi token chung thông qua các bộ tokenizer chuyên biệt. Chuỗi token thống nhất này sau đó được đưa vào lõi Diffusion Transformer để xử lý đồng thời. Các ứng dụng điển hình như Kling đã đạt được khả năng sinh video chất lượng cao lên đến 1080p, 30fps, dài tối đa 2 phút. Bên cạnh đó, các công nghệ vệ tinh như LivePortrait giúp sinh chuyển động chân dung từ ảnh tĩnh, hay Kling-Avatar giúp tạo nhân vật ảo 3D sinh động.",
    
    "scene_15": "Trong lĩnh vực tạo video AI, cộng đồng nghiên cứu đang tập trung vào 4 hướng phát triển chính. Hướng thứ nhất là nâng cấp kiến trúc mô hình và thuật toán tạo sinh, tối ưu hóa cấu trúc DiT để đẩy nhanh tốc độ hội tụ của quá trình Diffusion. Hướng thứ hai là tăng cường khả năng tương tác và điều khiển, cho phép điều khiển camera chính xác với các thao tác Pan, Zoom, Tilt, cũng như nhận biết lực tác động vật lý lên môi trường.",
    
    "scene_16": "Hướng thứ ba là thiết lập cơ chế đánh giá và căn chỉnh chính xác, xây dựng các thang đo đo lường mức độ chân thực vật lý và sự liên kết nội dung với prompt của người dùng. Hướng thứ tư là cải thiện nhận thức và suy luận đa phương thức, giúp mô hình không chỉ tạo ra video mà còn có khả năng giải thích cấu trúc chuyển động và các hiện tượng xảy ra trong đó.",
    
    "scene_17": "Vậy hãy tổng kết Phần 1. Chúng ta đã tìm hiểu 4 đột phá chính trong kiến trúc tạo video AI: 3D VAE giải quyết vấn đề flickering bằng cách nén đồng thời không gian và thời gian. Spatiotemporal Attention cho phép mô hình attend xuyên qua các khung hình. Diffusion Transformer sinh video từ noise qua quá trình denoising lặp lại. Và kiến trúc thống nhất MVL kết hợp mọi tác vụ trong một mô hình duy nhất. Nhưng một câu hỏi quan trọng vẫn còn: Video đẹp là chưa đủ — liệu mô hình có thực sự hiểu cấu trúc 3D của thế giới hay không?",
    
    "scene_18": "Phần 2: Nhận thức 3D liên tục từ video. Trong phần này, chúng ta sẽ khám phá cách xây dựng các mô hình AI có khả năng hiểu cấu trúc không gian 3 chiều từ luồng video liên tục — một bước tiến quan trọng từ tạo video sang xây dựng mô hình thế giới thực sự.",
    
    "scene_19": "Các mô hình tạo video hiện tại đạt mức độ chân thực trực quan đáng kinh ngạc. Chúng tạo ra sóng nước lấp lánh, phản chiếu ánh sáng hoàn hảo, bóng đổ chân thực. Người xem có cảm giác mô hình thực sự hiểu thế giới. Nhưng thực chất thì sao? Chúng chỉ là những pixel renderer siêu việt. Chúng học cách phân phối pixel trên mặt phẳng 2D để đánh lừa thị giác con người, nhưng bên trong hoàn toàn không có structured 3D representation nào cả.",
    
    "scene_20": "Vấn đề bộc lộ rõ nhất khi góc quay camera thay đổi hoặc khi vật thể bị che khuất. Mô hình không có bộ nhớ vật lý nào để nhớ rằng mặt sau của vật thể trông như thế nào. Kết quả là hiện tượng structural drift, khi hình dạng vật thể tự thay đổi dần. Hoặc hiện tượng morphing, vật thể tự biến đổi hình dạng phi vật lý khi bị che khuất rồi xuất hiện lại.",
    
    "scene_21": "Vậy giải pháp là gì? Câu trả lời là Streaming Perception. Ý tưởng này lấy cảm hứng từ cách con người nhận thức thế giới. Khi một đứa trẻ sơ sinh lớn lên, nó liên tục quan sát và tự xây dựng mô hình cấu trúc vật thể trong đầu. Khi ta đi bộ trong một căn phòng, não bộ cũng liên tục cập nhật một mô hình 3D bền vững. Hệ thống AI cũng phải hoạt động tương tự, liên tục cập nhật 3D representation từ luồng camera đầu vào.",
    
    "scene_22": "CUT3R, viết tắt của Continuous Updating Transformer for 3D Reconstruction, là một phương pháp hiện thực hóa ý tưởng Streaming Perception. CUT3R là một stateful recurrent Transformer. Điều đặc biệt là nó không xử lý từng khung hình độc lập, cũng không chạy global optimization đắt đỏ. Thay vào đó, nó duy trì một 3D Memory State.",
    
    "scene_23": "Quy trình hoạt động như sau: Tại mỗi bước thời gian t, khi camera nhận khung hình mới I t, Transformer của CUT3R sẽ nhận hai đầu vào: Recurrent 3D Memory State S t trừ 1, và khung hình mới I t. Nó so sánh thông tin trực quan mới với bộ nhớ cũ, chỉ tính toán và cập nhật phần thông tin thay đổi, rồi bồi đắp vào trạng thái bộ nhớ để sinh ra trạng thái mới S t.",
    
    "scene_24": "Công thức cập nhật rất ngắn gọn: S t bằng Transformer Update của S t trừ 1 và I t. Quá trình này diễn ra theo thời gian thực, với mỗi khung hình mới chỉ mất vài mili-giây để cập nhật, thay vì phải chạy global optimization đắt đỏ cho toàn bộ video.",
    
    "scene_25": "Một khả năng ấn tượng của CUT3R là xử lý vật thể bị che khuất. Hãy tưởng tượng camera đang nhìn thấy một chiếc bàn, rồi camera quay sang hướng khác. Chiếc bàn không còn trong khung hình nữa. Với mô hình thông thường, thông tin về chiếc bàn sẽ bị mất. Nhưng CUT3R giữ nguyên hình học của chiếc bàn trong bộ nhớ trạng thái, và khi camera quay trở lại, chiếc bàn được tái dựng nguyên vẹn, đúng vị trí và kích thước.",
    
    "scene_26": "Tiếp theo, chúng ta tìm hiểu ST4rtrack — một phương pháp giải quyết đồng thời bài toán point tracking và 4D reconstruction trong một World Coordinate Frame thống nhất. Để hiểu tại sao đây là đột phá, hãy xem cách truyền thống. Trong Computer Vision truyền thống, hai bài toán này được chia làm 2 bước riêng biệt chạy nối tiếp nhau. Bước 1: Dùng Optical Flow để theo dõi vết các điểm ảnh di chuyển trên mặt phẳng 2D. Bước 2: Dùng thuật toán Structure from Motion để từ các điểm 2D dựng thành mô hình 3D.",
    
    "scene_27": "Vấn đề nghiêm trọng là hai bước này hoạt động hoàn toàn độc lập và không chia sẻ thông tin. Nếu Optical Flow ở bước một chỉ cần sai lệch vài pixel do nhiễu hoặc ánh sáng, Structure from Motion ở bước hai sẽ nhận đầu vào sai. Sai số này sẽ bị phóng đại, dẫn đến tọa độ 3D bị méo mó và làm sụp đổ toàn bộ mô hình tái dựng.",
    
    "scene_28": "ST4rtrack giải quyết vấn đề này một cách triệt để bằng cách xử lý đồng thời cả hai bài toán tracking và reconstruction trong một feed-forward model duy nhất. Không còn 2 bước riêng biệt nữa. Mô hình dự đoán trực tiếp một Spatiotemporal Pointmap trong một World Coordinate Frame thống nhất.",
    
    "scene_29": "Biểu diễn toán học như sau: Với mỗi điểm i trên bề mặt vật thể, dù tĩnh hay động, mô hình dự đoán tọa độ 3D liên tục theo thời gian t. P i t là một vector gồm X i t, Y i t, và Z i t trong không gian 3 chiều. Việc tích hợp này giúp hình học 3D bổ trợ ngược lại cho tracking 2D, triệt tiêu hoàn toàn sai số tích lũy.",
    
    "scene_30": "Hãy so sánh hai phương pháp. CUT3R tập trung vào việc cập nhật liên tục 3D Memory State theo thời gian thực từ video stream, sử dụng cơ chế recurrent. Trong khi đó, ST4rtrack tập trung dự đoán 4D Pointmap cho cả vật thể tĩnh lẫn động bằng mô hình feed-forward, theo dõi tọa độ 3D của mọi điểm liên tục theo thời gian. Cả hai đều hướng tới việc xây dựng structured representation bền vững của thế giới.",
    
    "scene_31": "Tổng kết Phần 2: Chúng ta đã thấy rằng video đẹp là chưa đủ — mô hình AI cần hiểu cấu trúc 3D thực sự. Streaming Perception đặt nền tảng lý thuyết. CUT3R hiện thực hóa bằng Transformer hồi quy với bộ nhớ 3D bền vững. ST4rtrack giải quyết đồng thời theo dõi và tái dựng 4D trong một mô hình duy nhất. Câu hỏi cuối cùng: Làm sao tận dụng tất cả những khả năng này để xây dựng mô hình thế giới giúp robot hành động thông minh?",
    
    "scene_32": "Phần 3: Mở rộng mô hình thế giới cho robot thông minh. Trong phần cuối cùng này, chúng ta sẽ tìm hiểu cách biến các mô hình tạo video thành các bộ giả lập thế giới để huấn luyện và đánh giá robot — một trong những ứng dụng đầy hứa hẹn nhất của AI hiện nay.",
    
    "scene_33": "Ý tưởng về mô hình thế giới đã tồn tại từ lâu trong Reinforcement Learning. Năm 2018, nghiên cứu World Models cho phép agent học trong môi trường giả lập do chính mô hình tạo ra. Từ 2020 đến 2023, loạt công trình Dreamer từ phiên bản V1 đến V3 tiếp tục phát triển ý tưởng này. Tuy nhiên, các mô hình cũ chỉ hoạt động trong môi trường nhỏ và đơn giản như game Atari hay MuJoCo. Điểm khác biệt ngày nay nằm ở hai yếu tố: dữ liệu quy mô Internet và kiến trúc có khả năng mở rộng.",
    
    "scene_34": "Mô hình thế giới hiện đại được huấn luyện trên tập dữ liệu khổng lồ gồm 21 triệu cặp time-aligned video và action data từ 4 nguồn dữ liệu đa dạng. Điểm mấu chốt là mỗi hành động phải khớp chính xác với từng khung hình video tương ứng. Ý tưởng cốt lõi là biến video thành một ngôn ngữ chung cho việc ra quyết định. Video không chỉ là hình ảnh động, mà là biểu diễn trực quan của các hành động và hệ quả của chúng.",
    
    "scene_35": "4 nguồn dữ liệu bao gồm: Thứ nhất, cặp văn bản và video — ví dụ video một người đang dùng dao cắt ớt chuông, đi kèm mô tả hành động. Thứ hai, điều khiển camera — video quay quét đi kèm thông tin xoay 360 độ. Thứ ba, điều khiển robot — video thao tác robot đi kèm vector vận tốc khớp delta x, delta y. Và thứ tư, điều khiển bàn phím — video chơi game như Minecraft đi kèm lịch sử nhấn phím. Sự đa dạng này giúp mô hình học được các quy luật vật lý tổng quát.",
    
    "scene_36": "Một thách thức cốt lõi khi xây dựng World Model là: Làm sao đưa continuous control action của robot vào video diffusion model một cách chính xác nhất? Nếu dùng phương pháp discretization hoặc dùng text embedding, kết quả thực nghiệm cho thấy robot trong video di chuyển rất giật cục, sai lệch vị trí nghiêm trọng, và mô phỏng vật lý bị drift.",
    
    "scene_37": "Giải pháp hiệu quả nhất lại là phương pháp đơn giản nhất: Linear Projection. Giữ nguyên raw action vector a, rồi nhân với weight matrix W để ánh xạ thành action feature vector h a. Công thức cực kỳ đơn giản: h a bằng W nhân a. Action feature h a sau đó được cộng trực tiếp vào latent space của mô hình video. Kết quả giúp robot di chuyển mượt mà, bám sát chính xác vector vận tốc thực tế. Bài học rút ra: đôi khi giải pháp đơn giản nhất lại hiệu quả nhất.",
    
    "scene_38": "Tiếp theo, làm sao để robot thực hiện các nhiệm vụ dài hạn phức tạp? Ví dụ như dọn dẹp bàn ăn và cất quả táo vào ngăn kéo. Sinh một video dài thể hiện toàn bộ quá trình trong một lượt là cực kỳ khó và dễ bị suy giảm chất lượng. Giải pháp là Video Language Planning, viết tắt VLP, một cơ chế lập kế hoạch phân cấp kết hợp giữa ngôn ngữ và video.",
    
    "scene_39": "VLP chia quá trình thành 3 cấp. Cấp cao: LLM nhận nhiệm vụ tổng thể và phân rã thành các hành động bằng chữ ngắn hạn. Ví dụ: Bước 1 mở ngăn kéo, bước 2 bỏ quả táo vào, bước 3 đóng ngăn kéo. Cấp trung: Với mỗi hành động, mô hình Text-to-Video đóng vai trò Universal Policy, sinh ra video ngắn thể hiện robot hoàn thành bước đó thành công. Cấp thấp: Video sinh ra được đưa vào Inverse Dynamics Model để dịch thành các motor command gửi đến các khớp robot.",
    
    "scene_40": "Khi đã có robot policy, câu hỏi tiếp theo là: Làm sao evaluate policy đó mà không cần chạy robot thật, vì robot thật tốn kém và có thể bị hỏng? Đánh giá trong các simulator truyền thống thì sim-to-real gap quá lớn, kết quả hầu như không tương quan với thực tế.",
    
    "scene_41": "Giải pháp: Dùng chính mô hình thế giới làm bộ giả lập. Chạy các hành động do robot policy đưa ra vào mô hình thế giới để sinh video giả lập. Sau đó, sử dụng VLM đóng vai trò bộ chấm điểm để đánh giá xem nhiệm vụ có thành công hay không.",
    
    "scene_42": "Tuy nhiên, phương pháp này có hai loại lỗi chí mạng cần lưu ý. Lỗi thứ nhất là False Negative: Robot thực tế hành động hoàn toàn đúng, nhưng mô hình thế giới render video bị lỗi hiển thị hoặc méo mó vật lý, khiến VLM đánh giá robot thất bại. Lỗi thứ hai là False Positive: Robot hành động sai và vụng về, nhưng mô hình thế giới tự sửa sai, tự kết xuất video thành công, khiến VLM đánh giá robot đạt. Cả hai lỗi đều nguy hiểm.",
    
    "scene_43": "Để khắc phục các lỗi này và liên tục cải thiện, mô hình thế giới sử dụng 2 cơ chế phản hồi. Cơ chế 1 là AI Feedback: VLM chấm điểm chất lượng video sinh ra, sau đó dùng DPO để huấn luyện mô hình tự sửa lỗi. Cơ chế 2 là Execution Feedback: Thu thập dữ liệu từ quá trình robot thực thi thực tế, rồi dùng thuật toán DAgger hoặc STaR để cập nhật mô hình.",
    
    "scene_44": "Tổng kết Phần 3: Mô hình thế giới cho robot cần 3 yếu tố. Một là dữ liệu quy mô lớn, với 21 triệu cặp time-aligned video và action data. Hai là kỹ thuật đưa hành động vào mô hình chính xác bằng Linear Projection. Ba là cơ chế tự cải tiến qua AI Feedback và Execution Feedback. Video Language Planning giúp robot thực hiện nhiệm vụ dài hạn, và mô hình thế giới đóng vai trò bộ giả lập để đánh giá robot policy.",
    
    "scene_45": "Và đó là toàn bộ hành trình từ tạo video AI đến mô hình thế giới. Chúng ta đã đi qua 3 trụ cột chính. Trụ cột thứ nhất: Kiến trúc tạo video thế hệ mới với 3D VAE, Spatiotemporal Attention, và kiến trúc MVL. Trụ cột thứ hai: Streaming Perception với CUT3R xây dựng bộ nhớ 3D bền vững và ST4rtrack theo dõi tái dựng 4D đồng thời. Và trụ cột thứ ba: Mô hình thế giới cho robot với dữ liệu quy mô Internet, Action Conditioning bằng Linear Projection, và vòng lặp tự cải tiến. Tương lai của AI không chỉ là tạo ra hình ảnh đẹp, mà là thực sự hiểu và tương tác với thế giới. Cảm ơn các bạn đã theo dõi!"
}

VOICE = "vi-VN-HoaiMyNeural"

async def generate_all():
    os.makedirs("voiceover", exist_ok=True)
    for name, text in SCRIPTS.items():
        path = f"voiceover/{name}.mp3"
        print(f"🎤 Generating {path}...")
        if os.path.exists(path):
            print(f"  Already exists, skipping!")
            continue
        try:
            communicate = edge_tts.Communicate(text, VOICE)
            await communicate.save(path)
            print(f"  ✅ Success!")
        except Exception as e:
            print(f"  ❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(generate_all())
