import multiprocessing
import os
bind = f"0.0.0.0:{os.getenv('PORT',8000)}"
worker_class = "uvicorn.workers.UvicornWorker"
workers = 3
wsgi_app = "app.main:app"
timeout = 600
