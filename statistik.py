class Statistik:
    def __init__(self, data):
        self.data = set(data)

    def mean(self):
        try:
            total = sum(self.data)
            count = len(self.data)
            mean = (total / count)
            return mean
        except TypeError as e:
            raise TypeError(f"Data harus berupa list.") from e

    def median(self):
        try:
            data_urut = sorted(self.data)
            n = len(data_urut)
            if n % 2 == 0:
                return (data_urut[n // 2] + data_urut[n // 2 - 1]) / 2
            else:
                return data_urut[n // 2]
        except TypeError as e:
            raise TypeError(f"Data harus berupa list.") from e

    def modus(self):
        try:
            data_unik = set(self.data)
            frekuensi = {i: 0 for i in data_unik}

            for i in data_unik:
                frekuensi[i] += 1

            frekuensi_max = max(frekuensi, key=frekuensi.get)
            return frekuensi_max
        except TypeError as e:
            raise TypeError(f"Data harus berupa list.") from e
        