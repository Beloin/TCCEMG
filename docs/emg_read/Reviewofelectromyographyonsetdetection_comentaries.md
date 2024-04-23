# Review (2023)

[Article](https://pubmed.ncbi.nlm.nih.gov/37872633/) 

Has read 156 papers, the goal is to review state-of-art on EMG onset detection.

On-set time -> When muscle is really used
> [!IMPORTANT]
> There's latency on action between tendons and bones.
> This means that we can acctually have time to "calculate" and properly use external device as complement or substitute for body movements.

As mentioned: there is not a gold standard approach yet, hence the high numbers of articles. (See reference here too).
Again multiple algorithms that mostly do the same thing are use different nomenclatures, so this makes even harder to gather information about which is better.

Compares methods.

In fact, homologous, there's a international initiative to make eletromyography comes to a consensus in which we can study to check whenever they really
came to a consensus. Named as for experimental design in electromyography’ (CEDE project).

Database used: Scopus Database

Separeted in:

1. Reason:
 - Robotics
 - Clinical
 - Research
2. Detection Method:
 - Visual Inspection
 - Threshold based
 - Statistical 
 - Machine Learning
 - Others

# Pre-processing

1. Calculating EMG Envelope is the most common method.
2. Followed by TKEO method (Teager-Kaiser Energy Operator)
3. Wavelet Transform

## EMG Envelope

See also:

```
McManus L, Lowery M, Merletti R, Søgaard K, Besomi M, Clancy EA,
et al. Consensus for experimental design in electromyography (CEDE)
project: terminology matrix. J Electromyogr Kinesiol. 2021;59: 102565
```

According to the CEDE project, EMG envelope is a smooth curve that tracks changes in the amplitude of an EMG signal over time [8]. Calculating the EMG envelope is a pre-processing method that can be obtained in several ways.

Common approach:

1. Rectification followed by Moving average or Low-pass filtering (This approach is also used by `A fast and reliable technique for muscle activity detection from surface EMG signals`)
2. Moving RMS

### 1: Rectification and Low-pass

Mostly uses a discrete low-pass filter after a analogic Rectification. The most common is Butterworth filter

#### Moving Average

This is used to "Smooth" the EMG raw signal, so acting as a low-pass filter, so it can remove flutuations.
Inherently, the MA method adds a N values delay. It attenue rapid variations but keeps slow variations intact, so acting as a low-pass filter.


### 2: Moving RMS

Measures the signal's power. Uses the following calculation:

[Put calculation here].


## Teager-Kaiser Energy Operator

First proposed in 1982.

See:
```
Li X, Zhou P, Aruin AS. Teager-Kaiser energy operation of surface
EMG improves muscle activity onset detection. Ann Biomed Eng.
2007;35(9):1532–8.
```

Is applied to extract motor unit activaty by "making the action potential spikes sharper and narrower, enhancing the muscle activation points".

> Here we can look for the papers that use TKEO as pre-processor, since they achieve good results.

## Wavelet Transform

Also used in `A fast and reliable technique for muscle activity detection from surface EMG signals`.

There's other methods, but not as used as those three methods.

# On-set Detection methods

After Pre-processing we can apply methods to achieve onset.

As explained previosly, there's the Visual Inspection, Threshold-Based, Statistical and Machine Learning.



# Conclusions

This paper does not conclude much things about which is better. But this paper opened the mind to search for "Best hand sEMG onset detection".





