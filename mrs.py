#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import librosa  # https://librosa.org/
import librosa.display
import librosa.beat
import sounddevice as sd  # https://anaconda.org/conda-forge/python-sounddevice
import warnings


def readFeatures(fileName):  # 2
    # 2.1
    top100 = np.genfromtxt(fileName, delimiter=',')
    lines, columns = np.shape(top100)
    #print("dim ficheiro top100_features.csv original = %d x %d\n\n" % (lines, columns), top100)
    top100 = top100[1:, 1:(columns-1)]
    """lines, columns = np.shape(top100)
    print("\ndim top100 data = %d x %d\n\n" % (lines, columns), top100)"""
    return top100


def normalization(top100):  # 2.1.2
    top100_N = np.zeros(np.shape(top100))
    columns = np.shape(top100_N)[1]
    for i in range(columns):
        vmax = top100[:, i].max()
        vmin = top100[:, i].min()
        top100_N[:, i] = (top100[:, i] - vmin)/(vmax - vmin)
    # print(top100_N)
    return top100_N


def saveFeatures(fileName, top100_N):  # 2.1.3
    fileName.replace(".csv", "_normalized_data.csv")
    np.savetxt(fileName, top100_N, fmt="%lf", delimiter=',')

    """# checando
    top100_N = np.genfromtxt(fileName, delimiter=',')
    lines, columns = top100_N.shape
    print("dim ficheiro top100_features_normalized_data.csv = ", lines, "x", columns)
    print()
    print(top100_N)"""


def loadAudio(fileName, sr, mono):
    warnings.filterwarnings("ignore")
    y, fs = librosa.load(fileName, sr=sr, mono=mono)
    # print(y.shape)
    # print(fs)
    return y, fs


# --- Extract features
def extracFeatures(y):  # 2.2.2
    rms = librosa.feature.rms(y=y)
    rms = rms[0, :]
    # print(rms.shape)
    times = librosa.times_like(rms)
    plt.figure()
    plt.plot(times, rms)
    plt.xlabel('Time (s)')
    plt.title('RMS')
    plt.imshow()


if __name__ == "__main__":
    plt.close('all')

    # --- Ex2.1
    featuresFile = './Features - Audio MER/top100_features.csv'
    top100 = readFeatures(featuresFile)
    top100_N = normalization(top100)
    saveFeatures(featuresFile, top100_N)

    # --- Load file
    audioFile = "MER_audio_taffc_dataset/audios/MT0000414517.mp3"
    sr = 22050  # sampling rate
    mono = True
    y, fs = loadAudio(audioFile, sr, mono)

    # --- Play Sound
    sd.play(y, sr, blocking=False)

    # --- Plot sound waveform
    plt.figure()
    librosa.display.waveshow(y)

    # --- Plot spectrogram
    Y = np.abs(librosa.stft(y))
    Ydb = librosa.amplitude_to_db(Y, ref=np.max)
    fig, ax = plt.subplots()
    img = librosa.display.specshow(Ydb, y_axis='log', x_axis='time', ax=ax)
    ax.set_title('Power spectrogram')
    fig.colorbar(img, ax=ax, format="%+2.0f dB")

    plt.show()
