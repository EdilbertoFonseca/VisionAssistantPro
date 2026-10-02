# Dokumentasi Vision Assistant Pro

<!-- DOWNLOAD_COUNT_START --> Total Unduhan: 62.863 <!-- DOWNLOAD_COUNT_END -->

**Vision Assistant Pro** adalah asisten AI multimodal tingkat lanjut untuk NVDA. Add-on ini memakai mesin AI kelas dunia untuk membantu pembacaan layar cerdas, penerjemahan, dikte suara, dan analisis dokumen.

_Add-on ini dirilis untuk komunitas dalam rangka memperingati Hari Internasional Penyandang Disabilitas._

## 1. Pengaturan & Konfigurasi

Buka **Menu NVDA > Preferensi > Pengaturan > Vision Assistant Pro**. Dialog pengaturan tersusun dalam 9 tab yang aksesibel: **Koneksi**, **Asisten Langsung**, **Perilaku AI**, **Bahasa Terjemahan**, **Pembaca Dokumen**, **Video**, **CAPTCHA**, **Prompt**, dan **Lanjutan**.

### 1.1 Tab Koneksi

- **Penyedia:** Pilih layanan AI yang ingin Anda gunakan. Penyedia yang didukung meliputi **Google Gemini**, **OpenAI**, **Mistral**, **Groq**, **MiniMax**, dan **Kustom** (server yang kompatibel dengan OpenAI seperti Ollama, LM Studio, Jan.ai, atau KoboldCPP).
- **Kunci API:** Masukkan satu atau beberapa kunci API (dipisahkan dengan koma atau baris baru) untuk rotasi otomatis.
- **Ambil Model:** Setelah kunci API dimasukkan, tekan tombol ini untuk mengunduh daftar model terbaru dari penyedia.
- **Model AI:** Pilih model utama untuk obrolan umum dan analisis.
- **Pengaturan Penyedia Kustom:** Konfigurasikan endpoint lokal atau kustom. Bagian ini mencakup **Siapkan AI Lokal** (pengaturan sekali klik untuk Ollama, LM Studio, Jan.ai, atau KoboldCPP) dan **Konfigurasi Endpoint Lanjutan**.
- **Perutean Model Lanjutan (Khusus Tugas):** Anda dapat memilih model khusus dari daftar untuk tugas OCR, STT, TTS, Operator AI, Video, dan Asisten Langsung.
- **Opsi Koneksi & Keluaran:** Atur URL Proksi, pemeriksaan pembaruan saat mulai, Bersihkan Markdown dalam Obrolan, salin respons AI ke papan klip, dan Keluaran Langsung (Tanpa Jendela Obrolan).
- **Simpan obrolan ke riwayat:** Menyimpan percakapan Anda dalam daftar Riwayat.

### 1.2 Tab Asisten Langsung

- **Asisten Langsung: Keluaran Langsung (Tanpa Jendela):** Memulai Asisten Langsung tanpa jendela percakapan. Anda dapat membukanya nanti dengan tombol Buka Hasil Terakhir (`Space`).
- **Tekan untuk Bicara:** Saat diaktifkan, mikrofon hanya mengirim audio selama Anda menahan tombol yang ditetapkan.
- **Tombol Tekan untuk Bicara:** Tekan tombol yang ingin dijadikan pintasan (misalnya `F12` atau `Ctrl+F12`). Anda juga dapat memakai satu tombol pengubah, seperti `Left Ctrl` (Ctrl kiri). Tahan tombol untuk berbicara, lalu lepaskan setelah selesai. Bunyi bip singkat menandai setiap penekanan dan pelepasan tombol.

Catatan: Tab ini hanya muncul jika penyedia aktif Anda adalah **Google Gemini** atau penyedia Kustom yang kompatibel dengan Gemini.

### 1.3 Tab Perilaku AI

- **Kreativitas (Temperature):** Mengatur keacakan dan kreativitas AI (dari 0,0 hingga 2,0). Nilai lebih rendah menghasilkan terjemahan dan OCR yang lebih konsisten serta akurat.

### 1.4 Tab Bahasa Terjemahan

- **Bahasa Sumber:** Pilih bahasa masukan bawaan.
- **Bahasa Target:** Pilih bahasa utama tujuan terjemahan.
- **Bahasa Respons AI:** Pilih bahasa untuk respons AI secara umum.
- **Pertukaran Cerdas:** Menukar bahasa sumber dan target secara otomatis berdasarkan masukan yang terdeteksi.

### 1.5 Tab Pembaca Dokumen

- **Mesin OCR:** Pilih **Chrome (Cepat)** untuk hasil cepat atau **AI (Lanjutan)** untuk mempertahankan tata letak dengan lebih baik.
- **Ukuran Batch OCR:** Tentukan jumlah halaman per permintaan (atur ke 0 agar diproses dalam satu permintaan).
- **Deskripsikan Gambar dalam Teks:** Aktifkan deskripsi gambar di antara teks saat mengekstrak teks dokumen.
- **Ekspor Nomor Halaman:** Aktifkan nomor dan pemisah halaman pada keluaran dokumen multihalaman.
- **Suara TTS:** Pilih gaya suara bawaan untuk pembuatan audio.
- **Simpan dokumen ke riwayat:** Menyimpan dokumen yang dibuka dalam daftar Riwayat. Teks OCR dalam cache dan data untuk melanjutkan proses tetap disimpan meskipun opsi ini dinonaktifkan.

### 1.6 Tab Video

- **Ukuran Potongan Video:** Tentukan durasi segmen dalam menit untuk pembuatan Deskripsi Audio (atur ke 0 untuk memproses seluruh file).
- **Tambahkan Daftar Karakter:** Tambahkan kamus karakter sebagai entri subtitel pertama.
- **Tambahkan Penafian AI:** Sisipkan penafian AI di awal subtitel SRT video.
- **Kamus Karakter & Pengelolaan Serial:** Tambahkan, edit, impor, atau kelola nama, ciri fisik, dan peran karakter untuk setiap serial. AI mencocokkan karakter yang ditemukan dengan kamus Anda dan menambahkan karakter baru saat Anda menganalisis episode berikutnya. Catatan yang Anda tulis sendiri selalu diutamakan dibanding pembaruan AI, sementara deskripsi fisik diperbarui sesuai episode.

### 1.7 Tab CAPTCHA

- **Aktifkan Pemecah CAPTCHA Visual:** Aktifkan pemecahan tantangan visual otomatis (hCaptcha, reCAPTCHA).
- **Metode CAPTCHA Teks:** Pilih antara menangkap **Objek Navigator** atau **Layar Penuh**.

### 1.8 Tab Prompt

- **Kelola Prompt:** Membuka dialog untuk menyesuaikan Prompt sistem bawaan atau membuat, mengedit, mengurutkan ulang, dan mempratinjau Prompt kustom dengan variabel dinamis seperti `[selection]` dan `[screen_fg_obj]`.

- **Pintasan Prompt Kustom:** Tetapkan pintasan untuk setiap prompt kustom langsung di Pengelola Prompt. Tekan tombol yang ingin digunakan: tombol tunggal dijalankan dalam Lapisan Perintah dan secara global melalui `NVDA + Shift + tombol`, sedangkan kombinasi seperti `Control + Shift + 1` dapat langsung digunakan secara global.

### 1.9 Tab Lanjutan & Pencatatan Global

Buka tab **Lanjutan** untuk mengatur pencatatan global add-on:

- **Aktifkan file log khusus:** Mencatat semua peristiwa operasional, lalu lintas API, dan error dari seluruh modul add-on ke file terpisah (`vision_assistant.log`).
- **Tingkat Log:** Pilih tingkat perincian antara **Debug (Semua Detail)**, **Info (Informasi Umum)**, **Peringatan (Hanya Peringatan)**, dan **Kesalahan (Hanya Kesalahan)**.
- **Simpan Log Selama:** Atur masa penyimpanan dari 1 jam hingga 90 hari. Entri yang lebih lama akan dibersihkan secara otomatis.
- **Kontrol Pengelolaan Log:** Gunakan **Buka File Log**, **Buka Folder Log**, atau **Bersihkan File Log** untuk memeriksa atau membersihkan data log tanpa memulai ulang NVDA dan tanpa mengganggu log standar NVDA.

- **Folder Data Terpadu:** Semua file data add-on (riwayat, serial, label, progres OCR, cache, dan log) disimpan dalam satu folder `VisionAssistant` di folder konfigurasi NVDA. Data menjadi lebih tertata dan mudah dicadangkan secara manual.

### 1.10 Pencadangan & Pemulihan Pengaturan

Tab **Lanjutan** juga memiliki bagian **Pencadangan dan Pemulihan**:

- **Cadangkan:** Menyimpan konfigurasi dalam satu file JSON. Anda dapat memilih **Semuanya** (pengaturan, label kustom, progres OCR, dan riwayat) atau **Pengaturan Saja**.
- **Pulihkan:** Memuat cadangan untuk memulihkan pengaturan dan data kapan saja, di komputer lain, atau setelah menginstal ulang NVDA. Anda akan diminta mengonfirmasi karena pemulihan mengganti pengaturan dan data saat ini sesuai isi cadangan.

## 2. Lapisan Perintah & Pintasan

Untuk mencegah konflik tombol keyboard, add-on ini memakai **Lapisan Perintah**.

1. Tekan **NVDA + Shift + V** (Tombol Utama) untuk mengaktifkan lapisan (Anda akan mendengar bunyi bip).
2. Lepaskan tombol, lalu tekan salah satu tombol tunggal berikut:

| Tombol        | Fungsi                 | Deskripsi                                                                  |
|---------------|------------------------|----------------------------------------------------------------------------|

