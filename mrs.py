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
    fileName = fileName.replace(".csv", "_normalized_data.csv")
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
def extracFeatures():  # 2.2.2
    if not os.path.isdir(audioDir):
        print("Directory not found!")
        return

    warnings.filterwarnings("ignore")

    # List of songs to extract features
    files = os.listdir(audioDir)
    files.sort()
    numFiles = len(files)
    allSongs = np.zeros((numFiles, 190))

    # Extract features of each song
    for i in range(numFiles):
        features = []

        # Song to extract
        inFile = librosa.load(audioDir + files[i], sr=22050, mono=True)[0]

        # Extract mfcc
        mfcc = librosa.feature.mfcc(inFile, n_mfcc=13)
        features.append(mfcc)

        # Extract pectral centroid
        spectral_centroid = librosa.feature.spectral_centroid(inFile)
        features.append(spectral_centroid)

        # Extract spectral bandwith
        spectral_bandwidth = librosa.feature.spectral_bandwidth(inFile)
        features.append(spectral_bandwidth)

        # Extract spectral contrast
        spectral_contrast = librosa.feature.spectral_contrast(inFile, n_bands=6)
        features.append(spectral_contrast)

        # Extract spectral flatness
        spectral_flatness = librosa.feature.spectral_flatness(inFile)
        features.append(spectral_flatness)

        # Extract spectral rollof
        spectral_rolloff = librosa.feature.spectral_rolloff(inFile)
        features.append(spectral_rolloff)

        # Extract F0
        F0 = librosa.yin(inFile, fmin=20, fmax=11025)
        features.append(F0)

        # Extract rms
        rms = librosa.feature.rms(inFile)
        features.append(rms)

        # Extract zero_crossing_rate
        zero_crossing_rate = librosa.feature.zero_crossing_rate(inFile)
        features.append(zero_crossing_rate)

        # Extract tempo
        tempo = librosa.beat.tempo(inFile)

        allFeatures = np.array([])
        for feature in features:
            try:
                r, _ = feature.shape
            except:
                r = feature.shape[0]
                feature = feature.reshape((1, r), order='F')
                r, _ = feature.shape

            addFeature = np.zeros((r, 7))
            for j in range(r):
                mean = np.mean(feature[j, :])
                stdDev = np.std(feature[j, :])
                skew = st.skew(feature[j, :])
                kurtosis = st.kurtosis(feature[j, :])
                median = np.median(feature[j, :])
                maxv = np.max(feature[j, :])
                minv = np.min(feature[j, :])

                addFeature[j, :] = np.array([mean, stdDev, skew, kurtosis, median, maxv, minv])

            addFeature = addFeature.flatten()
            allFeatures = np.append(allFeatures, addFeature)

        allFeatures = np.append(allFeatures, tempo)
        allSongs[i] = allFeatures

    return allSongs


if __name__ == "__main__":
    plt.close('all')

    # --- Ex2.1
    featuresFile = './Features - Audio MER/top100_features.csv'
    top100 = readFeatures(featuresFile)
    top100_N = normalization(top100)
    saveFeatures(featuresFile, top100_N)

    audioDir = 'MER_audio_taffc_dataset/audios/'
    allSongs = extracFeatures()

    """
    # --- Load file
    audioFile = "MER_audio_taffc_dataset/audios/MT0000414517.mp3"
    sr = 22050  # sampling rate
    mono = True
    y, fs = loadAudio(audioFile, sr, mono)

    # --- Play Sound
    # sd.play(y, sr, blocking=False)

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

    # plt.show()
    """
