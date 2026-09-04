# SOAL 1

print("Simulasi Transaksi soal 1")

subtotal = int(input("Masukkan subtotal belanja (Rp): "))
metode_pembayaran = input("Masukkan metode pembayaran (QRIS/CREDIT" \
" CARD/CASH): ").upper()
kupon_flash_sale = input("Apakah punya kupon flashsale? (YA/" \
"TIDAK): ").upper()

persen_diskon = 0
cashback = 0

if subtotal >= 5000000:
    persen_diskon = 0.25
    cashback = 100000
elif subtotal >= 3000001:
    persen_diskon = 0.15
    cashback = 50000
else:
    persen_diskon = 0.05
    if kupon_flash_sale == "YA":
        persen_diskon += 0.10


if subtotal >= 3000000 and metode_pembayaran == "QRIS":
    persen_diskon += 0.05

nominal_diskon = int(subtotal * persen_diskon)
total_bayar = int(subtotal - nominal_diskon)

print("Ringkasan Pembayaran")
print(f"Subtotal Belanja  : Rp {subtotal}")
print(f"Metode Pembayaran : {metode_pembayaran}")
print(f"Kupon Flash Sale  : {kupon_flash_sale}")
print(f"Total Diskon      : Rp {nominal_diskon}")
print(f"Cashback          : Rp {cashback}")
print(f"TOTAL BAYAR       : Rp {total_bayar}")