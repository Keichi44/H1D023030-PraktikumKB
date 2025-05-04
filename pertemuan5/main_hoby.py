from pyswip import Prolog
import tkinter as tk
from tkinter import ttk, messagebox

prolog = Prolog()
prolog.consult("main_hoby.pl")

class PakarHobiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Rekomendasi Hobi")
        self.minat_list = self.get_pertanyaan()
        self.current_index = 0

        self.mainframe = ttk.Frame(root, padding="20")
        self.mainframe.grid(column=0, row=0)

        ttk.Label(self.mainframe, text="Rekomendasi Hobi", font=("Arial", 16)).grid(column=0, row=0, columnspan=2, pady=10)

        self.pertanyaan_label = ttk.Label(self.mainframe, text="", wraplength=400)
        self.pertanyaan_label.grid(column=0, row=1, columnspan=2, pady=10)

        self.btn_ya = ttk.Button(self.mainframe, text="Ya", command=lambda: self.jawab("ya"))
        self.btn_tidak = ttk.Button(self.mainframe, text="Tidak", command=lambda: self.jawab("tidak"))

        self.btn_ya.grid(column=0, row=2, padx=10, pady=10)
        self.btn_tidak.grid(column=1, row=2, padx=10, pady=10)

        self.tampilkan_pertanyaan()

    def get_pertanyaan(self):
        pertanyaan = []
        for hasil in prolog.query("pertanyaan(Kode, Teks)"):
            pertanyaan.append((hasil["Kode"], hasil["Teks"]))
        return pertanyaan

    def tampilkan_pertanyaan(self):
        if self.current_index < len(self.minat_list):
            kode, teks = self.minat_list[self.current_index]
            self.pertanyaan_label.config(text=teks)
        else:
            self.analisis()

    def jawab(self, pilihan):
        kode, _ = self.minat_list[self.current_index]
        if pilihan == "ya":
            prolog.assertz(f"minat_pos({kode})")
        else:
            prolog.assertz(f"minat_neg({kode})")
        self.current_index += 1
        self.tampilkan_pertanyaan()

    def analisis(self):
        hasil = list(prolog.query("rekomendasi(Hobi)"))
        if hasil:
            nama = hasil[0]["Hobi"]
            messagebox.showinfo("Rekomendasi Hobi", f"Hobi yang cocok untuk Anda: {nama}")
        else:
            messagebox.showinfo("Rekomendasi Hobi", "Belum ada hobi yang cocok teridentifikasi.")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = PakarHobiApp(root)
    root.mainloop()
