#!/usr/bin/python3
# creates an archive file and compresses folder into it.

from fabric import Connection, task
import os
import tarfile
from datetime import datetime

def do_pack():
    """function that creates a .tgz archive from the contents of web_static"""

    # ensure versions exitst or create it
    os.makedirs("versions", exist_ok=True)

    # creating a timestamp name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"

    with tarfile.open(archive_name, "w:gz") as tar:
        tar.add("web_static", arcname="web_static")
    return archive_name
