import json
import os
import platform
from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor

from datetime import datetime
from logging import Logger as LG
from threading import Lock

from project_name.db_manager.orm_helper import *

class FileController:
    def __init__(self,config):
        self.config = config
