# 🐛 Bug Report — Tombol "Add to Cart" Tidak Merespons

**Website:** [https://www.saucedemo.com](https://www.saucedemo.com)  
**Dibuat oleh:** QA Tester  
**Tanggal ditemukan:** 2026-03-04

---

## Detail Bug

| Field | Detail |
|---|---|
| **Bug ID** | BUG_Cart_001 |
| **Severity** | 🔴 Critical |
| **Priority** | 🔴 High |
| **Status** | Open |

---

## Deskripsi

Ketika pengguna mengklik tombol **"Add to Cart"** untuk menambahkan produk ke keranjang, tombol tersebut tidak bisa diklik, tidak muncul respons apapun, dan tombol mati. Sementara untuk produk lain, tombol "Add to Cart" bisa diklik dan produk berhasil masuk ke keranjang.

---

## Steps to Reproduce

1. Buka browser Chrome versi 145.0.7632.160 (Official Build) (64-bit)
2. Akses halaman login di https://www.saucedemo.com
3. Masukkan username: `error_user`
4. Masukkan password: `secret_sauce`
5. Klik tombol "Login"
6. Klik tombol **"Add to Cart"** pada salah satu produk yang bermasalah

---

## Expected Result

- Pengguna berhasil mengklik tombol "Add to Cart"
- Produk masuk ke keranjang belanja
- Badge angka pada icon keranjang bertambah

---

## Actual Result

- Tombol "Add to Cart" **tidak merespons** sama sekali
- Halaman tetap di posisi yang sama
- Tidak ada loading, tidak ada pesan error, tidak ada produk yang masuk keranjang
- Badge pada icon keranjang tidak berubah

---

## Environment

| Field | Detail |
|---|---|
| **OS** | Windows 11 Home 64-bit |
| **Browser** | Chrome versi 145.0.7632.160 (Official Build) (64-bit) |
| **Device** | Acer Nitro 5 AN-515-58 |
| **URL** | https://www.saucedemo.com/ |
| **User Login** | error_user |

---

## Attachment

- 📹 `Swag Labs - Google Chrome 2026-03-04 15-00-51.mp4`

---

## Catatan Tambahan

Bug ini hanya terjadi pada akun `error_user`. Pada akun `standard_user`, tombol "Add to Cart" berfungsi normal.
