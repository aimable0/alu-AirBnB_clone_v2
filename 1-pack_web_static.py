#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from fabric import Connection, task
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a tgz archive"""

    # ensure versions exitst or create it
    os.makedirs("versions", exist_ok=True)

    # creating a timestamp name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    archive_name = f"versions/web_static_{timestamp}.tgz"
    try:
        local(f"tar -cvzf {archive_name}")
        return archive_name
    except:
        return None