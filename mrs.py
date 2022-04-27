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


def readFeatures(fileName):  # 2.1.1
    top100 = np.genfromtxt(fileName, delimiter=',')
    lines, columns = np.shape(top100)
    # print("dim ficheiro top100_features.csv original = %d x %d\n\n" % (lines, columns), top100)
    top100 = top100[1:, 1:(columns-1)]
    """lines, columns = np.shape(top100)
    print("\ndim top100 data = %d x %d\n\n" % (lines, columns), top100)
    print()"""
    return top100


def normalization(features):  # 2.1.2
    features_N = np.zeros(np.shape(features))
    columns = np.shape(features_N)[1]
    for i in range(columns):
        vmax = features[:, i].max()
        vmin = features[:, i].min()
        features_N[:, i] = (features[:, i] - vmin)/(vmax - vmin)
    # print(features_N)
    return features_N


def saveFeatures(fileName, features):  # 2.1.3
    # np.savetxt(fileName, features, fmt="%lf", delimiter=',')

    # checks if it's all good
    features = np.genfromtxt(fileName, delimiter=',')
    lines, columns = features.shape
    print("dim ficheiro %s = %d x %d\n\n" % (fileName, lines, columns), features)
    print()


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
    files.sort()    # sort the files alphabetically
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

        # Extract spectral centroid
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
    top100File = './Features - Audio MER/top100_features.csv'
    top100 = readFeatures(top100File)
    top100File_N = top100File.replace('.csv', '_normalized_data.csv')
    top100_N = normalization(top100)
    saveFeatures(top100File_N, top100_N)

    # --- Ex2.2
    audioDir = 'MER_audio_taffc_dataset/audios/'
    # allSongs = extracFeatures()
    # allSongs_N = normalization(allSongs)
    allSongsFile_N = './Features - Audio MER/All_features_normalized_data.csv'
    saveFeatures(allSongsFile_N, [])
