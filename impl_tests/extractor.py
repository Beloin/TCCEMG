class Cycle:
    rest = []
    extension = []
    flexion = []
    ulnar_deviation = []
    radial_deviation = []
    grip = []
    finger_abduction = []
    finger_adduction = []
    supination = []
    pronation = []


class RecordExtractor(object):

    _freq = None

    def __init__(self, freq=2000):
        self._freq = freq

    def read_sample(self, samples):
        """ samples should be a Dataframe with 4 columns"""
        cycles = []
        for i in range(4):
            cycles.append([])
            for j in range(5):
                nc = self.read_cycle(j, samples.iloc[:, i])
                cycles[i].append(nc)

        return cycles

    # Cycle starts with 0
    def read_cycle(self, n, sample):
        print(len(sample))
        offset = n*(104 * self._freq) + n*(30 * self._freq)
        offsample = sample[offset:]

        c = Cycle()

        # 0°
        # c.rest = offsample[self.sec(4):self.sec(6)]
        c.rest = self.read_nthc(0, offsample)
        c.extension = self.read_nthc(1, offsample)
        c.flexion = self.read_nthc(2, offsample)
        c.ulnar_deviation = self.read_nthc(3, offsample)
        c.radial_deviation = self.read_nthc(4, offsample)
        c.grip = self.read_nthc(5, offsample)
        c.finger_abduction = self.read_nthc(6, offsample)
        c.finger_adduction = self.read_nthc(7, offsample)
        c.supination = self.read_nthc(8, offsample)
        c.pronation = self.read_nthc(9, offsample)

        return c

    def read_nthc(self, n, sample):
        offset = self.sec(4) + n*(self.sec(6) + self.sec(4))
        return sample[offset:offset + self.sec(6)]

    def sec(self, s):
        return s * self._freq
