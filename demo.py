import torchaudio
import torch
import torch
import augment
import numpy as np
import IPython.display as ipd

x, sr = torchaudio.load('test.wav')
combination = augment.EffectChain().time_dropout(max_seconds=1.0)
y = combination.apply(x, src_info={'rate': sr}, target_info={'rate': sr})
ipd.Audio(y, rate=sr)
