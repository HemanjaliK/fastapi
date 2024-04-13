from fastapi import FastAPI
from app.config import QR_DIRECTORY
from app.routers import qr_code, oauth
from app.services.qr_service import create_directory_if_not_exists  # This import is okay
from app.utils.common import setup_logging

setup_logging()

app = FastAPI(
    title="QR Code Manager",
    description="A FastAPI application for creating, listing available codes, and deleting QR codes. It also supports OAuth for secure access.",
    version="0.0.1",
    redoc_url=None,
    contact={
        "name": "API Support",
        "url": "http://www.example.com/support",
        "email": "support@example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
)

@app.on_event("startup")
async def startup_event():
    # This is now the only place where directories are created.
    create_directory_if_not_exists(QR_DIRECTORY)

app.include_router(qr_code.router)
app.include_router(oauth.router)


