


http://zulko.github.io/blog/2013/09/19/a-basic-example-of-threads-synchronization-in-python/


def view(movie):
    new_thread( play_audio( movie ) )
    play_video( movie )


In this code, play_audio() and play_video() will start at approximately the same time and will run parallely, but these functions need some preparation before actually starting playing stuff. Their code looks like that:

def play_audio(movie):
    audio = prepare_audio( movie )
    audio.start_playing()


def play_video(movie):
    video = prepare_video( movie )
    video.start_playing()


To have a well-synchronized movie we need the internal functions audio.start_playing() and video.start_playing(), which are run in two separate threads, to start at exactly the same time. How do we do that ?

The solution seems to be using threading.Event objects. An Event is an object that can be accessed from all the threads and allows very basic communication between them : each thread can set or unset an Event, or check whether this event has already been been set (by another thread).

For our problem we will use two events video_ready and audio_ready which will enable our two threads to scream at each other “I am ready ! Are you ?”. Here is the Python fot that:

import threading

def play_audio(movie, audio_ready, video_ready):

    audio = prepare_audio( movie )

    audio_ready.set() # Say "I'm ready" to play_video()
    video_ready.wait() # Wait for play_video() to say "I'm ready"

    audio.start_playing()


def play_video(movie, audio_ready, video_ready):

    video = prepare_video( movie )

    video_ready.set() # Say "I'm ready" to play_audio()
    audio_ready.wait()  # Wait for play_audio() to say "I'm ready"

    video.start_playing()


def view(movie):

    audio_ready = threading.Event()
    video_ready = threading.Event()


    # launch the parrallel audio thread
    audiothread = threading.Thread(target=play_audio,
                              args = (movie, audio_ready, video_ready))
    audiothread.start()

    play_video(movie, audio_ready, video_ready)



import time
while not audio_ready.is_set():
    time.sleep(0.002) # sleep 2 milliseconds



    Here I am using the module threading, and the two threads will be played in parrallel on the same processor. If you have a computer with several processors you can also use the multiprocessing module to have your threads played on two different processors (which can be MUCH faster). Nicely enough the two modules have the same syntax: simply replace threading by multiprocessing and Thread by Process in the example above and it should work.







































