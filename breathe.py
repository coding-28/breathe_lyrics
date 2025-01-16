import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.08):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("What's that supposed to be about, baby?", 0.08),
        ("Go free up your vibe, stop acting crazy",  0.08),    
        ("Reminiscing all the good times daily", 0.08),
        ("Try and pull that, got me acting shady",  0.08),
        ("What's that supposed to be about, baby?", 0.08),
        ("Go free up your vibe, stop acting crazy",  0.08),
        ("You know I give you the good loving dailyg",  0.08),
        ("Try and pull that, got me actin' shady", 0.08)
    ]
    delays = [0, 3, 7, 9, 13, 15, 19, 21]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
