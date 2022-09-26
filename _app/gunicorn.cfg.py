import multiprocessing

bind = ":80"
workers = multiprocessing.cpu_count() * 2 + 1
errorlog = "gunicorn_src.log"