| **Shift + A** | **Operator AI**        | **Operasi Mandiri:** Minta AI melakukan tugas di layar Anda. Tekan lagi untuk langsung membatalkan operasi yang sedang berjalan. |
| **E**         | **UI Explorer**        | **Klik Interaktif:** Mengenali dan mengklik elemen UI di aplikasi apa pun. |
| **T**         | Penerjemah Cerdas      | Menerjemahkan teks di kursor navigator atau teks yang dipilih.             |
| **Shift + T** | Penerjemah Papan Klip  | Menerjemahkan isi papan klip saat ini.                                     |
| **R**         | Penyempurna Teks       | Meringkas, memperbaiki tata bahasa, menjelaskan, atau menjalankan **Prompt Kustom**. |
| **V**         | Visi Objek             | Mendeskripsikan Objek Navigator saat ini.                                  |
| **O**         | Visi Layar Penuh       | Menganalisis tata letak dan isi seluruh layar.                             |
| **Shift + V** | Analisis Video         | Menganalisis file video lokal atau video online **YouTube**, **Instagram**, **TikTok**, atau **Twitter (X)**. |
| **Control + V** | Perekaman Video Lokal | Merekam video tanpa suara dari layar Anda dan menganalisis tindakan serta tata letaknya. |
| **D**         | Pembaca Dokumen        | Pembaca lanjutan untuk PDF, gambar, serta file teks biasa/HTML dengan pilihan rentang halaman.      |
| **F**         | **Tindakan File Cerdas** | Mengenali konteks dari file gambar, PDF, atau TIFF yang dipilih.          |
| **M**         | Transkripsi dan Sulih Suara Media | Mentranskripsikan atau menyulihsuarakan file audio/video ke bahasa target. |
| **C**         | Pemecah CAPTCHA        | Menangkap dan memecahkan CAPTCHA.                                          |
| **Shift + C** | Obrolan Langsung       | Membuka antarmuka obrolan berbasis teks secara langsung dengan AI.         |
| **S**         | Dikte Cerdas           | Mengubah ucapan menjadi teks. Tekan untuk mulai merekam, tekan lagi untuk berhenti dan mengetik hasilnya. |
| **Control+T** | Terjemahan Suara       | Mentranskripsikan, menerjemahkan, lalu mengetik hasil sesuai pengaturan bahasa. |
| **Control+L** | **Asisten Langsung**   | **Kopilot Real-time (Khusus Gemini):** Memulai atau mengakhiri percakapan suara dan layar langsung dengan asisten AI. |
| **I**         | Laporan Status         | Mengumumkan progres saat ini (misalnya, "Memindai...", "Siaga").           |
| **L**         | **Label Objek**        | **Pelabelan AI Semantik:** Memberi label permanen pada elemen/ikon fokus saat ini. |
| **Shift + L** | **Kelola/Pindai Label** | Membuka Pengelola Label (jika label sudah ada) atau memindai aplikasi untuk elemen tanpa nama. |
| **U**         | Cek Pembaruan          | Mengecek versi terbaru add-on di GitHub secara manual.                     |
| **Space**     | Buka Hasil Terakhir    | Menampilkan respons AI terakhir di dialog obrolan untuk ditinjau atau ditindaklanjuti. |
| **H**         | Bantuan Perintah       | Menampilkan daftar semua pintasan yang tersedia.                           |
| **Control + H** | **Riwayat** | Membuka daftar obrolan dan dokumen sebelumnya, dengan filter jenis serta pilihan Hapus dan Hapus Semua. |
| **Alt + S**   | Pengaturan             | Membuka dialog pengaturan Vision Assistant Pro secara instan.               |
| **Alt + Q**   | Laporan Kunci Kuota Habis | Melaporkan jumlah kunci API Gemini yang telah melebihi kuota harian beserta waktu pemulihan kuotanya. |
| **Alt + M**   | Audit Perutean         | Melaporkan model AI yang saat ini dipilih dalam perutean lanjutan.         |
| **Up / Down** | Navigasi Pengaturan Cepat | Berpindah antar kategori Pengaturan Cepat di dalam lapisan.              |
| **Left / Right** | Ubah Pengaturan Cepat | Mengubah nilai Pengaturan Cepat yang sedang dipilih.                       |

## 3. Obrolan & Riwayat

Jendela obrolan dan dialog Riwayat tersedia untuk berbagai fitur, sehingga Anda dapat meninjau percakapan dan melanjutkannya dari posisi terakhir.

### 3.1 Pintasan Jendela Obrolan

Saat jendela obrolan terbuka (Obrolan Langsung, obrolan dokumen, penyempurnaan teks, dan lainnya), gunakan:

- **Alt + Down:** Membaca pesan berikutnya.
- **Alt + Up:** Membaca pesan sebelumnya.
- **Alt + C:** Menyalin pesan saat ini.

### 3.2 Riwayat (Control + H)

Tekan **Control + H** dalam Lapisan Perintah untuk membuka **Riwayat** obrolan dan dokumen. Gunakan filter Semua / Obrolan / Dokumen untuk memilih jenis yang ditampilkan. Buka obrolan untuk melanjutkan percakapan; file lampirannya akan dilampirkan kembali secara otomatis. Anda juga dapat membuka dokumen untuk melanjutkan membaca. Tekan **Delete** pada suatu item untuk menghapusnya, atau **Hapus Semua** untuk mengosongkan daftar. Untuk dokumen, Anda dapat memilih menghapus entri riwayat saja atau sekaligus teks OCR dalam cache agar dokumen dipindai ulang dari awal saat dibuka kembali. Centang **Jangan tanyakan lagi** untuk mengingat pilihan tersebut.

Anda dapat mengatur apa yang disimpan dalam daftar ini. **Simpan obrolan ke riwayat** (tab Koneksi) dan **Simpan dokumen ke riwayat** (tab Pembaca Dokumen) aktif secara bawaan. Keduanya juga dapat diubah melalui Pengaturan Cepat. Opsi dokumen hanya memengaruhi entri Riwayat; teks OCR dalam cache dan data untuk melanjutkan proses tetap disimpan.

## 4. Operator AI - Kontrol Komputer Mandiri

**Operator AI** mengubah Vision Assistant Pro dari pembaca pasif menjadi asisten aktif yang dapat berinteraksi dengan komputer untuk Anda. Anda dapat memintanya mendeskripsikan layar, menjawab pertanyaan tentang apa yang dilihatnya, atau bahkan mengambil kendali - mengklik tombol, menyeret item, mengetik teks, dan menavigasi aplikasi dengan perintah bahasa alami.

Keunggulan terbesarnya adalah kemampuan bekerja di perangkat lunak yang sama sekali tidak aksesibel. Jika Anda terjebak di aplikasi kustom, desktop jarak jauh, atau situs web yang membuat pembaca layar benar-benar diam, Operator AI tetap dapat membantu. Karena "melihat" layar secara visual, fitur ini dapat menemukan, membaca, dan berinteraksi dengan elemen tanpa label aksesibilitas.

### Cara Kerja

1. Tekan **NVDA + Shift + V**, lalu **Shift + A** (atau gunakan pintasan langsung) untuk membuka dialog Operator AI.
2. Ketik tindakan yang Anda inginkan dengan bahasa biasa, misalnya "Klik tombol Simpan", "Apa isi pesan error?", atau "Ubah nama file menjadi final.pdf".
3. AI akan menganalisis layar, mengenali elemen yang sesuai, lalu menjalankan tindakan atau memberikan jawaban. Jika tugas memerlukan beberapa langkah, Operator AI akan terus bekerja hingga selesai.
4. Tekan **Shift + A** lagi kapan saja untuk langsung membatalkan operasi yang sedang berlangsung.

### Tindakan yang Didukung

Operator AI memahami beragam perintah:

- **Deskripsikan & Jawab:** "Deskripsikan tata letak layar" atau "Apa isi pesan error?"
- **Klik:** "Klik tombol Simpan"
- **Klik Kanan:** "Klik kanan file tersebut"
- **Klik Ganda:** "Klik ganda dokumen tersebut"
- **Seret & Lepas:** "Seret dokumen ke folder Arsip"
- **Ketik:** "Ketik 'Hello World' di kotak pencarian"
- **Gulir:** "Gulir ke bawah tiga kali"
- **Tekan Tombol:** "Tekan Enter", "Tekan Tab", "Tekan Escape"
- **Tugas Bertahap:** "Buka File Explorer, cari laporan, lalu ubah namanya menjadi final.pdf"

### Catatan Penting

- **Peringatan Penggunaan API:** Karena Operator AI perlu "melihat" apa yang terjadi di layar, fitur ini mengirim tangkapan layar beresolusi tinggi pada setiap langkah. Penggunaan yang sering akan menghabiskan kuota API lebih cepat daripada fitur berbasis teks.
- **Aplikasi Administrator:** Jika NVDA tidak dijalankan dengan hak Administrator, Operator AI mungkin tidak dapat berinteraksi dengan jendela yang memerlukan izin lebih tinggi. Ini adalah batasan keamanan Windows, bukan bug add-on.
- **Praktik Terbaik:** Berikan perintah yang jelas dan spesifik. "Klik tombol Kirim berwarna biru di bagian bawah formulir" hampir selalu lebih efektif daripada sekadar "Klik tombol".

## 5. Analisis Video & Deskripsi Audio

> **Catatan:** Fitur Analisis Video dan Deskripsi Audio didukung sepenuhnya oleh penyedia **Google Gemini**. Pastikan penyedia aktif Anda di pengaturan add-on diatur ke Google Gemini.

Vision Assistant Pro memperkenalkan kemampuan pemrosesan video andal yang dirancang khusus untuk pengguna tunanetra. Add-on ini dapat menganalisis video online dan rekaman layar lokal untuk memberikan deskripsi visual yang sangat mendetail dan menghasilkan skrip Deskripsi Audio (SRT) profesional.

### 5.1 Perekaman Layar Lokal (Control + V)

Jika Anda menemukan video tanpa suara, animasi, atau tutorial di layar, Anda dapat merekamnya secara langsung:

1. Tekan **NVDA + Shift + V** untuk masuk ke Lapisan Perintah, lalu tekan **Control + V**.
2. Add-on akan merekam layar Anda secara diam-diam di latar belakang.
3. Tekan **Control + V** lagi untuk menghentikan perekaman.
4. AI kemudian akan menganalisis segmen video yang direkam dan memberikan deskripsi yang sangat mendetail tentang pemandangan, karakter, dan tindakan.

### 5.2 Analisis Video (Shift + V)

Anda dapat menganalisis file video lokal maupun video online. Cukup pilih file video lokal di Windows Explorer, atau salin tautan video online ke papan klip Anda. Anda juga dapat menekan **Shift + V** di mana saja (seperti di dalam pemutar media) untuk membuka dialog tempat Anda dapat menelusuri file video atau menempelkan URL secara manual.

- **Platform Online yang Didukung:** YouTube, Instagram, TikTok, dan Twitter (X).
- AI akan mendeteksi file lokal atau URL secara otomatis, memproses video, dan memberikan deskripsi visual serta ringkasan audio yang komprehensif.
- **Cache File Video Selama 48 Jam:** Video yang diunggah ke Gemini disimpan dalam cache selama 48 jam. Anda dapat membuat ulang SRT atau MP3 untuk video yang sama tanpa mengunggah ulang, bahkan setelah memulai ulang NVDA. Cache terkait dengan kunci API dan otomatis tidak berlaku lagi jika kunci tersebut berubah.

### 5.3 Pembuatan Deskripsi Audio (SRT)

Untuk pengalaman yang lebih terstruktur, add-on dapat menghasilkan skrip Deskripsi Audio profesional dalam format standar SubRip (SRT).

- **Pengaturan Waktu Jeda Cerdas:** AI mendengarkan trek audio dan menempatkan deskripsi visual pada jeda hening alami untuk meminimalkan tumpang tindih dengan dialog.
- **Pelacakan Karakter:** Mesin terlebih dahulu mengenali karakter berdasarkan ciri wajah yang tetap, lalu membuat kamus global agar identitas mereka konsisten di berbagai adegan. Mesin juga melacak **kemunculan pertama** setiap karakter. Penampilan fisik hanya dijelaskan saat karakter pertama kali muncul; adegan selanjutnya cukup menyebut namanya agar narasi tidak berulang.
- **OCR Teks Verbatim:** Teks apa pun yang muncul di layar (papan tanda, ponsel, kredit) dikutip secara tepat apa adanya.
- **Cara Menggunakan:** Untuk mendengarkan subtitel yang dihasilkan, cukup letakkan file `.srt` di folder yang sama dengan file video Anda dan beri nama yang sama persis. Kemudian, konfigurasikan pemutar media Anda (misalnya, VLC atau PotPlayer) untuk mengarahkan teks subtitel langsung ke pembaca layar atau mesin TTS Anda selama pemutaran.

