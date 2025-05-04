:- dynamic minat_pos/1.
:- dynamic minat_neg/1.

% Hobi
hobi("Melukis").
hobi("Mendaki Gunung").
hobi("Membaca Buku").
hobi("Menari").
hobi("Menulis Cerita").
hobi("Bermain Musik").
hobi("Bermain Bola").
hobi("Coding").

% Hubungan minat dengan hobi
minat(seni, "Melukis").
minat(alam, "Mendaki Gunung").
minat(tenang, "Membaca Buku").
minat(gerak, "Menari").
minat(imajinasi, "Menulis Cerita").
minat(musik, "Bermain Musik").
minat(olahraga, "Bermain Bola").
minat(logika, "Coding").

% Pertanyaan terkait minat
pertanyaan(seni, "Apakah Anda menyukai seni atau aktivitas kreatif visual?").
pertanyaan(alam, "Apakah Anda menikmati kegiatan di alam seperti hiking atau camping?").
pertanyaan(tenang, "Apakah Anda lebih suka suasana tenang dan introspektif?").
pertanyaan(gerak, "Apakah Anda suka bergerak dan aktif secara fisik?").
pertanyaan(imajinasi, "Apakah Anda senang berimajinasi dan menciptakan cerita?").
pertanyaan(musik, "Apakah Anda menyukai musik dan alat musik?").
pertanyaan(olahraga, "Apakah Anda suka kegiatan olahraga dan kompetisi?").
pertanyaan(logika, "Apakah Anda menikmati memecahkan masalah atau logika?").

% Aturan rekomendasi
rekomendasi(H) :-
    hobi(H),
    findall(M, minat(M, H), MinatList),
    semua_minat_positif(MinatList).

semua_minat_positif([]).
semua_minat_positif([M|Rest]) :-
    minat_pos(M),
    semua_minat_positif(Rest).
