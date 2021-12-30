#!/bin/python

import site
import pathlib

TARGET = pathlib.Path("~/.local/share/systemd/user/mpd_autoplaylist.service").expanduser()

TARGET.parent.mkdir(parents=True, exist_ok=True)


# using -m the module is not found so hardcode the path

# ExecStart="python -m mdp_autoplaylist"
# Environment="PYTHONPATH={site.USER_SITE}"

file = pathlib.Path(__file__).parent/'mpd_autoplaylist/autoplaylist.py'

s = f"""
[Unit]
Description=Auto Playlist for MPD
After=mpd.service

[Service]
ExecStart = python {file}
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=default.target
"""
TARGET.write_text(s)
print (s)
