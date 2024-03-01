from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(
    title="MDGT Report Creator",
    description="Сервис для создания отчетов по опытам",
    version="1.0.0")

origins = [
    "http://localhost",
    "http://188.225.47.38",
    "https://188.225.47.38",
    "188.225.47.38"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/", response_class=HTMLResponse)
async def index():
    html_content = """
        <html>
        <head>
            <title>MDGT Report Creator</title>
            <style>
                p {
                    font-family: Consolas;
                    text-align: center;
                    font-size: 50;
                }
                div {
                    text-align: center;
                }
                body {
                    background_color: #0a7f0b;
                }
            </style>
        </head>
        <body>
            <div>
                <img src="https://s3.timeweb.com/433ae73f-12afa07c-c290-4b34-a1e2-1dd026c9fc72/reports_data/mdgt_qr_transparent.png", alt="МОСТДОРГЕОТРЕСТ", height="400px", width="400px">
            </div>
            <p>MDGT Report Creator</p>
        </body>
</html>
        """
    return HTMLResponse(content=html_content, status_code=200)




