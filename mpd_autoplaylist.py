#!/bin/python3

import musicpd
import sys
import random
import datetime
import time
import argparse


ARG_PARSER = argparse.ArgumentParser(description="Client for ht3.daemon")
ARG_PARSER.add_argument("--server",   "-s", default='localhost')
ARG_PARSER.add_argument("--port",     "-p", default=6600, type=int)
ARG_PARSER.add_argument("--playlist", "-l", default="autoplay")

def main():
    o = ARG_PARSER.parse_args()
    sys.exit(run(o))

def run(options):
    mpd = musicpd.MPDClient()
    mpd.connect(options.server, options.port)


    while True:
        songs = mpd.listplaylist(options.playlist)
        if not songs:
            raise ValueError("playlist empty", options.playlist)
        random.shuffle(songs)
        works = False
        exc = False
        for song in songs:
            while True: # Wait until Conditions are met
                status = mpd.status()
                if status['consume'] != '1':
                    print ("Consume is off")
                else:
                    if status['playlistlength'] == '0':
                        print("Playlist empty")
                        break
                    if 'xfade' in status:
                        if status['playlistlength'] == '1':
                            print("No Song to CrossFade to in Playlist")
                            break
                    print ("Playlist long enough: " + status['playlistlength'])
                time.sleep(1)
                e = mpd.idle()
                print (f"Event: {e}")

            try:    # try to add and play the song
                print(f'Add {song}')
                mpd.add(song)
                mpd.play()
            except Exception as e:
                print(f'{e}')
                exc = e
            else:
                works = True

        if not works:   # If no Song worked, raise the last exception
            raise exc

if __name__ == '__main__':
    main()
