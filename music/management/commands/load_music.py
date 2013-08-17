from django.core.management.base import BaseCommand, CommandError
from music.models import Song

import os, string


class Command(BaseCommand):
    args = '<music_root_path>'
    help = 'Loads music from files'

    def handle(self, *args, **options):
        def list_subdirs(path):
            return [ d for d in os.listdir(path) if not os.path.isfile(os.path.join(path, d)) ]

        def list_subfiles(path):
            return [ d for d in os.listdir(path) if os.path.isfile(os.path.join(path, d)) ]

        def load_music_dir(music_root):
            print "searching in music_root=%s" % music_root
            for letter_dir in list_subdirs(music_root):
                print "  searching in letter_dir=%s" % letter_dir
                for artist_dir in list_subdirs(os.path.join(music_root, letter_dir)):
                    print "    searching artist_dir=%s" % artist_dir
                    for album_dir in list_subdirs(os.path.join(music_root, letter_dir, artist_dir)):
                        print "      searching album_dir=%s" % album_dir

                        for f in list_subfiles(os.path.join(music_root, letter_dir, artist_dir, album_dir)):
                            name = os.path.splitext(f)[0]
                            extension = os.path.splitext(f)[1][1:]
                            print "        adding song at %s with format=%s" %(f, extension)
                            song = Song(
                                path=os.path.join(letter_dir, artist_dir, album_dir, f),
                                name=name,
                                artist=artist_dir,
                                album=album_dir,
                                format=extension,autoloaded=True,
                            )
                            song.save()
                            print "        saving song..."

            print "-- Done with music!"

        if len(args) is 1:
            load_music_dir(args[0])
        else:
            print "Usage: load_music <music_root>"
