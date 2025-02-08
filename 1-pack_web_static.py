#!/usr/bin/python3
# creates an archive file and compresses folder into it.

from fabric import Connection, task
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Creates a compressed .tgz archive of the web_static folder.

    - Ensures that the 'versions' directory exists.
    - Generates a timestamp-based archive name in the format:
      'web_static_<year><month><day><hour><minute><second>.tgz'.
    - Uses the tar command to create the archive.

    Returns:
        str: The path to the created archive if successful.
        None: If the archive creation fails.
    """

    # ensure versions exitst or create it
    os.makedirs("versions", exist_ok=True)

    # creating a timestamp name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"
    local(f"tar -cvzf {archive_name}")
    return archive_name
