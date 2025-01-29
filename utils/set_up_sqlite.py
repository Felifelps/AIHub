def set_up_sqlite():
    import os
    os.environ["LD_LIBRARY_PATH"] = "/home/appuser/.local/bin"

    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
