import math
from math import log
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np
import extractor as ext
import pandas as pd

# Nonlinear measures for dynamic system
# import nodls


#|%%--%%| <MhygeRZNUY|QcH1C2VbZC>

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

import nolds

nolds.sampen(cycle_01.grip[:int(.2*extractor._freq)])

#|%%--%%| <bSEp5543T3|uRqC8wpvIV>

data = []
names = []
for i in range(20):
    window_s = .2 * (i+1)
    window = window_s * extractor._freq
    data.append(nolds.sampen((cycle_01.grip[:int(window)])))
    names.append("{0:0.2f}s".format(window_s))

data.append(nolds.sampen(cycle_01.grip[:int(window)]))
names.append('{0:0.2f}s'.format(cycle_01.grip.__len__()/extractor._freq))
print(data)


plt.bar(names, data)


# |%%--%%| <uRqC8wpvIV|RTbV6qOJTj>
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

# |%%--%%| <zHvvG2zHsf|pI4OKMOq8t>


rms(cycle_01.grip)

# |%%--%%| <pI4OKMOq8t|ckJuZndQA1>

# Choose the range, or the window
rms(cycle_01.grip[:int(.2*extractor._freq)])

# |%%--%%| <ckJuZndQA1|We2ZiuwrQg>

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


# |%%--%%| <We2ZiuwrQg|MtlNpD3ptX>
r"""°°°
Waveform Length
Waveform length is a measure of complexity of the EMG signal. It is defined as cumulative length of the EMG waveform over the time segment.

![Wave Formula](./wavelength_formula.png)
°°°"""
# |%%--%%| <MtlNpD3ptX|Sy0uAjQCNc>


def waveformlen(sample):
    sum = 0
    for i in range(len(sample)-1):
        sum += math.fabs(sample[i+1] - sample[i])
    return sum

# |%%--%%| <Sy0uAjQCNc|0tkSgscJkZ>


waveformlen(np.array(cycle_01.grip[:int(.2*extractor._freq)]))

#|%%--%%| <0tkSgscJkZ|IftIPSWAmT>

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

# |%%--%%| <IftIPSWAmT|INpH9OwTFZ>
r"""°°°
# Willison Amplitude
Willison  amplitude  (WAMP)  is  the  number  of counts  for  each  change  in  the  EMG  signal amplitude  that  exceeds  a  predefine threshold

![wamp](./wamp.png)
°°°"""
# |%%--%%| <INpH9OwTFZ|gXh8hBUUkY>


def wamp(sample, threshold=10):
    """
    @param: sample - Sample based on volts
    @param: threshold - Based on milivolts
    """
    threshold /= 1000
    sum = 0
    for i in range(len(sample)-1):
        v = math.fabs(sample[i] - sample[i+1])
        if v > threshold:
            sum += 1
    return sum


#|%%--%%| <gXh8hBUUkY|k9YNHRMXNc>

plt.plot(cycle_01.grip[:int(.2*extractor._freq)])

#|%%--%%| <k9YNHRMXNc|zZNXRDd2WV>

wamp(np.array(cycle_01.grip[:int(.2*extractor._freq)]))

# |%%--%%| <zZNXRDd2WV|YWWrqNXR2S>

data = []
names = []
for i in range(5):
    window_s = .2 * (i+1)
    window = window_s * extractor._freq
    data.append(wamp(np.array(cycle_01.grip[:int(window)])))
    names.append("{0:0.2f}s".format(window_s))

data.append(wamp(np.array(cycle_01.grip[:int(window)])))
names.append('{0:0.2f}s'.format(cycle_01.grip.__len__()/extractor._freq))
print(data)

plt.bar(names, data)

#|%%--%%| <YWWrqNXR2S|PHUZqmqvOl>
r"""°°°
# Approximate Entropy
ApEn, technique used to quantify the amount of regularity and the unpredictability of fluctuations over time-series data.

The approximate entropy explains the complexity of the irregularity, quantifies how predictible the values of a time series are.
°°°"""
#|%%--%%| <PHUZqmqvOl|CwwddfAmvg>

import EntropyHub as EH

EH.ApEn(cycle_01.grip[:int(.2*extractor._freq)]) # Won't work, don't know why

#|%%--%%| <CwwddfAmvg|0NP8vgSuEN>

import antropy as an

an.app_entropy(cycle_01.grip[:int(.2*extractor._freq)]) # Slow

#|%%--%%| <0NP8vgSuEN|sL8IwFU5yR>

data = []
names = []
for i in range(20):
    window_s = .2 * (i+1)
    window = window_s * extractor._freq
    data.append(an.app_entropy(np.array(cycle_01.grip[:int(window)])))
    names.append("{0:0.2f}s".format(window_s))

data.append(an.app_entropy(np.array(cycle_01.grip[:int(window)])))
names.append('{0:0.2f}s'.format(cycle_01.grip.__len__()/extractor._freq))
print(data)

plt.bar(names, data)

#|%%--%%| <sL8IwFU5yR|zVhDhiQEia>
r"""°°°
MAV - Mean Absolute Value
Measures the contraction level of muscles.
 
Does't looks promising

![MAV](./mav.png)
°°°"""
#|%%--%%| <zVhDhiQEia|X0SwFcaUiE>

def mav(sample):
    return sum(sample)/len(sample)

#|%%--%%| <X0SwFcaUiE|b8UulLYmfd>

mav(cycle_01.grip[:int(.2*extractor._freq)])

#|%%--%%| <b8UulLYmfd|G9YrSgN2qE>

data = []
names = []
for i in range(20):
    window_s = .2 * (i+1)
    window = window_s * extractor._freq
    data.append(mav(np.array(cycle_01.grip[:int(window)])))
    names.append("{0:0.2f}s".format(window_s))

data.append(mav(np.array(cycle_01.grip[:int(window)])))
names.append('{0:0.2f}s'.format(cycle_01.grip.__len__()/extractor._freq))
print(data)

plt.bar(names, data)

#|%%--%%| <G9YrSgN2qE|Uu6tDABCVG>



# |%%--%%| <Uu6tDABCVG|GEDwmG2wVf>