- **Penyimpanan yang Lebih Mudah:** Saat menyimpan SRT atau MP3, dialog penyimpanan otomatis membuka folder video sumber, baik video dibuka melalui dialog file maupun melalui Shift+V dari Explorer.

### 5.4 Narasi Audio Tersinkron (Ekspor MP3)

Selain membuat file SRT berbasis teks, add-on ini berfungsi sebagai alat produksi Deskripsi Audio lengkap dengan mengubah deskripsi menjadi ucapan dan mencampurnya dengan video. Anda dapat memilih **Gemini Live TTS** sebagai mesin suara. Mesin ini menggunakan Gemini Live API untuk menghasilkan narasi suara yang sangat realistis tanpa batas. Saat membuat MP3 untuk file video lokal, tersedia beberapa mode pencampuran:

- **AD Standar (Campur Suara):** Narasi diputar langsung di atas audio video. Anda akan ditanya apakah ingin menerapkan **Peredaman Audio** (menurunkan volume latar belakang selama deskripsi) agar narasi terdengar jelas.
- **AD Diperpanjang (Jeda Audio):** Mesin menjeda audio asli video selama narasi deskripsi agar dialog asli maupun narasi AI tetap terdengar lengkap. Deteksi jeda hening kini memakai model jaringan saraf **Silero VAD**, yang diunduh saat pertama kali digunakan seperti ffmpeg dan eSpeak. Model ini membedakan jeda alami dalam dialog dari musik dan suara latar untuk menentukan waktu jeda dengan lebih tepat.
- **Video YouTube:** Untuk sumber YouTube (yang tidak diunduh secara lokal), ekspor MP3 hanya akan berisi trek suara AI yang disinkronkan tanpa audio latar belakang video.

## 6. Transkripsi dan Sulih Suara Media (M)

Transkripsi Audio telah dibangun ulang sepenuhnya agar mendukung file audio dan video (MP3, WAV, MP4, MKV, dan lainnya). Tekan **M** di Lapisan Perintah untuk memilih file media dan salah satu dari 3 mode operasi berikut:

1. **Transkripsikan (Bahasa Asli):** Mentranskripsikan ucapan secara akurat dalam bahasa aslinya.
2. **Transkripsikan dan Terjemahkan (Bahasa Target):** Mentranskripsikan ucapan lalu menerjemahkannya ke bahasa target yang telah Anda atur.
3. **Sulihsuarakan dan Terjemahkan (Bahasa Target)** *(Khusus Gemini):* Mentranskripsikan ucapan, menerjemahkannya ke bahasa target, lalu membuat sulih suara dengan mesin TTS add-on.

## 7. Pembaca Dokumen & Gambar Lanjutan

**Pembaca Dokumen** mengubah dokumen menjadi teks yang mudah dibaca, diterjemahkan, dan didengarkan, mulai dari buku hasil pindai hingga kumpulan foto. Fitur ini mendukung PDF multihalaman, gambar kompleks, format HEIC iPhone, serta file teks biasa (`.txt`) dan HTML (`.html`, `.htm`) yang dapat langsung dibuka tanpa OCR atau AI. Jika Anda memilih beberapa file sekaligus, semuanya digabung menjadi satu dokumen sesuai urutan halaman. Tersedia tiga mesin OCR di Pengaturan > Pembaca Dokumen: **Chrome (Cepat)**, **AI (Lanjutan)** untuk mempertahankan tata letak dengan lebih baik, dan **Tanpa OCR (Ekstrak Lapisan Teks)** untuk PDF yang teksnya dapat dicari.

### Cara Kerja

1. Tekan **NVDA + Shift + V**, lalu **D** untuk membuka Pembaca Dokumen. Jika file sudah dipilih di File Explorer, gunakan **D** / **F** untuk langsung memprosesnya tanpa dialog pemilihan file.
2. Pilih satu atau beberapa PDF atau gambar. Add-on akan memeriksa file dan mengumumkan jumlah halamannya.
3. Dalam dialog **Opsi**, pilih rentang halaman (Dari/Sampai). Anda juga dapat mencentang **Terjemahkan Keluaran** dan memilih bahasa target, atau mengaktifkan **Deskripsikan gambar di dalam teks selama OCR**.
4. Ekstraksi teks berjalan secara bertahap di latar belakang. Anda dapat menutup jendela kapan saja dan melanjutkannya nanti tanpa kehilangan progres.
5. Setelah halaman siap, Anda dapat membacanya, berpindah atau langsung menuju halaman tertentu, bertanya kepada AI, menyimpan teks, atau membuat narasi audio.

### 7.1 Pemrosesan Batch & Melanjutkan Proses

Anda tidak perlu membaca dokumen panjang sekaligus. Pilih rentang halaman (misalnya `1-20`), atau biarkan pilihan bawaan untuk memproses semuanya. AI akan mengekstrak teks di latar belakang. Jika NVDA berhenti karena kesalahan atau pemindaian terhenti, add-on mengingat progres dan menawarkan untuk **Melanjutkan** dari posisi terakhir, bahkan setelah NVDA dimulai ulang. Dokumen yang telah selesai juga disimpan dalam cache. Membukanya kembali melalui Dokumen Terakhir atau **D** akan langsung memuat teks tanpa mengulangi OCR, kecuali file sumber berubah.

### 7.2 Tindakan File Cerdas

Di Windows File Explorer, pilih PDF, gambar, atau file teks/HTML, lalu tekan **D** (Pembaca Dokumen) dalam Lapisan Perintah. Untuk PDF atau gambar, Anda juga dapat memakai **F** (Tindakan File Cerdas). Add-on langsung memproses file yang dipilih tanpa membuka dialog pemilihan file. Beberapa file yang dipilih sekaligus diproses sebagai satu dokumen.

### 7.3 Kontrol & Pintasan Penampil Dokumen

Saat jendela Pembaca Dokumen terbuka, tersedia kontrol berikut.

#### Pintasan Keyboard

- **Ctrl + PageDown / Ctrl + PageUp:** Berpindah ke halaman berikutnya / sebelumnya.
- **Panah Down / Up:** Tekan **Down** saat kursor berada di baris terakhir untuk berpindah ke halaman berikutnya. Tekan **Up** di awal halaman untuk kembali ke halaman sebelumnya.
- **Alt + A:** Membuka obrolan untuk bertanya tentang dokumen.
- **Alt + R:** Menjalankan **Pindai ulang dengan AI** menggunakan penyedia aktif.
- **Alt + G:** Membuat dan menyimpan file audio berkualitas tinggi (WAV/MP3). *(Disembunyikan jika penyedia tidak mendukung TTS.)*
- **Alt + S / Ctrl + S:** Menyimpan teks hasil ekstraksi sebagai file TXT atau HTML.

#### Tombol & Kontrol

- **Ke halaman:** Memilih halaman yang ingin dibuka.
- **Lihat Berformat:** Menampilkan seluruh dokumen sebagai teks gabungan yang terformat.
- **Coba Ulang Halaman yang Gagal:** Mengulangi hanya kelompok halaman yang gagal diproses karena kesalahan server sementara, misalnya server sibuk. Tombol ini muncul saat diperlukan.
- **Suara TTS / Mesin TTS:** Memilih suara. Pada Gemini, Anda juga dapat memilih **TTS Standar** atau **Gemini Live**, yang menghasilkan suara secara streaming.
- **Sebelumnya / Berikutnya:** Berpindah halaman, sama seperti Ctrl+PageUp/Down.

### 7.4 Dokumen Terakhir (D)

Menekan **D** dalam Lapisan Perintah akan menampilkan dokumen yang terakhir Anda baca terlebih dahulu. Pilih dokumen untuk melanjutkan dari halaman terakhir, meskipun OCR sudah selesai. Untuk memilih file lain seperti biasa, tekan **Buka File...** (`Ctrl + O`).

## 8. Pelabelan AI Semantik & UI Explorer

Terjebak dalam aplikasi dengan banyak "tombol tanpa label"? Mesin Pelabelan AI Semantik menyelesaikannya secara permanen.

### 8.1 Pelabelan Objek Permanen (L)

Fokuskan pembaca layar Anda pada grafik atau tombol tanpa label dan tekan **L** di Lapisan Perintah. AI akan melihat tombol tersebut secara visual, menentukan fungsinya, dan menerapkan label permanen.
*Berbeda dengan alat pelabelan pembaca layar lama, add-on ini menggunakan sistem hibrida "Object Signature" (AutomationId/ControlID) yang canggih. Label kustom Anda akan tetap bertahan meskipun jendela diubah ukurannya, monitor dipindahkan, dan aplikasi diperbarui!*

### 8.2 Pemindaian Aplikasi Penuh (Shift + L)

Tekan **Shift + L** untuk memindai seluruh jendela aktif sekaligus. AI akan menemukan semua elemen tanpa label dan menamainya secara cerdas sekaligus. Anda nantinya dapat mengelola, mengganti nama, atau menghapus label ini secara massal dari Pengelola Label bawaan.

### 8.3 UI Explorer (E)

Perlu berinteraksi dengan suatu elemen tanpa mencarinya secara manual? Tekan **E** untuk mengaktifkan UI Explorer. AI akan memindai layar dan menghasilkan daftar yang aksesibel dari setiap elemen yang dapat diklik (mengabaikan gangguan sistem seperti taskbar). Pilih item dari daftar, dan add-on akan langsung mengkliknya untuk Anda.

## 9. Asisten Suara Langsung

Asisten Langsung mengubah Vision Assistant Pro menjadi kopilot interaktif real-time.
*(Catatan: Fitur ini eksklusif untuk Google Gemini dan penyedia Kustom yang kompatibel dengan Gemini).*

- **Aktivasi:** Tekan **Control + L** di Lapisan Perintah untuk membuka dialog Asisten Langsung.
- **Interaksi Real-time:** Bicaralah secara alami melalui mikrofon Anda. AI akan mendengarkan suara Anda dan melihat layar aktif Anda secara bersamaan. Anda dapat mengajukan pertanyaan seperti "Apa yang sedang saya lihat?" atau "Bacakan paragraf ketiga untuk saya."
- **Tekan untuk Bicara:** Aktifkan **Tekan untuk Bicara** di tab pengaturan Asisten Langsung atau langsung di jendela Asisten Langsung. Tahan tombol yang ditetapkan saat berbicara dan lepaskan setelah selesai. Mikrofon tidak mengirim suara sebelum tombol ditekan, sehingga berguna di lingkungan bising.
- **Masukan Kamera Web:** Centang **Gunakan Kamera Web** dalam jendela Asisten Langsung untuk mengirim gambar kamera ke AI sebagai pengganti layar. Anda dapat bertanya tentang benda, dokumen cetak, atau lingkungan sekitar. Jika ffmpeg belum terpasang, mencentang opsi ini akan mengunduhnya satu kali setelah Anda menyetujui. Opsi tidak tersedia jika kamera tidak terdeteksi atau akses kamera diblokir oleh pengaturan privasi Windows.
- **Kustomisasi:** Di dalam dialog, Anda dapat mengubah Gaya Suara AI (misalnya, Profesional, Ramah, Ceria) dan menyesuaikan "Kedalaman Berpikir" (Thinking Depth) untuk mengontrol seberapa mendalam analisisnya sebelum menjawab.

## 10. Prompt Kustom & Variabel

Anda dapat mengelola prompt di **Pengaturan > Prompt > Kelola Prompt...**.

