import logging
import os
from nicegui import ui

# create the log folder if missing
log_path = 'log'
log_fileName = 'log.txt'
if os.path.exists(log_path) and os.path.isdir(log_path):
    pass
else:
    os.mkdir(log_path)

# set the log basic config with debug level
logging.basicConfig(level=logging.DEBUG
                    , format='%(asctime)s - %(levelname)-7s [%(filename)30s:%(lineno)-4s - %(funcName)30s()] %(message)s'
                    , filename=log_path + '\\' + log_fileName)

#add a basic label
ui.label('test label')

# custom_uvicorn_reload_excludes = '.*, .py[cod], .sw.*, ~*, *.txt'
# run the app in native mode
ui.run(title='My App', native=True)
#ui.run(title='My App', native=True, uvicorn_reload_excludes=custom_uvicorn_reload_excludes)

