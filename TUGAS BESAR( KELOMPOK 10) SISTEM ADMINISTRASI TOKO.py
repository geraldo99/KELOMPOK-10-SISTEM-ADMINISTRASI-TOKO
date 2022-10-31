from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
### FRAME GUI
messagebox.showwarning("Perhatian", "HANYA DIGUNAKAN OLEH PEMILIK, SEGALA MACAM PELANGGARAN AKAN DITUNTUT SECARA HUKUM")

root = tk.Tk()
root.geometry('900x600')
root.title("TOKO SEPATU DAGO")

teks1 = ''' ================================TOKO SEPATU DAGO=================================
TOKO SEPATU DAGO TELAH BERDIRI
SEJAK 197O DAN TELAH BERPENGALAMAN
SELAMA 52 TAHUN DALAM MELAYANI KONSUMEN.
TOKO SEPATU DAGO MELAYANI
PEMBELIAN SEPATU SERTA BERBAGAI
PRODUK LAINNYA DARI BERBAGAI
MERK SERTA JAMINAN ORISINILITAS
YANG TERJAMIN DAN TERPERCAYA
SEBAGAI DISTRIBUTOR.
=============================================================================================
'''

judul1= tk.Label(root, text="ADMINISTRATION TOOLS", font=('Arial',15,'bold'), bg='white')
judul1.grid(row=0, column=0)

label_e= tk.Label(root, bg='black', width=3, height=35)
label_e.grid(row=1, column=1)

kanvas= tk.Frame(root, bg='black',width=150, height=60)
kanvas.grid(row=1, rowspan=3, column=0)

frame_list1= tk.Frame(kanvas, bg='ivory4', width=200, height=80)
frame_about= tk.Frame(kanvas, bg='white', width=90, height=80)

aboutus = tk.Label(frame_about, text=teks1, bg="white", width=40, height=30).grid()

layar= tk.Label(kanvas, bg='black',width=50, height=30)
layar.grid(row=0, column=0)

kanvase= tk.Frame(layar,width=30, height=100)
kanvase.grid(row=4, column=0, rowspan=3)
###

### FUNGSI ENTRY

frame_editor1= tk.Entry(kanvase, bg='white', width=35)
frame_editor1.grid(row=0, column=1)
frame_editor2= tk.Entry(kanvase, bg='white', width=35)
frame_editor2.grid(row=1, column=1)
frame_editor3= tk.Entry(kanvase, bg='white', width=35)
frame_editor3.grid(row=2, column=1)
frame_editor4= tk.Entry(kanvase, bg='white', width=35)
frame_editor4.grid(row=3, column=1)
frame_editor5= tk.Entry(kanvase, bg='white', width=35)
frame_editor5.grid(row=4, column=1)


### TOOLS EDITOR

merk = tk.Label(kanvase, text="MERK", font=('Arial',15,'bold'))
merk.grid(row=0, rowspan=1, column=0)

ukuran = tk.Label(kanvase, text="UKURAN", font=('Arial',15,'bold'))
ukuran.grid(row=1, column=0)

harga = tk.Label(kanvase, text="HARGA", font=('Arial',15,'bold'))
harga.grid(row=2, column=0)

stok = tk.Label(kanvase, text="STOK", font=('Arial',15,'bold'))
stok.grid(row=3, column=0)

jenis = tk.Label(kanvase, text="JENIS", font=('Arial',15,'bold'))
jenis.grid(row=4, column=0)

### TABULASI PRODUK
merk = [
    ["Nike Air Force 1 React", '40', '900000', '12', "MEN"],
    ["Nike Air Force 1 Vintage", '40', '999000', '12', "MEN"],
    ["Adidas Ultraboost 2000", '35', "1000000", '12', 'UNISEX'] 
]

scroll = tk.Scrollbar(frame_list1)
scroll.grid(row=1, column=2)