### Pintasan Prompt Kustom

Tetapkan pintasan untuk setiap prompt kustom langsung di Pengelola Prompt. Prompt dapat langsung dijalankan menggunakan teks yang dipilih atau konteks saat ini:

- **Tombol tunggal** (misalnya `1`, `p`, atau `F3`): Berfungsi dalam Lapisan Perintah, dan secara global melalui `NVDA + Shift + tombol`.
- **Kombinasi tombol** (misalnya `Control + Shift + 1`, `Alt + P`, atau `Insert + 1`): Langsung berfungsi secara global.

### Variabel yang Didukung

- `[selection]`: Teks yang dipilih saat ini.
- `[clipboard]`: Konten papan klip.
- `[clipboard_image]`: Gambar di papan klip saat ini.
- `[screen_obj]`: Tangkapan layar dari objek navigator.
- `[screen_fg_obj]`: Tangkapan layar jendela aktif di latar depan.
- `[screen_full]`: Tangkapan layar seluruh layar.
- `[file_ocr]`: Pilih file gambar/PDF untuk ekstraksi teks.
- `[file_read]`: Pilih dokumen untuk dibaca (TXT, Kode, PDF).
- `[file_audio]`: Pilih file audio untuk analisis (MP3, WAV, OGG).
- `{target_lang}`: Bahasa target saat ini.
- `{source_lang}`: Bahasa sumber saat ini.
- `{response_lang}`: Bahasa respons AI saat ini.
- `{swap_target}`: Bahasa cadangan untuk terjemahan tukar cerdas.
- `{swap_instruction}`: Blok instruksi terjemahan tukar cerdas.

## 11. Kasus Penggunaan di Dunia Nyata (Fitur mana yang harus saya gunakan?)

Vision Assistant Pro dilengkapi dengan berbagai alat canggih. Berikut adalah beberapa skenario umum untuk membantu Anda memilih fitur yang tepat:

- **Skenario: Anda ingin memahami tata letak lengkap dari jendela yang rumit atau aplikasi yang tidak aksesibel.**
  *Solusi:* Tekan **O** (Visi Layar Penuh). AI akan menganalisis seluruh layar dan mendeskripsikan secara tepat di mana elemen, teks, dan tombol diposisikan.

- **Skenario: Anda menemukan gambar di halaman web atau grafik tanpa label di dokumen.**
  *Solusi:* Pindahkan objek navigator Anda ke grafik tersebut dan tekan **V** (Visi Objek). AI akan mendeskripsikan secara spesifik apa isi gambar tersebut.

- **Skenario: Anda ingin menonton film atau klip video dengan deskripsi audio.**
  *Solusi:* Tekan **Shift + V** pada video Anda dan pilih **"Buat Deskripsi Audio (File SRT)"**. Setelah selesai, klik **"Buat Narasi Tersinkron (MP3)"** dan pilih **"AD Diperpanjang"**. Add-on akan membuat trek audio yang menjeda dialog film secara cerdas untuk mendeskripsikan adegan visual.

- **Skenario: Anda menemukan aplikasi yang penuh dengan "tombol tanpa label".**
  *Solusi:* Tekan **L** untuk memberi label pada tombol tertentu menggunakan AI secara permanen. Atau, tekan **Shift + L** untuk memindai dan memberi label pada seluruh jendela sekaligus. Jika Anda hanya ingin mengklik sesuatu dengan cepat, tekan **E** (UI Explorer) untuk mendapatkan daftar semua item yang dapat diklik.

- **Skenario: Anda perlu melewati CAPTCHA yang tidak aksesibel.**
  *Solusi:* Tekan **C** (Pemecah CAPTCHA). AI akan secara otomatis menangkap CAPTCHA, memecahkannya, dan memasukkan jawabannya ke kolom yang benar.

- **Skenario: Anda ingin membaca dokumen PDF panjang sebanyak 50 halaman.**
  *Solusi:* Tekan **D** (Pembaca Dokumen), atur penyedia Anda ke Google Gemini, dan masukkan rentang halaman `1-50`. Add-on akan mengekstrak teks secara akurat di latar belakang.

- **Skenario: Anda sedang menonton tutorial video tanpa suara atau animasi di layar Anda.**
  *Solusi:* Tekan **Control + V** untuk mulai merekam layar. Biarkan tutorial berjalan, lalu tekan **Control + V** lagi. AI akan menjelaskan dengan tepat apa yang didemonstrasikan.

- **Skenario: Anda menemukan error tak terduga, kegagalan koneksi API, atau ingin mendiagnosis masalah pada server lokal kustom.**
  *Solusi:* Buka **Pengaturan > Lanjutan**, centang **"Aktifkan file log khusus"**, lalu atur **Tingkat Log** ke **"Debug"**. Ulangi tindakan yang bermasalah, kemudian pilih **"Buka File Log"** untuk memeriksa detail teknis atau melampirkan `vision_assistant.log` pada laporan dukungan.

***
**Catatan:** Koneksi internet aktif diperlukan untuk semua fitur AI. Dokumen multi-halaman diproses secara otomatis.

## 12. Dukungan & Komunitas

Ikuti perkembangan berita terbaru, fitur, dan rilis:

- **Saluran Telegram:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)
- **GitHub Issues:** Untuk laporan bug dan permintaan fitur.

### Melaporkan Bug & Log

Saat meminta dukungan, sertakan penyedia AI, model, dan versi NVDA. Untuk masalah koneksi atau crash, aktifkan file log khusus di **Pengaturan > Lanjutan**, ulangi masalahnya, lalu lampirkan `vision_assistant.log`.

## 13. Pendukung Proyek

Terima kasih sebesar-besarnya kepada anggota komunitas yang mendukung pengembangan dan pemeliharaan proyek ini melalui kontribusi finansial:

