# 📋 Test Case — Fitur Login
**Website:** [https://www.saucedemo.com](https://www.saucedemo.com)  
**Module:** Authentication - Login  
**Dibuat oleh:** QA Tester  
**Tanggal:** 2026-03-04

---

## Precondition (Berlaku untuk Semua Test Case)
- Website sudah terbuka di browser Google Chrome
- Akses ke halaman: https://www.saucedemo.com

---

## Ringkasan Eksekusi

| Total TC | Pass | Fail | Pass Rate |
|---|---|---|---|
| 9 | 9 | 0 | 100% |

---

## TC_LOGIN_01 — Login dengan Kredensial Valid

| Field | Detail |
|---|---|
| **Test Case ID** | TC_LOGIN_01 |
| **Title** | Login valid terhadap website saucedemo.com |
| **Module** | Login |
| **Priority** | High |

**Test Steps:**
1. Buka laman website https://www.saucedemo.com
2. Masukkan username
3. Masukkan password
4. Klik tombol "Login"

**Test Data:**
- Username: `standard_user`
- Password: `secret_sauce`

**Expected Result:**
- User berhasil login
- Diarahkan ke halaman inventory
- Muncul list dari berbagai produk yang ada di inventory

**Actual Result:**
- User berhasil login
- Diarahkan ke halaman inventory
- Muncul list dari berbagai produk yang ada di inventory

**Status: ✅ PASS**

---

## TC_LOGIN_02 — Login dengan Password Salah

| Field | Detail |
|---|---|
| **Test Case ID** | TC_LOGIN_02 |
| **Title** | Login dengan password yang salah |
| **Module** | Login dengan password yang salah |
| **Priority** | High |

**Test Steps:**
1. Buka laman website https://www.saucedemo.com
2. Masukkan username
3. Masukkan password yang salah
4. Klik tombol "Login"

**Test Data:**
- Username: `standard_user`
- Password: `secret_sauce1`

**Expected Result:**
- Login GAGAL
- Muncul pesan error
- User tetap di halaman login

**Actual Result:**
- Login GAGAL
- Muncul pesan error
- User tetap di halaman login

**Status: ✅ PASS**

---

## TC_LOGIN_03 — Login dengan Username Tidak Terdaftar

| Field | Detail |
|---|---|
| **Test Case ID** | TC_LOGIN_03 |
| **Title** | Login dengan username yang tidak terdaftar |
| **Module** | Login dengan username tidak terdaftar |
| **Priority** | High |

**Test Steps:**
1. Buka laman website https://www.saucedemo.com
2. Masukkan username yang tidak terdaftar
3. Masukkan password
4. Klik tombol "Login"

**Test Data:**
- Username: `standard_up`
- Password: `secret_sauce`

**Expected Result:**
- Login GAGAL
- Muncul pesan error
- User tetap di halaman login

**Actual Result:**
- Login GAGAL
- Muncul pesan error
- User tetap di halaman login

**Status: ✅ PASS**

---

## TC_LOGIN_04 — Login dengan Username Kosong

| Field | Detail |
|---|---|
| **Test Case ID** | TC_LOGIN_04 |
| **Title** | Login dengan username kosong |
| **Module** | Login dengan username yang kosong |
| **Priority** | High |

**Test Steps:**
1. Buka laman website https://www.saucedemo.com
2. Biarkan kolom username kosong
3. Masukkan password
4. Klik tombol "Login"

**Test Data:**
- Username: *(kosong)*
- Password: `secret_sauce`

**Expected Result:**
- Login GAGAL
- Muncul pesan error
- User tetap di halaman login

**Actual Result:**
- Login GAGAL
- Muncul pesan error
- User tetap di halaman login

**Status: ✅ PASS**

---

## TC_LOGIN_05 — Login dengan Password Kosong

| Field | Detail |
|---|---|
| **Test Case ID** | TC_LOGIN_05 |
| **Title** | Login dengan password kosong |
| **Module** | Login dengan password kosong |
| **Priority** | High |

**Test Steps:**
1. Buka laman website https://www.saucedemo.com
2. Masukkan username
3. Biarkan kolom password kosong
4. Klik tombol "Login"

**Test Data:**
- Username: `standard_user`
- Password: *(kosong)*

**Expected Result:**
- Login GAGAL
- Muncul pesan error
- User tetap di halaman login

**Actual Result:**
- Login GAGAL
- Muncul pesan error
- User tetap di halaman login

**Status: ✅ PASS**

---

## TC_LOGIN_06 — Login dengan Username dan Password Kosong

| Field | Detail |
|---|---|
| **Test Case ID** | TC_LOGIN_06 |
| **Title** | Login dengan username dan password kosong |
| **Module** | Login dengan username dan password kosong |
| **Priority** | High |

**Test Steps:**
1. Buka laman website https://www.saucedemo.com
2. Biarkan kolom username dan password kosong
3. Klik tombol "Login"

**Test Data:**
- Username: *(kosong)*
- Password: *(kosong)*

**Expected Result:**
- Login GAGAL
- Muncul pesan error
- User tetap di halaman login

**Actual Result:**
- Login GAGAL
- Muncul pesan error
- User tetap di halaman login

**Status: ✅ PASS**

---

## TC_LOGIN_07 — Login dengan Spasi di Awal dan Akhir Username

| Field | Detail |
|---|---|
| **Test Case ID** | TC_LOGIN_07 |
| **Title** | Login dengan spasi di awal dan akhir username |
| **Module** | Login dengan spasi di awal dan akhir username |
| **Priority** | High |

**Test Steps:**
1. Buka laman website https://www.saucedemo.com
2. Masukkan username dengan spasi di awal dan akhir
3. Masukkan password
4. Klik tombol "Login"

**Test Data:**
- Username: `(spasi)standard_user(spasi)`
- Password: `secret_sauce`

**Expected Result:**
- Login GAGAL
- Muncul pesan error
- User tetap di halaman login

**Actual Result:**
- Login GAGAL
- Muncul pesan error
- User tetap di halaman login

**Status: ✅ PASS**

---

## TC_LOGIN_08 — Login dengan Password Kurang dari 8 Karakter

| Field | Detail |
|---|---|
| **Test Case ID** | TC_LOGIN_08 |
| **Title** | Login dengan password kurang dari 8 karakter |
| **Module** | Login dengan password kurang dari 8 karakter |
| **Priority** | High |

**Test Steps:**
1. Buka laman website https://www.saucedemo.com
2. Masukkan username
3. Masukkan password kurang dari 8 karakter
4. Klik tombol "Login"

**Test Data:**
- Username: `standard_user`
- Password: `secret_`

**Expected Result:**
- Login GAGAL
- Muncul pesan error
- User tetap di halaman login

**Actual Result:**
- Login GAGAL
- Muncul pesan error
- User tetap di halaman login

**Status: ✅ PASS**

---

## TC_LOGIN_09 — Login Kembali Setelah Logout

| Field | Detail |
|---|---|
| **Test Case ID** | TC_LOGIN_09 |
| **Title** | Login kembali setelah logout |
| **Module** | Login kembali setelah logout |
| **Priority** | High |

**Test Steps:**
1. Buka laman website https://www.saucedemo.com
2. Masukkan username
3. Masukkan password
4. Klik tombol "Login"
5. Klik icon menu (3 garis) lalu klik "Logout"
6. Login kembali dengan kredensial yang sama

**Test Data:**
- Username: `standard_user`
- Password: `secret_sauce`

**Expected Result:**
- Login berhasil
- Muncul tampilan produk
- Tampilan menu terbuka saat diklik
- Kembali ke tampilan login setelah logout
- Bisa login kembali setelah logout

**Actual Result:**
- User berhasil login
- Muncul tampilan produk
- Tampilan menu terbuka
- Kembali ke halaman login setelah logout
- Berhasil login kembali

**Status: ✅ PASS**
