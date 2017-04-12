Auto Playlist for MPD
=================

Waits until mpds playlist is empty, (and consume is on) and adds 1 random song from the playlist `autoplaylist`. Then it Waits again.


Crontab
-------

    @reboot mpd && python3 ~/code/autoplaylist/autoplaylist.py &> ~/tmp/autoplaylist.log



