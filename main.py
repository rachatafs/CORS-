from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

# ตั้งค่า CORS (รปภ. คอยคัดกรองข้ามพอร์ต)
# สั่งเปิดใช้งานระบบ CORS ให้กับแอปพลิเคชันของเรา
app.add_middleware(
    CORSMiddleware,
    #นุญาตให้ทุกเว็บไซต์หรือทุกพอร์ตบนโลก (เครื่องหมาย * หมายถึงทั้งหมด) สามารถเข้ามาดึงข้อมูลจาก API ของเราได้
    allow_origins=["*"],
    # อนุญาตให้ใช้คำสั่ง HTTP ได้ทุกรูปแบบ เช่น GET, POST, PUT, DELETE
    allow_methods=["*"],
    # อนุญาตให้แนบข้อมูลส่วนหัว (Headers) มากับคำขอได้ทุกประเภท เช่น Token ยืนยันตัวตน
    allow_headers=["*"],
)

# หน้าเว็บ Frontend คลีนๆ สวยงาม มินิมอล
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="th">
    <head>
        <meta charset="UTF-8">
        <title>CORS Demo</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f1f5f9; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .box { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); text-align: center; width: 400px; }
            h2 { color: #1e293b; margin-bottom: 10px; }
            p { color: #64748b; font-size: 14px; margin-bottom: 20px; }
            button { background: #3b82f6; color: white; border: none; padding: 10px 20px; font-size: 15px; border-radius: 6px; cursor: pointer; transition: 0.2s; }
            button:hover { background: #2563eb; }
            pre { background: #0f172a; color: #38bdf8; padding: 15px; border-radius: 6px; text-align: left; margin-top: 20px; font-size: 13px; max-height: 150px; overflow-y: auto; }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>CORS Middleware Demo</h2>
            <p>ทดสอบการดึงข้อมูล API ข้ามพอร์ตด้วย FastAPI</p>
            <button onclick="getData()">ดึงข้อมูลสินค้า</button>
            <pre id="output">รอผลลัพธ์...</pre>
        </div>

        <script>
            async function getData() {
                try {
                    const res = await fetch('http://127.0.0.1:8000/api/products');
                    const data = await res.json();
                    document.getElementById('output').innerText = JSON.stringify(data, null, 2);
                } catch (err) {
                    document.getElementById('output').innerText = "CORS Error: " + err;
                }
            }
        </script>
    </body>
    </html>
    """

# Backend API ส่งข้อมูลสินค้า
# กำหนดว่าถ้ามีใครยิงคำสั่งแบบ GET มาที่ลิงก์นี้ ให้ทำงานฟังก์ชันด้านล่าง
@app.get("/api/products")
# ฟังก์ชันหลักของหลังบ้าน
def get_products():
    return [
        {"id": 1, "name": "iPhone 14 Pro Max", "price": 40000},
        {"id": 2, "name": "Gaming Mouse", "price": 12000}
    ]