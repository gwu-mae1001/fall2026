
import numpy as np
import sounddevice as sd

def play_power_chord(root_freq, duration=1.0, fs=44100):
    fifth_freq = root_freq * 2**(7/12)
    t = np.linspace(0, duration, int(fs*duration), endpoint=False)
    tone = np.sin(2*np.pi*root_freq*t) + np.sin(2*np.pi*fifth_freq*t)
    tone = tone / np.max(np.abs(tone))  # Normalize
    sd.play(tone, fs)
    sd.wait()

# for i in range(5):
# play_power_chord(440)  # Play A5 chord
play_power_chord(82.41)
play_power_chord(110)
play_power_chord(146.83)
play_power_chord(196)
play_power_chord(246.94)
play_power_chord(329.63)

# A minor chord is a summation of these three frquencyies
# A (A3): 220.00 Hz
# C (C4): 261.63 Hz
# E (E4): 329.63 Hz

