#!/usr/bin/python3
# creates an archive file and compresses folder into it.

from fabric import Connection, task
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """This function creates a .tgz archive from the contents of web_static
    on success:
        - Returns the archive path
    """

    # ensure versions exitst or create it
    os.makedirs("versions", exist_ok=True)

    # creating a timestamp name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"
    local(f"tar -cvzf {archive_name}")
    return archive_name
