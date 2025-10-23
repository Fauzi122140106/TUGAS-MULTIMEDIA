import numpy as np
import matplotlib
matplotlib.use('Agg')  # <-- tambahkan ini untuk hindari error Tcl/Tk
import matplotlib.pyplot as plt

# Parameter
duration = 2       # seconds
sample_rate = 44100
frequency = 440    # A4 note

# Generate time axis
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate sine wave
audio_signal = np.sin(2 * np.pi * frequency * t)

# Plot waveform (first 1000 samples)
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], audio_signal[:1000])
plt.title('Sine Wave (440 Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.savefig('sine_wave_test.png', dpi=150, bbox_inches='tight')
plt.show()

# Info
print(f"Generated {duration}s sine wave at {frequency}Hz")
print(f"Sample rate: {sample_rate}Hz")
print(f"Total samples: {len(audio_signal)}")
