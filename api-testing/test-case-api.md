# Test Case — API Testing
**Base URL:** https://jsonplaceholder.typicode.com
**Dibuat oleh:** David Darmawan
**Tanggal:** 11-03-2026


| TC ID | Method | Endpoint | Body | Expected Status | Actual Status | Status |
|-----------------------------------------------------------------------------|
| TC_API_001 | GET | /users | - | 200 OK | 200 OK | Pass |
| TC_API_002 | GET | /users/1 | - | 200 OK | 200 OK | Pass |
| TC_API_003 | GET | /users/9999 | - | 404 Not Found | 404 Not Found | Pass |
| TC_API_004 | POST | /posts | {title, body, userId} | 201 Created | 201 Created | Pass |
| TC_API_005 | DELETE | /posts/1 | - | 200 OK | 200 OK | Pass |