*   **@Alyabani94**
*   **Ali Alamri**
*   **Ilya**
*   **leonardo0216**
*   **Sergei Fleytin**
*   **Arne Siebert**
*   **Schalkefan**
*   **[avalai.org](https://avalai.org)**

*Jika Anda ingin mendukung proyek secara finansial dan ingin nama Anda ditampilkan di sini, buka opsi **Donasi** di menu Tools NVDA (submenu Vision Assistant) atau pada proses pengaturan setelah instalasi.*

---
## Perubahan untuk 2026.10.01

*   **Kamus Karakter & Pengelolaan Serial**: Dialog Analisis Video kini memiliki **Kamus Karakter**. Tambahkan, edit, impor, atau kelola nama, ciri fisik, dan peran karakter untuk setiap serial. AI mencocokkan karakter yang ditemukan dengan kamus Anda dan menambahkan karakter baru saat episode berikutnya dianalisis. Catatan yang Anda tulis sendiri selalu diutamakan dibanding pembaruan AI, sementara deskripsi fisik diperbarui sesuai episode. Kamus disimpan per serial dan digunakan kembali untuk setiap video dalam serial tersebut. Dalam daftar karakter, tekan **F2** untuk mengedit karakter yang dipilih atau **Delete** untuk menghapusnya.
*   **Cache File Video Selama 48 Jam**: Video yang diunggah ke Gemini kini disimpan dalam cache selama 48 jam. Anda dapat membuat ulang SRT atau MP3 untuk video yang sama tanpa mengunggah ulang, bahkan setelah memulai ulang NVDA. Cache terkait dengan kunci API dan otomatis tidak berlaku lagi jika kunci tersebut berubah.
*   **Deteksi Jeda Hening dengan AI (Silero VAD)**: AD Diperpanjang kini menggunakan model jaringan saraf Silero VAD untuk mendeteksi jeda hening dengan tepat. Model ini membedakan jeda alami dalam dialog dari musik dan suara latar. Seperti ffmpeg dan eSpeak, model diunduh saat pertama kali digunakan setelah Anda menyetujui.
*   **Pelacakan Kemunculan Pertama Karakter**: AI kini menjelaskan penampilan fisik setiap karakter hanya saat pertama kali muncul dalam video. Kemunculan berikutnya cukup menyebut nama, sehingga deskripsi tidak berulang di setiap segmen dan narasi tetap alami.
*   **Folder Data Terpadu**: Semua file data add-on (riwayat, serial, label, progres OCR, cache, dan log) dipindahkan ke satu folder `VisionAssistant` di folder konfigurasi NVDA. Data menjadi lebih tertata dan mudah dicadangkan secara manual.
*   **Penyimpanan Video yang Lebih Mudah**: Saat menyimpan SRT atau MP3, dialog penyimpanan kini otomatis membuka folder video sumber, baik video dibuka melalui dialog file maupun melalui Shift+V dari Explorer.
*   **Hapus Dokumen dengan atau tanpa Teks dalam Cache**: Dialog Riwayat (`Control + H`) kini menyediakan dua pilihan penghapusan dokumen. Tekan Delete, lalu pilih **Hapus dari riwayat saja** atau **Hapus dari riwayat beserta teks yang tersimpan dalam cache**. Pilihan kedua menghapus teks OCR yang tersimpan agar dokumen dipindai ulang dari awal saat dibuka kembali, misalnya setelah hasil pemindaian kurang baik. Centang **Jangan tanyakan lagi** untuk mengingat pilihan Anda pada penghapusan berikutnya. Data untuk melanjutkan proses yang terhenti tetap disimpan.
*   **Cache OCR Terpisah per Mesin dengan Penggabungan Halaman**: Teks OCR kini disimpan per mesin OCR. Saat Anda mengganti mesin, dokumen akan dipindai dengan mesin baru, bukan menampilkan hasil mesin sebelumnya. Membuka kembali dokumen akan menampilkan dialog rentang halaman dengan pilihan terakhir Anda. Halaman yang sudah dipindai langsung digunakan, sedangkan halaman yang belum tersedia akan dipindai. Cache digabung per halaman, bukan diganti seluruhnya, sehingga setiap rentang yang pernah dibaca tetap tersimpan.
*   **Kamera Web untuk Asisten Langsung**: Jendela Asisten Langsung kini memiliki kotak centang **Gunakan Kamera Web** untuk mengirim gambar kamera ke AI sebagai pengganti layar. Anda dapat bertanya tentang benda, dokumen, atau lingkungan sekitar. Jika ffmpeg belum terpasang, mencentang opsi ini akan mengunduhnya satu kali setelah Anda menyetujui. Opsi tidak tersedia jika kamera tidak terdeteksi atau aksesnya diblokir oleh pengaturan privasi Windows. Tersedia tombol untuk membuka pengaturan privasi kamera. Jika kamera diaktifkan tetapi tidak menghasilkan gambar, masalah dicatat dalam log NVDA untuk diperiksa, tanpa diam-diam beralih kembali ke layar.
*   **Perbaikan Bug & Peningkatan Stabilitas**: Memperbaiki proses pembuatan MP3 yang macet saat dialog progres ditutup di tengah proses, benturan akses bersamaan pada penyimpanan Kamus Karakter, pelaporan kesalahan pengodean MP3, serta proses tunggu Pembaca Dokumen agar mengikuti pembatalan oleh pengguna.

## Perubahan untuk 2026.09.01

*   **Riwayat (Control + H)**: Lapisan Perintah kini memiliki dialog **Riwayat** (`Control + H`) yang menampilkan obrolan dan dokumen sebelumnya, dengan filter Semua, Obrolan, dan Dokumen. Buka kembali obrolan beserta seluruh percakapannya; file lampiran akan dilampirkan kembali secara otomatis. Anda juga dapat membuka dokumen untuk melanjutkan membaca. Tekan **Delete** untuk menghapus item, atau hapus semuanya sekaligus.
*   **Dokumen Terakhir dalam Pembaca Dokumen**: Menekan **D** dalam Lapisan Perintah kini menampilkan dokumen yang terakhir dibaca terlebih dahulu. Pilih dokumen untuk melanjutkan dari halaman terakhir, meskipun OCR sudah selesai, atau tekan **Buka File...** (`Ctrl + O`) untuk memilih file seperti biasa.
*   **Tekan untuk Bicara pada Asisten Langsung**: Aktifkan **Tekan untuk Bicara** di tab pengaturan Asisten Langsung yang baru, lalu tetapkan tombol yang ingin digunakan. Anda bahkan dapat memilih satu tombol pengubah, seperti `Left Ctrl` (Ctrl kiri). Tahan tombol untuk berbicara dan lepaskan setelah selesai. Bunyi bip singkat menandai setiap penekanan dan pelepasan tombol. Opsi yang sama juga tersedia di jendela Asisten Langsung agar Anda dapat beralih antara mode Tekan untuk Bicara dan mikrofon terbuka tanpa meninggalkan percakapan.
*   **Audio Bawaan Gemini 2.5 Flash**: Asisten Langsung kini mendukung model audio bawaan Gemini 2.5 Flash (`gemini-2.5-flash-native-audio-preview-12-2025`) untuk percakapan suara yang alami dengan jeda respons singkat. Pilih model ini melalui **Pengaturan > Perutean Model Lanjutan > Model Asisten Langsung (khusus Gemini)**, atau biarkan pilihan "Otomatis" untuk memakai model yang disarankan.
*   **Pencadangan & Pemulihan Pengaturan**: Menambahkan sistem pencadangan dan pemulihan di tab **Lanjutan**. Simpan pengaturan add-on, termasuk kunci API, model, prompt kustom, dan preferensi, dalam satu file JSON. Pulihkan kapan saja, di komputer lain, atau setelah menginstal ulang NVDA. Saat mencadangkan, pilih **Semuanya** (pengaturan, label kustom, progres OCR, dan riwayat) atau **Pengaturan Saja**.
*   **Membaca Teks & HTML secara Langsung**: Pembaca Dokumen kini dapat langsung membuka file teks biasa (`.txt`) dan HTML (`.html`, `.htm`). Pengodean file dideteksi secara otomatis, skrip dan format yang tidak diperlukan dibuang, lalu isi dibagi menjadi halaman yang mudah dibaca. File hasil ekspor add-on juga dapat dibuka kembali dengan struktur halaman tetap terjaga. Semuanya dapat dibaca tanpa OCR atau pemrosesan AI.
*   **Gemini Live TTS untuk Pembaca Dokumen**: Tombol "Buat Audio" kini mendukung Gemini Live, mesin teks ke suara berkualitas tinggi yang menghasilkan audio secara streaming dengan tempo alami. Jika Gemini adalah penyedia aktif, Anda dapat memilih TTS Standar atau Gemini Live langsung dalam pembaca. Pilihan disimpan untuk penggunaan berikutnya.
*   **Pintasan Prompt Kustom**: Anda kini dapat menetapkan satu tombol atau kombinasi tombol untuk setiap prompt kustom langsung dari Pengelola Prompt. Jalankan prompt dengan cepat; teks yang dipilih atau konteks saat ini diambil secara otomatis tanpa langkah tambahan.
*   **Navigasi Pesan Obrolan**: Di jendela obrolan apa pun, termasuk Obrolan Langsung, obrolan dokumen, dan penyempurnaan teks, tekan `Alt + Down` untuk mendengar pesan berikutnya atau `Alt + Up` untuk pesan sebelumnya. Awalan "Anda" / "AI" serta penanda "Pesan pertama" / "Pesan terakhir" dibacakan agar posisi Anda jelas.
*   **Salin Pesan Obrolan (Alt + C)**: Saat meninjau percakapan dengan `Alt + Up/Down`, tekan `Alt + C` untuk menyalin pesan saat ini ke papan klip. Penyalinan mengikuti pengaturan Bersihkan Markdown dan disertai konfirmasi suara.
*   **Prompt Sistem Obrolan Langsung**: Obrolan Langsung (`Shift+C`) kini memiliki prompt sistem yang dapat diedit, yaitu "Instruksi Obrolan Langsung". Prompt ini mengatur karakter asisten dan bahasa respons untuk setiap percakapan. Anda dapat menyesuaikannya di tab Prompt Bawaan dalam Pengelola Prompt.
*   **Navigasi Halaman dengan Kursor di Pembaca Dokumen**: Di Penampil Dokumen, tekan `Down` saat kursor berada di baris terakhir untuk langsung menuju halaman berikutnya. Tekan `Up` di awal halaman untuk kembali ke halaman sebelumnya, sehingga Anda tidak perlu berpindah halaman secara manual saat membaca.
*   **Pilihan Baru dalam Pengaturan Cepat**: Salin respons AI ke papan klip, Keluaran Langsung (tanpa jendela obrolan), Bersihkan Markdown dalam Obrolan, dan Pertukaran Cerdas kini dapat langsung diaktifkan atau dinonaktifkan melalui Pengaturan Cepat di Lapisan Perintah.
*   **Tab Pengaturan Asisten Langsung**: Asisten Langsung kini memiliki tab pengaturan tersendiri. Opsi "Asisten Langsung: Keluaran Langsung (Tanpa Jendela)" dipindahkan dari tab Koneksi ke tab ini. Tab hanya muncul jika penyedia aktif adalah Google Gemini atau penyedia Kustom yang kompatibel dengan Gemini.

## Perubahan untuk 2026.08.06

*   **Pelabelan di UI Explorer**: Kini Anda dapat menambahkan label langsung ke elemen yang ditemukan di UI Explorer. Tombol baru "Tambahkan Label" telah tersedia. Antarmuka tetap terbuka dan mempertahankan fokus, sehingga Anda dapat memberi label pada beberapa objek dengan cepat tanpa gangguan.
*   **Peningkatan Lapisan Pengaturan Cepat**: Lapisan Vision Assistant (`Insert+Shift+V`) kini tetap aktif dan sangat interaktif. Gunakan panah `Up/Down` untuk berpindah di antara Pengaturan Cepat (Penyedia, Model, Bahasa Respons AI, Model TTS), dan panah `Left/Right` untuk langsung mengubah nilainya dengan umpan balik suara yang ringkas dan cerdas. Pilihan langsung diterapkan, termasuk mengaktifkan Perutean Model Lanjutan secara otomatis bila diperlukan, dan lapisan tetap aktif selama Anda melakukan konfigurasi.
*   **Obrolan Langsung (`Shift+C`)**: Menambahkan perintah baru ke lapisan. Tekan `Shift+C` untuk langsung membuka jendela "Obrolan Langsung". Antarmuka percakapan berbasis teks yang bersih ini memungkinkan Anda langsung mengobrol dengan AI tanpa harus memulai dari gambar atau dokumen.
*   **Pemanggilan Riwayat Obrolan yang Andal**: Memperbaiki bug besar yang membuat riwayat obrolan lanjutan hilang ketika `Space` ditekan untuk membuka hasil terakhir. Kini add-on melacak percakapan secara global. Jika Anda mengobrol, menutup dialog, lalu menekan `Space`, seluruh riwayat percakapan dua arah akan dipulihkan dengan sempurna. Fitur ini berlaku untuk Obrolan Langsung, Analisis Visi, Obrolan Dokumen, dan Terjemahan.
*   **Deskripsi Gambar dalam Teks OCR**: Menambahkan fitur opsional untuk mendeskripsikan gambar di antara teks selama OCR dokumen. Anda dapat mengubah pengaturan ini di pengaturan OCR add-on, di opsi Pembaca Dokumen sebelum ekstraksi, atau secara cepat melalui lapisan Pengaturan Cepat.
*   **Terjemahan Suara (`Control+T`)**: Menambahkan fitur baru yang canggih. Diktekan ucapan untuk langsung menerjemahkan dan mengetik hasilnya dengan AI berdasarkan bahasa sumber dan target yang telah Anda atur.
*   **Peningkatan Pengunduh Pembaruan**: Dialog pengunduhan pembaruan kini menampilkan progres dalam persentase dengan benar. Bug yang memunculkan pesan semu "Mengunduh pembaruan" setelah instalasi dibatalkan juga telah diperbaiki.
*   **Peningkatan Pengunduh eSpeak-NG**: Menambahkan pelacakan progres dalam persentase untuk unduhan eSpeak-NG.
*   **Ketahanan OCR Batch**: Memperbaiki masalah pada OCR PDF batch yang menghentikan proses jika kuota kunci API aktif habis di tengah jalan. Kini add-on otomatis beralih ke kunci berikutnya yang tersedia dan melanjutkan proses.
*   **Dukungan CAPTCHA Visual**: Menambahkan dukungan yang andal untuk memecahkan CAPTCHA visual. Add-on mencoba memecahkan tantangan gambar kompleks seperti hCaptcha dan reCAPTCHA secara otomatis, sehingga formulir web yang sulit menjadi jauh lebih aksesibel.
*   **Perombakan Transkripsi Audio**: Modul Transkripsi Audio telah dibangun ulang sepenuhnya dan kini mendukung file audio maupun video. Tersedia 3 mode operasi: "Transkripsikan (Bahasa Asli)", "Transkripsikan dan Terjemahkan (Bahasa Target)", serta opsi baru "Sulihsuarakan dan Terjemahkan (Bahasa Target)" khusus Gemini yang membuat sulih suara terjemahan dari ucapan asli.
*   **Nomor Halaman Opsional di Pembaca Dokumen**: Menambahkan pengaturan untuk mengaktifkan atau menonaktifkan nomor dan pemisah halaman pada keluaran dokumen multihalaman. Opsi ini dapat dikelola dari pengaturan utama atau diubah langsung melalui lapisan Pengaturan Cepat. Fitur berlaku untuk ekspor file teks/HTML dan jendela "Lihat Berformat", sehingga dokumen gabungan dapat dibaca dengan lancar.
*   **Gemini Live TTS Tanpa Batas untuk Deskripsi Video**: Kini Anda dapat memilih "Gemini Live TTS" sebagai mesin suara saat membuat Narasi Audio Tersinkron (MP3) untuk video. Gemini Live API menghasilkan Deskripsi Audio berkualitas tinggi tanpa batas karakter atau durasi.
*   **Modularisasi Basis Kode**: Struktur add-on dirombak dari satu file menjadi arsitektur modular dengan beberapa file agar lebih mudah dipelihara.
*   **Desain Ulang Antarmuka Pengaturan**: Dialog Pengaturan didesain ulang sepenuhnya dengan antarmuka modern berbasis tab, menggantikan tata letak berkelompok. Susunan baru lebih teratur dan mudah dinavigasi tanpa menghilangkan opsi yang sudah ada.
*   **Pencatatan Global & File Khusus**: Menambahkan sistem pencatatan global opsional di tab pengaturan "Lanjutan" yang baru. Sistem ini otomatis mencatat peristiwa operasional, lalu lintas API, dan error dari seluruh modul add-on ke file khusus (`vision_assistant.log`). Tersedia tingkat perincian log yang dapat diatur (Debug, Info, Peringatan, Error), masa penyimpanan otomatis (1 jam hingga 90 hari), serta kontrol untuk membuka atau membersihkan log langsung dari pengaturan tanpa memengaruhi performa atau log NVDA.
*   **Pelacakan Progres Unggahan Gemini**: Menambahkan pengumuman progres persentase secara real-time saat mengunggah file besar (video, audio, dokumen) ke Google Gemini API.

## Perubahan untuk 2026.07.15

*   **Penyaringan Model API Cerdas**: Perombakan total sistem penyaringan model untuk menggunakan pendekatan blacklist murni alih-alih whitelist. Menambahkan kata kunci penyaringan yang lebih kuat (`embedding`, `bison`, `gecko`, `audio`, `realtime`, `babbage`, `moderation`, `deep`, `antigravity`, `computer`) untuk memastikan menu dropdown model obrolan utama tetap bersih dan tahan masa depan, sementara tetap menjaga semua model khusus dapat diakses di bagian Perutean Lanjutan.
*   **Pencarian Perutean Lanjutan**: Semua dropdown Perutean Model Lanjutan (OCR, STT, TTS, Operator, Video, Live) dan pemilih Varian eSpeak sekarang sepenuhnya dapat dicari. Anda dapat mengetik dengan cepat untuk menyaring dan menemukan model atau varian yang Anda inginkan.
*   **Pintasan Lapisan Perintah Baru**:
    *   **Pengaturan (`Alt + S`)**: Membuka dialog pengaturan Vision Assistant Pro secara instan.
    *   **Laporan Kunci Kuota Habis (`Alt + Q`)**: Melaporkan jumlah persis kunci API Gemini yang telah melebihi kuota harian mereka, mengidentifikasi model spesifik mana yang kuotanya habis, dan mengumumkan waktu reset persisnya.
    *   **Audit Perutean (`Alt + M`)**: Mengaudit dan mengumumkan konfigurasi Perutean Lanjutan Anda saat ini, membacakan model mana yang aktif dipilih untuk tugas-tugas khusus (melewati pengaturan default).
*   **Perombakan Total Penganalisis Video**: Penganalisis Video telah diubah sepenuhnya! Sebelumnya, fitur ini hanya menyediakan deskripsi dasar untuk video online. Sekarang, fitur ini adalah paket pemrosesan video komprehensif yang dirancang untuk pengguna tunanetra:
    *   **Perekaman Layar Lokal (`Control+V`)**: Anda sekarang dapat merekam video tanpa suara langsung dari layar Anda. AI akan menganalisis segmen yang direkam dan memberikan deskripsi yang sangat rinci tentang pemandangan, tata letak, dan tindakan.
    *   **Pembuatan Deskripsi Audio (SRT)**: Add-on sekarang dapat menghasilkan skrip Deskripsi Audio yang sangat mendetail (dalam format SRT standar) untuk video, lengkap dengan waktu jeda cerdas untuk menambatkan deskripsi secara cerdas ke jeda alami di trek audio, dan OCR verbatim untuk teks apa pun yang ada di layar.
    *   **Narasi Audio Tersinkron (MP3)**: Selain subtitel berbasis teks, add-on dapat mengubah Deskripsi Audio menjadi ucapan, mencampurnya secara otomatis dengan trek audio asli video, menerapkan Peredaman Audio, dan mengekspor hasil akhir yang tersinkron sebagai file MP3.
    *   **Aksi File Video Cerdas**: Jika Anda memfokuskan pada file video lokal dan menekan pintasan video, add-on akan secara otomatis mendeteksinya dan memproses file tersebut secara langsung.
    *   **Pelacakan Karakter Lanjutan**: AI sekarang melakukan ekstraksi karakter tahap pertama. Ini membangun kamus karakter global dan melacak karakter secara akurat segmen demi segmen tanpa membingungkan identitas.
    *   **Konfigurasi Analisis Video**: Menambahkan pengaturan baru untuk mengontrol ukuran potongan SRT, subtitel karakter, dan penafian.
    *   **Perutean Model Diperluas**: Anda sekarang dapat memilih model video khusus (`gemini_video_model`, `custom_video_model`) secara eksplisit di pengaturan Perutean Model Lanjutan.
*   **Manajemen Kuota API Cerdas**: Penanganan kesalahan 429 (Batas Harian) yang ditingkatkan dengan melacak kuota per model. Jika sebuah kunci mencapai batas hariannya pada satu model, ia akan dikarantina secara cerdas hanya untuk model tersebut, membiarkan kunci tersebut tetap tersedia untuk digunakan dengan model lainnya.

## Perubahan untuk 7.0.0

*   **Melanjutkan Pemindaian yang Belum Selesai**: Menambahkan fitur lanjutkan untuk Pembaca Dokumen dan Tindakan File Cerdas. Jika pemindaian terputus, sekarang Anda dapat melanjutkan dari titik terakhir alih-alih memulai lagi dari awal.
*   **Variabel `[screen_fg_obj]` Baru**: Menambahkan variabel prompt kustom untuk mengambil tangkapan layar hanya dari jendela aktif di latar depan, bukan seluruh layar.
*   **Coba Ulang Cerdas & Rotasi Kunci**: Add-on kini diam-diam mencoba ulang hingga 5 kali pada kunci yang sama saat terjadi beban server sementara, seperti "permintaan tinggi" atau respons tidak valid. Jika percobaan ulang gagal, add-on otomatis beralih ke kunci API berikutnya dalam daftar Anda.
*   **Deteksi Screen Curtain**: Menambahkan pemeriksaan untuk mencegah pengambilan tangkapan layar saat Screen Curtain aktif, baik aktif permanen maupun dinyalakan sementara dengan hotkey. Add-on akan memperingatkan Anda dan berhenti, sehingga Anda tidak mengirim gambar hitam dan membuang token API.
*   **Penyempurnaan Pembaca Dokumen**: Dialog rentang PDF kini otomatis memilih bahasa target default dari pengaturan add-on. Penanganan thread juga ditingkatkan agar tugas latar belakang berhenti dengan bersih saat pembaca ditutup.
*   **Integrasi OCR Mistral Bawaan**: Mengintegrasikan API Document OCR bawaan Mistral. Dokumen multi-halaman otomatis digabung, diunggah, dan diproses secara batch memakai endpoint khusus `/v1/ocr` milik Mistral, sedangkan gambar satu halaman diproses langsung tanpa konversi PDF yang tidak perlu [1].
*   **Penangan URL Kustom Dinamis**: Mengubah URL API Kustom kini langsung menghapus cache daftar model dan mengembalikan kotak teks entri model manual. Ini memastikan kompatibilitas penuh dengan endpoint kustom, seperti Cloudflare AI Gateway, yang tidak mendukung endpoint daftar `/v1/models` standar.
*   **Mesin Input Operator AI Dirombak**: Sistem simulasi mouse dan keyboard dasar untuk Operator AI ditulis ulang sepenuhnya. API lama `mouse_event` diganti dengan API Windows modern `SendInput`, sehingga kompatibilitas dengan aplikasi modern, jendela yang dilindungi UAC, dan tampilan high-DPI jauh lebih baik.
*   **Operasi Seret & Lepas Diperbaiki**: Aksi seret dan lepas di Operator AI kini jauh lebih stabil dan andal. Mesin baru memakai kurva "easing" yang natural, posisi kursor presisi, timing yang dioptimalkan, dan teknik "nudge" cerdas agar Windows dan aplikasi mengenali serta menjalankan gestur seret-dan-lepas dengan benar tanpa gagal di tengah jalan.
*   **Dukungan Multi-Monitor**: Operator AI kini mendukung penuh setup multi-monitor. Gerakan dan klik mouse bekerja benar di semua monitor memakai flag `MOUSEEVENTF_VIRTUALDESK`, sehingga posisi tetap akurat di monitor mana pun aplikasi target berada.
*   **Simulasi Keyboard Ditingkatkan**: Injeksi tombol ditingkatkan agar mendukung penuh "Extended Keys", seperti tombol panah, Home, End, Page Up/Down, Insert, Delete, dan F1-F12. Ini memastikan navigasi dan perintah pintasan yang dikirim Operator AI berjalan lancar di semua aplikasi.
*   **Dukungan Gambar HEIC/HEIF**: Menambahkan dukungan bawaan untuk format foto iPhone. Sekarang Anda dapat langsung memilih file `.heic` dan `.heif` untuk deskripsi AI, OCR, atau Pembacaan Dokumen tanpa konversi lebih dulu.

## Perubahan untuk 6.5.0

*   **Asisten Langsung**: Menambahkan fitur asisten suara dan layar secara real-time, tersedia secara eksklusif untuk penyedia Google Gemini (atau penyedia kustom yang kompatibel dengan Gemini). Termasuk kustomisasi suara interaktif dan kedalaman berpikir langsung di dalam dialog, dengan rekoneksi otomatis setelah mengubah pengaturan.
*   **Penyedia AI MiniMax**: Mengintegrasikan MiniMax sebagai penyedia setara dengan dukungan multimodal penuh (obrolan, visi, OCR), TTS kustom menggunakan lebih dari 300+ suara dinamis, dan penghapusan blok penalaran secara otomatis (misalnya, `<think>...</think>`) dari keluaran.
*   **Terjemahan Penampil Dokumen**: Memperbaiki kegagalan terjemahan diam-diam untuk pengguna NVDA non-Inggris dengan memastikan kode bahasa 2 huruf standar dikirim ke Google Translate alih-alih nama bahasa yang dilokalkan.
*   **Coba Lagi Pemindaian Batch PDF**: Mengimplementasikan logika coba lagi yang sangat dioptimalkan, terpisah, dan diam-diam untuk pemindaian batch dokumen PDF guna mencegah pengunggahan berulang dan menghindari popup kesalahan yang mengganggu selama proses coba lagi.
*   **Status Penampil Dokumen**: Memperbaiki bug di mana status keseluruhan plugin (diperiksa melalui `I`) tetap macet di "Pemrosesan Batch Dimulai" selama pemindaian dokumen yang panjang.
*   **Perbaikan Crash Threading**: Memperbaiki crash pernyataan thread `IsMain() failed in wxTimerImpl` yang parah saat membuka dokumen dari thread latar belakang dengan memindahkan antrean callback GUI ke `wx.CallAfter`.

## Perubahan untuk 6.1.2

*   **Pemeriksaan Awal Label Duplikat**: Memperbaiki masalah pada pelabelan tunggal ketika pemeriksaan duplikat masih memakai kunci koordinat lama, sehingga NVDA membuat permintaan AI ganda untuk objek yang sudah diberi label alih-alih mengumumkan label yang ada.
*   **Obrolan Dokumen untuk Penyedia Non-Gemini**: Memperbaiki pemeriksaan kunci API yang terlalu ketat di Obrolan Dokumen (`on_ask`) agar pengguna OpenAI, Groq, atau penyedia Kustom lokal seperti Ollama dapat mengobrol dengan dokumen tanpa diblokir.
*   **Terjemahan OCR Chrome Cepat**: Mengembalikan API terjemahan gratis tanpa kunci untuk OCR Chrome. Terjemahan teks hasil ekstraksi kini melewati AI Gemini, sehingga kuota API lebih hemat dan proses terjemahan lebih cepat.
*   **Filter Alfanumerik CAPTCHA**: Memperbaiki logika filter di pemecah CAPTCHA agar karakter non-alfanumerik dibersihkan dengan benar dalam semua situasi.
*   **Pembaruan Bantuan Lapisan Perintah**: Memperbaiki pintasan pengumuman status di menu bantuan dari `L` menjadi `I`, dan menambahkan kedua perintah pelabelan (`L` dan `Shift+L`) ke daftar.

## Perubahan untuk 6.1.1

*   **Perbaikan Output Thinking Gemma 4**: Memperbaiki masalah pada model Gemma 4 ketika seluruh proses berpikir internal ditampilkan sebagai respons akhir, atau ketika menonaktifkan thinking menghasilkan respons kosong. Add-on kini memisahkan dan mengambil hanya teks akhir yang bersih.
*   **OCR Batch dari File Explorer**: Anda kini dapat memilih beberapa foto atau PDF langsung di Windows File Explorer dan mengekstrak teks atau menganalisisnya secara batch. Add-on akan otomatis memfilter dan memproses hanya format file yang didukung.

## Perubahan untuk 6.1.0

*   **Integrasi AI Lokal Universal (Siapkan AI Lokal)**: Menambahkan tombol **"Siapkan AI Lokal"** baru di Pengaturan Penyedia Kustom. Pengguna kini dapat mengonfigurasi mesin AI lokal seperti **Ollama**, **LM Studio**, **Jan.ai**, dan **KoboldCPP** secara otomatis dan instan.
*   **Bypass Proksi Lokal Cerdas**: Logika koneksi dibangun ulang dengan mekanisme bypass proksi lanjutan. Add-on kini dapat melewati proksi sistem Windows sepenuhnya untuk koneksi loopback lokal, sehingga koneksi AI lokal tetap stabil meskipun VPN atau mode TUN sedang aktif.
*   **Pelabelan AI Sangat Stabil (v2)**: Kunci berbasis koordinat layar absolut diganti dengan sistem **Object Signature** hibrida yang lebih canggih. Label kini mengandalkan pengenal programatik seperti UIA **AutomationId** atau Win32 **ControlID**, serta koordinat relatif jendela, sehingga label kustom tahan terhadap perubahan ukuran atau posisi jendela, perpindahan monitor, dan scaling.
*   **Migrasi Label Otomatis yang Mulus**: Proses upgrade berjalan transparan. Add-on akan memigrasikan label lama berbasis koordinat ke format sidik jari baru yang stabil di latar belakang saat fokus pertama kali, tanpa kehilangan data.

## Perubahan untuk 6.0

*   **Memperkenalkan Pelabelan AI Semantik**: Pengguna kini dapat memberi label permanen pada tombol dan ikon tanpa nama menggunakan AI. Tekan **L** untuk memberi label pada objek navigator saat ini (mendukung fokus Tab dan navigasi objek), atau **Shift+L** untuk memindai dan memberi label seluruh aplikasi sekaligus.
*   **Pengelolaan Label Cerdas**: Menambahkan dialog Pengelola Label baru yang sepenuhnya aksesibel (melalui **Shift+L** jika label sudah ada) untuk melihat, mengganti nama, atau menghapus banyak label kustom sekaligus.
*   **Analisis File Langsung (Tanpa Dialog File)**: Add-on kini dapat mendeteksi saat fokus berada pada file PDF atau gambar di Windows File Explorer. Menekan **F (Tindakan File Cerdas)** atau **D (Pembaca Dokumen)** pada file yang disorot akan langsung memprosesnya, tanpa membuka dialog "Buka" standar.

## Perubahan untuk 5.6

*   **Menambahkan Mesin OCR "Tanpa OCR (Ekstrak Lapisan Teks)"**: Pengguna kini dapat mengambil teks langsung dari PDF yang sudah memiliki lapisan teks tanpa memakai kredit AI. Ini membuat proses lebih cepat dan lebih privat untuk dokumen berbasis teks.
*   **Akurasi UI Explorer Ditingkatkan**: Prompt UI Explorer diperbaiki agar lebih tepat mengenali jenis elemen, seperti item daftar, dan melaporkan status seperti "(Dicentang)", "(Dipilih)", atau "(Diperluas)", sambil mengabaikan komponen sistem Windows seperti Taskbar dan Jam.
*   **Pengingat Pengaturan Setelah Instalasi**: Menambahkan notifikasi setelah instalasi untuk mengarahkan pengguna ke menu pengaturan agar dapat mengonfigurasi kunci API dan preferensi.

## Perubahan untuk 5.5.2

*   **Masalah Pengetikan Operator AI Diperbaiki:** Memperbaiki bug yang membuat huruf 'v' diketik alih-alih menempelkan teks pada sistem tertentu. Perbaikan ini mengatasi konflik timing yang muncul saat beban sistem tinggi.
*   **Stabilitas Ditingkatkan:** Menambahkan penanganan error yang lebih kuat untuk operasi papan klip agar add-on tidak crash saat papan klip sistem sedang dikunci sementara oleh aplikasi lain.
*   **Optimasi Timing:** Menyesuaikan jeda internal untuk event keyboard agar lebih andal di berbagai kecepatan sistem dan lebih kompatibel dengan Clipboard Manager pihak ketiga.

## Perubahan untuk 5.5 (Pembaruan Otomasi)

*   **Operator AI (Kontrol Mandiri - Shift+A):** Ini adalah fitur utama di v5.5. Vision Assistant Pro berkembang dari asisten pasif menjadi **Operator AI** pribadi Anda. Add-on ini tidak hanya mendeskripsikan layar, tetapi juga dapat mengambil tindakan.
    *   *Cara kerja:* Anda kini dapat memberi instruksi lisan atau tertulis untuk mengoperasikan PC. Misalnya, di aplikasi yang sama sekali tidak aksesibel dan pembaca layar tidak memberi informasi, tekan **Shift+A** lalu ketik: *"Klik tombol Pengaturan"* atau *"Cari kolom pencarian, ketik 'Berita Terbaru', lalu tekan enter."* AI akan mengenali elemen secara visual, menggerakkan mouse, dan menjalankan tugas tersebut.
    *   *Catatan performa:* Fitur ini dioptimalkan untuk **Gemini 3.0 Flash (Preview)** sehingga responsnya sangat cepat dan cerdas, bahkan untuk tata letak antarmuka yang rumit.
    *   **Peringatan penggunaan API:** Agar Operator AI bisa bekerja akurat, ia perlu "melihat" kondisi layar dan mengirim tangkapan layar resolusi tinggi pada setiap langkah. Penggunaan yang sering akan menghabiskan kuota API jauh lebih cepat daripada tugas berbasis teks biasa.
*   **Visual UI Explorer (E):** Lelah menghadapi "tombol tanpa label"? Tekan **E** untuk mengaktifkan UI Explorer. AI akan memindai seluruh jendela dan membuat daftar semua elemen yang bisa diklik, termasuk ikon, grafik, dan menu. Pilih item dari daftar, lalu Operator AI akan mengkliknya untuk Anda. Anggap saja seperti lapisan aksesibilitas tambahan di atas aplikasi apa pun.
*   **Tindakan File Cerdas Berbasis Konteks (F):** Tombol **F** dirombak total. Fitur ini tidak lagi menganggap Anda selalu ingin OCR. Saat Anda memilih satu gambar, add-on akan menanyakan tujuan Anda: pilih **Deskripsi Visual Terperinci** untuk memahami isi gambar, atau **Ekstraksi Teks Terstruktur (OCR)** untuk membaca teks. Menu akan menyesuaikan secara dinamis berdasarkan jenis file dan mesin AI yang aktif.
*   **Optimasi Inti:** Logika internal add-on dibersihkan secara menyeluruh dengan menghapus fungsi lama yang tidak dipakai dan kode yang berulang. Hasilnya adalah pengalaman yang lebih ringan, cepat, dan andal untuk semua pengguna.

## Perubahan untuk 5.0

* **Arsitektur Multi-Penyedia**: Menambahkan dukungan penuh untuk **OpenAI**, **Groq**, dan **Mistral** selain Google Gemini. Pengguna kini dapat memilih backend AI yang diinginkan.
* **Perutean Model Lanjutan**: Pengguna penyedia bawaan seperti Gemini dan OpenAI kini dapat memilih model tertentu dari daftar dropdown untuk berbagai tugas, seperti OCR, STT, dan TTS.
* **Konfigurasi Titik Akhir Lanjutan**: Pengguna penyedia kustom dapat memasukkan URL dan nama model tertentu secara manual untuk kontrol lebih rinci atas server lokal atau layanan pihak ketiga.
* **Visibilitas Fitur Cerdas**: Menu pengaturan dan antarmuka Pembaca Dokumen kini otomatis menyembunyikan fitur yang tidak didukung, seperti TTS, berdasarkan penyedia yang dipilih.
* **Pengambilan Model Dinamis**: Add-on kini mengambil daftar model yang tersedia langsung dari API penyedia, sehingga tetap kompatibel dengan model baru segera setelah dirilis.
* **OCR & Terjemahan Hybrid**: Logika dioptimalkan agar memakai Google Translate untuk kecepatan saat menggunakan Chrome OCR, dan terjemahan berbasis AI saat memakai mesin Gemini, Groq, atau OpenAI.
* **"Pindai ulang dengan AI" Universal**: Fitur pindai ulang di Pembaca Dokumen tidak lagi terbatas pada Gemini. Fitur ini memakai penyedia AI apa pun yang sedang aktif untuk memproses ulang halaman.

## Perubahan untuk 4.6

* **Pembukaan Ulang Hasil Interaktif:** Menambahkan tombol **Space** pada Lapisan Perintah, sehingga pengguna bisa langsung membuka kembali respons AI terakhir di jendela obrolan untuk pertanyaan lanjutan, bahkan saat mode "Keluaran Langsung" aktif.
* **Pusat Komunitas Telegram:** Menambahkan tautan "Kanal Telegram Resmi" di menu Tools NVDA, agar pengguna lebih cepat mengikuti kabar, fitur, dan rilis terbaru.
* **Stabilitas Respons Ditingkatkan:** Mengoptimalkan logika inti fitur Terjemahan, OCR, dan Visi agar performa lebih andal dan pengalaman output suara langsung lebih mulus.
* **Panduan Antarmuka Ditingkatkan:** Deskripsi pengaturan dan dokumentasi diperbarui agar sistem pembukaan ulang hasil terakhir lebih mudah dipahami, termasuk cara kerjanya bersama pengaturan output langsung.

## Perubahan untuk 4.5

* **Pengelola Prompt Lanjutan:** Menambahkan dialog khusus di pengaturan untuk menyesuaikan prompt sistem bawaan dan mengelola prompt buatan pengguna, termasuk tambah, edit, urut ulang, dan pratinjau.
* **Dukungan Proksi Menyeluruh:** Memperbaiki masalah koneksi dengan memastikan proksi yang diatur pengguna diterapkan secara ketat ke semua permintaan API, termasuk terjemahan, OCR, dan pembuatan suara.
* **Migrasi Data Otomatis:** Menambahkan sistem migrasi cerdas untuk memperbarui konfigurasi prompt lama ke format JSON v2 yang lebih kuat saat pertama kali dijalankan, tanpa kehilangan data.
* **Kompatibilitas Diperbarui (2025.1):** Menetapkan NVDA versi minimum 2025.1 karena ketergantungan pustaka pada fitur lanjutan seperti Pembaca Dokumen.
* **Antarmuka Pengaturan Dioptimalkan:** Pengaturan dibuat lebih rapi dengan memindahkan manajemen prompt ke dialog terpisah, sehingga pengalaman pengguna lebih bersih dan aksesibel.
* **Panduan Variabel Prompt:** Menambahkan panduan bawaan di dialog prompt agar pengguna mudah mengenali dan memakai variabel dinamis seperti [selection], [clipboard], dan [screen_obj].

## Perubahan untuk 4.0.3

*   **Ketahanan Jaringan Ditingkatkan:** Menambahkan mekanisme coba ulang otomatis untuk menangani koneksi internet tidak stabil dan error server sementara, sehingga respons AI lebih andal.
*   **Dialog Terjemahan Visual:** Menambahkan jendela khusus untuk hasil terjemahan. Pengguna dapat menelusuri dan membaca terjemahan panjang baris demi baris, mirip hasil OCR.
*   **Tampilan Berformat Gabungan:** Fitur "Lihat Berformat" di Pembaca Dokumen kini menampilkan semua halaman yang diproses dalam satu jendela terstruktur dengan header halaman yang jelas.
*   **Alur OCR Dioptimalkan:** Pemilihan rentang halaman otomatis dilewati untuk dokumen satu halaman, sehingga proses pengenalan lebih cepat dan mulus.
*   **Stabilitas API Ditingkatkan:** Beralih ke metode autentikasi berbasis header yang lebih kuat untuk mengatasi potensi error "All API Keys failed" akibat konflik rotasi kunci.
*   **Perbaikan Bug:** Memperbaiki beberapa potensi crash, termasuk masalah saat add-on dihentikan dan error fokus di dialog obrolan.

## Perubahan untuk 4.0.1

*   **Pembaca Dokumen Lanjutan:** Penampil baru yang kuat untuk PDF dan gambar, dengan pilihan rentang halaman, pemrosesan latar belakang, dan navigasi `Ctrl+PageUp/Down` yang mulus.
*   **Submenu Tools Baru:** Menambahkan submenu khusus "Vision Assistant" di menu Tools NVDA untuk akses cepat ke fitur utama, pengaturan, dan dokumentasi.
*   **Kustomisasi Fleksibel:** Anda kini dapat memilih mesin OCR dan suara TTS langsung dari panel pengaturan.
*   **Dukungan Multi Kunci API:** Menambahkan dukungan beberapa kunci API Gemini. Anda dapat memasukkan satu kunci per baris atau memisahkannya dengan koma di pengaturan.
*   **Mesin OCR Alternatif:** Menambahkan mesin OCR baru agar pengenalan teks tetap andal saat kuota Gemini API habis.
*   **Rotasi Kunci API Cerdas:** Add-on otomatis beralih ke kunci API yang berfungsi paling cepat dan mengingatnya untuk melewati batas kuota.
*   **Dokumen ke MP3/WAV:** Menambahkan kemampuan membuat dan menyimpan file audio berkualitas tinggi dalam format MP3 (128kbps) dan WAV langsung dari pembaca.
*   **Dukungan Instagram Stories:** Menambahkan kemampuan untuk mendeskripsikan dan menganalisis Instagram Stories melalui URL.
*   **Dukungan TikTok:** Menambahkan dukungan video TikTok untuk deskripsi visual lengkap dan transkripsi audio klip.
*   **Dialog Pembaruan Didesain Ulang:** Menghadirkan antarmuka baru yang aksesibel dengan kotak teks yang dapat digulir, sehingga perubahan versi mudah dibaca sebelum instalasi.
*   **Status & UX Diseragamkan:** Menyeragamkan dialog file di seluruh add-on dan meningkatkan perintah 'L' agar dapat melaporkan progres secara real-time.

## Perubahan untuk 3.6.0

*   **Sistem Bantuan:** Menambahkan perintah bantuan (`H`) di dalam Lapisan Perintah untuk menampilkan daftar pintasan dan fungsinya dengan mudah.
*   **Analisis Video Online:** Dukungan diperluas ke video **Twitter (X)**. Deteksi URL dan stabilitas juga ditingkatkan agar lebih andal.
*   **Kontribusi Proyek:** Menambahkan dialog donasi opsional bagi pengguna yang ingin mendukung pembaruan dan perkembangan proyek di masa depan.

## Perubahan untuk 3.5.0

*   **Lapisan Perintah:** Menambahkan sistem Lapisan Perintah (default: `NVDA+Shift+V`) untuk mengelompokkan pintasan di bawah satu tombol utama. Misalnya, alih-alih menekan `NVDA+Control+Shift+T` untuk menerjemahkan, kini Anda cukup menekan `NVDA+Shift+V`, lalu `T`.
*   **Analisis Video Online:** Menambahkan fitur baru untuk menganalisis video YouTube dan Instagram langsung dari URL.

## Perubahan untuk 3.1.0

*   **Mode Keluaran Langsung:** Menambahkan opsi untuk melewati dialog obrolan dan mendengar respons AI langsung melalui suara, agar lebih cepat dan mulus.
*   **Integrasi Papan Klip:** Menambahkan pengaturan baru untuk menyalin respons AI ke papan klip secara otomatis.

## Perubahan untuk 3.0

*   **Bahasa Baru:** Menambahkan terjemahan **Persia** dan **Vietnam**.
*   **Model AI Diperluas:** Daftar pilihan model ditata ulang dengan awalan yang jelas (`[Free]`, `[Pro]`, `[Auto]`) agar pengguna dapat membedakan model gratis dan model berbayar atau terbatas kuota. Dukungan untuk **Gemini 3.0 Pro** dan **Gemini 2.0 Flash Lite** juga ditambahkan.
*   **Stabilitas Dikte:** Stabilitas Dikte Cerdas ditingkatkan secara signifikan. Klip audio yang lebih pendek dari 1 detik kini diabaikan untuk mencegah halusinasi AI dan error kosong.
*   **Penanganan File:** Memperbaiki masalah yang membuat unggahan file dengan nama non-Inggris gagal.
*   **Optimasi Prompt:** Memperbaiki logika terjemahan dan menyusun hasil fitur visi agar lebih terstruktur.

## Perubahan untuk 2.9

*   **Menambahkan terjemahan Prancis dan Turki.**
*   **Tampilan Berformat:** Menambahkan tombol "Lihat Berformat" di dialog obrolan untuk melihat percakapan dengan format yang benar, seperti heading, teks tebal, dan kode, di jendela standar yang dapat dijelajahi.
*   **Pengaturan Markdown:** Menambahkan opsi "Clean Markdown in Chat" di Pengaturan. Jika opsi ini tidak dicentang, pengguna dapat melihat sintaks Markdown mentah, misalnya `**` dan `#`, di jendela obrolan.
*   **Manajemen Dialog:** Memperbaiki masalah yang membuat jendela "Refine Text" atau obrolan terbuka berkali-kali atau gagal mendapatkan fokus.
*   **Peningkatan UX:** Menyeragamkan judul dialog file menjadi "Open" dan menghapus pengumuman suara yang tidak perlu, seperti "Opening menu...", agar pengalaman lebih mulus.

## Perubahan untuk 2.8

* Menambahkan terjemahan bahasa Italia.
* **Laporan Status:** Menambahkan perintah baru (NVDA+Control+Shift+I) untuk mengumumkan status add-on saat ini, misalnya "Uploading..." atau "Analyzing...".
* **Ekspor HTML:** Tombol "Save Content" di dialog hasil kini menyimpan output sebagai file HTML terformat, termasuk gaya seperti heading dan teks tebal.
* **UI Pengaturan:** Tata letak panel pengaturan ditingkatkan dengan pengelompokan yang lebih aksesibel.
* **Model Baru:** Menambahkan dukungan untuk gemini-flash-latest dan gemini-flash-lite-latest.
* **Bahasa:** Menambahkan bahasa Nepal ke daftar bahasa yang didukung.
* **Logika Menu Refine:** Memperbaiki bug penting yang membuat perintah "Refine Text" gagal saat bahasa antarmuka NVDA bukan bahasa Inggris.
* **Dikte:** Meningkatkan deteksi hening agar tidak menghasilkan teks yang salah saat tidak ada ucapan.
* **Pengaturan Pembaruan:** "Check for updates on startup" kini dinonaktifkan secara default agar sesuai dengan kebijakan Add-on Store.
* Pembersihan kode.

## Perubahan untuk 2.7

* Memigrasikan struktur proyek ke Template Add-on resmi NV Access agar lebih sesuai standar.
* Menambahkan logika coba ulang otomatis untuk error HTTP 429 (Rate Limit), agar lebih andal saat trafik tinggi.
* Mengoptimalkan prompt terjemahan untuk akurasi lebih tinggi dan penanganan logika "Smart Swap" yang lebih baik.
* Memperbarui terjemahan Rusia.

## Perubahan untuk 2.6

* Menambahkan dukungan terjemahan Rusia (terima kasih kepada nvda-ru).
* Memperbarui pesan error agar informasi konektivitas lebih jelas.
* Mengubah bahasa target default ke bahasa Inggris.

## Perubahan untuk 2.5

* Menambahkan perintah OCR file bawaan (NVDA+Control+Shift+F).
* Menambahkan tombol "Save Chat" di dialog hasil.
* Menambahkan dukungan lokalisasi penuh (i18n).
* Memigrasikan umpan balik audio ke modul tones bawaan NVDA.
* Beralih ke Gemini File API untuk menangani PDF dan file audio dengan lebih baik.
* Memperbaiki crash saat menerjemahkan teks yang berisi kurung kurawal.

## Perubahan untuk 2.1.1

* Memperbaiki masalah variabel [file_ocr] yang tidak berfungsi dengan benar di Prompt Kustom.

## Perubahan untuk 2.1

* Menstandarkan semua pintasan agar memakai NVDA+Control+Shift untuk menghindari konflik dengan layout Laptop NVDA dan hotkey sistem.

## Perubahan untuk 2.0

* Menambahkan sistem Auto-Update bawaan.
* Menambahkan Smart Translation Cache untuk mengambil kembali teks yang pernah diterjemahkan secara instan.
* Menambahkan Conversation Memory untuk menyempurnakan hasil secara kontekstual di dialog obrolan.
* Menambahkan perintah khusus Terjemahan Papan Klip (NVDA+Control+Shift+Y).
* Mengoptimalkan prompt AI agar benar-benar mengikuti bahasa target.
* Memperbaiki crash akibat karakter khusus pada teks masukan.

## Perubahan untuk 1.5

* Menambahkan dukungan untuk lebih dari 20 bahasa baru.
* Menambahkan Dialog Refine Interaktif untuk pertanyaan lanjutan.
* Menambahkan fitur Dikte Cerdas bawaan.
* Menambahkan kategori "Vision Assistant" di dialog Input Gestures NVDA.
* Memperbaiki crash COMError pada aplikasi tertentu seperti Firefox dan Word.
* Menambahkan mekanisme coba ulang otomatis untuk error server.

## Perubahan untuk 1.0

* Rilis awal.