tree = ttk.Treeview(frame_list1, height=15, yscrollcommand=scroll.set)
tree['columns']=("1", "2", "3", "4", "5")




tree.column("#0", width=2, minwidth=2)
tree.column("1", width=180, minwidth=25)
tree.column("2", width=80, minwidth=25)
tree.column("3",width=150, minwidth=25)
tree.column("4", width=80, minwidth=25)
tree.column("5", width=110, minwidth=25)

tree.heading("#0")
tree.heading("1", text="MERK" )
tree.heading("2", text="UKURAN" )
tree.heading("3", text="HARGA")
tree.heading("4", text="STOK")
tree.heading("5", text="JENIS") 

tree.grid(row=1, column=1)


### FUNGSI-FUNGSI
global count
count = 0
for record in merk  :
    tree.insert(parent="", index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]))
    count += 1
scroll.config(command=tree.yview)



#Menginput data baru 
def data():
    global count
    tree.insert(parent="", index='end', iid=count, text='', values=(frame_editor1.get(), frame_editor2.get(),frame_editor3.get(),frame_editor4.get(),frame_editor5.get()))
    frame_editor1.delete(0, 'end')
    frame_editor2.delete(0, 'end')
    frame_editor3.delete(0, 'end')
    frame_editor4.delete(0, 'end')
    frame_editor5.delete(0, 'end')
    count += 1

#Menghapus seluruh data    
def hapus_semua():
    for record in tree.get_children():
        tree.delete(record)

#Menghapus data satu-persatu       
def hapus_item():
    cursor = tree.selection()[0]
    tree.delete(cursor)
#Menampilkan LIST DATA
def muncul():
    frame_list1.grid(row=0, rowspan=3, column=1)
    
#Menutup frame_list yaitu frame yang membawa list data serta menutup frame 'TENTANG KAMI'
def tutup():
    frame_list1.grid_forget()
    frame_about.grid_forget()

#KELUAR DARI PROGRAM
def keluar():
    root.destroy()
#MENAMPILKAN FRAME 'TENTANG KAMI'
def lisensi():
    frame_about.grid(row=0, column=2)
    
    
    

### TOMBOL-TOMBOL

#TOMBOL MENU UTAMA
    
button1 = tk.Button(layar, text="DAFTAR PRODUK", width=43, height=5, command=muncul).grid(row=0, column=0)
button3 = tk.Button(layar, text="RESET", width=43, height=5, command=hapus_semua).grid(row=2,column=0)
button4 = tk.Button(layar, text="TENTANG KAMI", width=43, height=5, command=lisensi).grid(row=3, column=0)

#TOMBOL EDITOR
button5 = tk.Button(kanvase, text="TUTUP", width=10, height=2, command=tutup).grid(row=5, column=0)
button6= tk.Button(kanvase, text="HAPUS", width=10, height=2, command=hapus_item).grid(row=6, column=0)
button7 = tk.Button(kanvase, text="TAMBAH", width=10, height=2, command=data).grid(row=5, column=1)
button8 = tk.Button(kanvase, text="KELUAR", width=10, height=2, command=keluar).grid(row=6, column=1)   

root.mainloop()






"""
DAFTAR PRODUK

Men Nike
2. Nike Air Force 1 React
3. Nike Air Force 1 Vintage
4. Nike Air max 97 Premium
5. Nike Air Max 95 (U)
6. Nike Flyknit Racer (U)
Women Nike
8. Nike Air Force 1 Pixel
9. Nike Daybreak
10. Nike Zoom Fly 5
11. Nike Air Max Bliss(U)
12. Nike Air Rift (U)
Men Adidas
14. Adidas ZX Alkyne
15. Adidas ZX 5K
16. Adidas X9000
17. Adidas Ultraboost 2000 (U)
18. Supernova (U)
Women Adidas
20. Adidas Aquina
21. Adidas Grand Court
22. Adidas Retropy
23. Adidas Duramo (U)
24. Adidas Breaknet (U)
"""














