import torchaudio
# import torch
import torch
import augment
# import numpy as np
# import IPython.display as ipd
import os


def doWork(filename='test.wav'):
    # filename='test.wav'
    print(os.path.realpath(__file__))
    x, sr = torchaudio.load(filename)
    combination = augment.EffectChain().time_dropout(max_seconds=6)
    y = combination.apply(x, src_info={'rate': sr}, target_info={'rate': sr})
    print("This is it", os.path.dirname(os.path.realpath(__file__)))
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "FINAL.wav")
    # print("it is this", path)
    torchaudio.save(path, y, sample_rate=sr)
    # print(type(y))
    return y


# doWork()
# doWork()
# ipd.Audio(y, rate=sr)
