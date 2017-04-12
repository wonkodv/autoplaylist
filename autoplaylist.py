#!/bin/python3

import musicpd
import sys
import random


def main():
    mpd = musicpd.MPDClient()
    mpd.connect("localhost",6600)

    while True:
        loop(mpd)
        mpd.idle()

def loop(mpd):
    status = mpd.status()
    if status['consume'] != '1':
        print ("Consume is off")
        return

    if status['playlistlength'] != '0':
        print ("Playlist long enough: " + status['playlistlength'])
        return

    songs = mpd.listplaylist("autoplay")
    song = random.choice(songs)
    print ("Select from {} songs: {}".format(len(songs), song))
    mpd.add(song)
    mpd.play()

if __name__ == '__main__':
    sys.exit(main())

