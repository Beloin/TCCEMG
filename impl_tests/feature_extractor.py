from math import log
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np
import extractor as ext
import pandas as pd

# Nonlinear measures for dynamic system
# import nodls


# |%%--%%| <KRXXGnMMAB|QcH1C2VbZC>

fbase = pd.read_csv('./1_filtered.csv', header=None)

# |%%--%%| <QcH1C2VbZC|IBSaTAkXwY>

extractor = ext.RecordExtractor()
cycles = extractor.read_sample(fbase)
len(cycles)

# |%%--%%| <IBSaTAkXwY|3YgVu9iRnr>
r"""°°°
Implement feature extractors:

1. SampEn - Sample Entropy
2. RMS - Root Mean Square
3. WL - Waveform Length
4. WAMP - Willison Amplitude
5. ApEn - Approximate entropy
6. MAV - Mean Absolute Value

°°°"""
# |%%--%%| <3YgVu9iRnr|4pPo6KQ1QC>
r"""°°°

# SampEn

Sample entropy (SampEn) is a modification of approximate entropy (ApEn), used for assessing the complexity of physiological time-series signals, diagnosing diseased states. SampEn has two advantages over ApEn: data length independence and a relatively trouble-free implementation.

°°°"""
# |%%--%%| <4pPo6KQ1QC|bSEp5543T3>


def construct_templates(timeseries_data: list, m: int = 2):
    num_windows = len(timeseries_data) - m + 1
    return [timeseries_data[x: x + m] for x in range(0, num_windows)]


def get_matches(templates: list, r: float):
    return len(
        list(filter(lambda x: is_match(
            x[0], x[1], r), combinations(templates, 2)))
    )


def is_match(template_1: list, template_2: list, r: float):
    return all([abs(x - y) < r for (x, y) in zip(template_1, template_2)])


def sample_entropy(timeseries_data: list, window_size: int, r: float):
    B = get_matches(construct_templates(timeseries_data, window_size), r)
    A = get_matches(construct_templates(timeseries_data, window_size + 1), r)
    return -log(A / B)

# |%%--%%| <bSEp5543T3|oJlYWSM7Hs>


fbase.head()

# |%%--%%| <oJlYWSM7Hs|yIJHBh1f9x>

# Cycles 4 Sensors with 5 Cycles
cycle_01 = cycles[0][0]
print(cycle_01)
print(len(cycle_01.grip))
cycle_01.grip.info()

# |%%--%%| <yIJHBh1f9x|Fv3Fn2slGu>

c_01std = np.std(cycle_01.grip)
cycle_01.grip.head()

# |%%--%%| <Fv3Fn2slGu|kh1XViUlqV>

sample_entropy(cycle_01.grip, 0.5*extractor._freq,
               c_01std)  # How to use withou integer?

# |%%--%%| <kh1XViUlqV|RTbV6qOJTj>
r"""°°°
# RMS - Root Mean Square 
Is the sum of all squared values, divided by the amount and made a square root
Also named as Effective Value

°°°"""
# |%%--%%| <RTbV6qOJTj|EfxF9lHnWe>

# Cycles 4 Sensors with 5 Cycles
cycle_01 = cycles[0][0]
print(cycle_01)
print(len(cycle_01.grip))
cycle_01.grip.info()

# |%%--%%| <EfxF9lHnWe|zHvvG2zHsf>


def rms(sample, window=200):
    return np.sqrt(np.mean(sample**2))

#|%%--%%| <zHvvG2zHsf|pI4OKMOq8t>

rms(cycle_01.grip)

#|%%--%%| <pI4OKMOq8t|ckJuZndQA1>

# Choose the range, or the window
rms(cycle_01.grip[:int(.2*extractor._freq)])

#|%%--%%| <ckJuZndQA1|We2ZiuwrQg>

data = []
names = []
for i in range(5):
    window_s = .2 * (i+1)
    window = window_s * extractor._freq
    data.append(rms(cycle_01.grip[:int(window)]))
    names.append("{0:0.2f}s".format(window_s))

data.append(rms(cycle_01.grip[:int(window)]))
names.append('{0:0.2f}s'.format(cycle_01.grip.__len__()/extractor._freq))
print(data)

    
plt.bar(names, data)


#|%%--%%| <We2ZiuwrQg|MtlNpD3ptX>
r"""°°°
Waveform Length
Waveform length is a measure of complexity of the EMG signal. It is defined as cumulative length of the EMG waveform over the time segment.

![Wave Formula](./wavelength_formula.png)
°°°"""
#|%%--%%| <MtlNpD3ptX|Sy0uAjQCNc>
import math

def waveformlen(sample):
    sum = 0
    for i in range(len(sample)-1):
        sum += math.fabs(sample[i+1] - sample[i])
    return sum

#|%%--%%| <Sy0uAjQCNc|0tkSgscJkZ>

waveformlen(np.array(cycle_01.grip[:int(.2*extractor._freq)]))

#|%%--%%| <0tkSgscJkZ|YWWrqNXR2S>

data = []
names = []
for i in range(5):
    window_s = .2 * (i+1)
    window = window_s * extractor._freq
    data.append(waveformlen(np.array(cycle_01.grip[:int(window)])))
    names.append("{0:0.2f}s".format(window_s))

data.append(waveformlen(np.array(cycle_01.grip[:int(window)])))
names.append('{0:0.2f}s'.format(cycle_01.grip.__len__()/extractor._freq))
print(data)
    
plt.bar(names, data)

# |%%--%%| <YWWrqNXR2S|GEDwmG2wVf>
