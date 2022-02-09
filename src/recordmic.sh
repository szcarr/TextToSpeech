#!/bin/bash
DURATION=$1
arecord -d $1 -f s16_le -r 44100 micaudio.wav