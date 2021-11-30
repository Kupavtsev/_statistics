# -*- coding: utf-8 -*-
import os
import dotenv


dotenv.load_dotenv()

PG_LOGIN = os.getenv('user_login')
PG_PASSWORD = os.getenv('user_pass')






