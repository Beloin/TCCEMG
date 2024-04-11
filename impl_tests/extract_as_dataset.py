r"""°°°
# Dataset for multi-channel surface electromyography (sEMG) signals of hand gestures

[Link](https://pdf.sciencedirectassets.com/311593/1-s2.0-S2352340922X00024/1-s2.0-S2352340922001330/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCUfold3%2BqkxQ13HfLNWyigkHJoqGWAh%2BBIRWbJv8D%2FDAIhAJippklkKHAk3KzgDtI%2FLQIwBNtlTHAoXl4OrEWnmJHYKrIFCDgQBRoMMDU5MDAzNTQ2ODY1IgzFZy2pCgtizItvnsYqjwVNQGQ8Qm3eqEQJYPbtE1XyXnRIDqCu%2BnNSu%2BfvSKltNaBnQerrbK23rCCBuNcYwqzeGXB%2Bgb5y1bzl2Z%2BtifmjtPmeR2svCwrgNrOJ%2FMoHJholvfzW1tbRKsBRqmLD%2FuH630Kwzn8KZ8%2FeuBc990JO7Gs5oOH6eXvd2Y%2B2GsBBMGv5X4f6arW07ly26vh9YHEjeoI1tAXFs%2FDnhD6a1nGWFx3GFrr8dcksi%2BtJPNSrD%2FebzIPGNf9k%2FCb%2F9p4O38666yHWBziZrtY91ZsY7ROnaSN93W5orQX3l7M9T1Rk62LnEezwa1oMyfV7icE8aj4%2BS69bOAQsEWws8FPyRzGAemL7UT1Jz1OmXozgvhVq5KAv8VhVeWdaVgWGjTINh8zp9v7FbeC9zkQKcuoF8B5dW2%2BNn6bHTMpXDMF91bgeTXTfSTCRZo46ZFiHmJy9YXiof77G5EiGxyhKxzvPo1elqr6VC9ld9FpDecLaj%2FguX6MIWYAMqy4OI4Vvz4UVFtYlv5RWqGFJwK7b7%2FBzwi4OEWWwz8WkwZVx3m2Uqu8KHAmYMqOAlCLYHRYXB7f6LpqB%2FqL0uWd3nPB04elu%2B1MyTpTa%2Bv5noSzr0FtnRr7k8484EPCJue%2F8g1kpjECHER9L%2F8yUvkLraxLdB8h%2FfpWoQMhrntdm4YCHYscG9401qrYWdzr6K6JPkQMONex7mpwGG9nGim7lq2JmT8PVvv6y7A3LjJvAIkEoFlEDU3Yy0fn1SsGLjRsZYenDAQyTwj9YQZw8Y3vyKIGsSf4siKZa%2FMNuL2eXwGrBMzfQBfLzk%2Bb05wXtpYo%2B5p%2FaiXN1snmW5nwK129kLo%2F83hO2l%2BIHrUKDwDU%2BHD%2F1scBSVjh%2FMP6y3LAGOrABFIlTwbZNid4kexTbJFoIgc1McjB7nFhuKYFVJdcWsqwrs2f%2FDZVUofXy%2BzlPCat8pjqCZTG%2Fnc3J%2FpkFnZq9EocneeGabfpfT1t7iGlk%2FfDQEeXpminuYCn2Z%2FEWBnqopMCN7Wh2zkLsYG5EYbGpUCUvSV%2Fy%2FHxCtRwBxnTox%2BEgrATcegpC6j%2FptBGHR8ENccK72nSKKlNTtHFaN4PnlLskOf4qwRouv9rbnhXN0Bs%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240410T231256Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTY6ZPUK4NJ%2F20240410%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=8d20dd03f36e3e369082aeb3c9a62c51b8e19df531bed6c76265ced367e0c953&hash=4e984a20e3c0de9cddae4cd36e1389c07b90de664e84115cdde03c63c114dea8&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S2352340922001330&tid=spdf-5d99dfee-4f0d-4b63-8cb0-05ab4986c6f2&sid=f5ca53635089b042106a7be1718ff3abfb07gxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=18145c535c52520c010b04&rr=87266caedded15b9&cc=br)

This EDA is made to extract EMG signals by class from the current dataset.
°°°"""
#|%%--%%| <jCPW9iYtqp|9aYFr1Xldj>

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#|%%--%%| <9aYFr1Xldj|oxpHeyNWqk>

base = pd.read_csv("./1_raw.csv", header=None)
fbase = pd.read_csv("./1_filtered.csv", header=None)
base.describe()

#|%%--%%| <oxpHeyNWqk|r4Kq6UKHKy>

plt.plot(base.iloc[:100,0])

#|%%--%%| <r4Kq6UKHKy|B8Xs5xTtDQ>

plt.plot(fbase.iloc[:1000,0])

#|%%--%%| <B8Xs5xTtDQ|IFoxyFk8cR>
r"""°°°
# Data specs

2kHz sample rate

| Raw and filtered

Filtered:
    - sixth-order Butterworth bandpass filter with a frequency range of 5–500 Hz
    - second-order notch filter at 50 Hz for the elimination of noises like motion artifacts, high-frequency noise, and power line interference

So probably we will need to use our own filter to use the notch filter with 60Hz and add Butterworth when acquiring our data.
°°°"""
#|%%--%%| <IFoxyFk8cR|MaBALBz83P>


#|%%--%%| <MaBALBz83P|hcjq3VbSL1>



#|%%--%%| <hcjq3VbSL1|Z7LE0G4TrZ>

