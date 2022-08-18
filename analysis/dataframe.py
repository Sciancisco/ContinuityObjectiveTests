
class DataFrame:

    def __init__(self, *keys):
        self._keys = keys
        self._data = []

    def _select(self, **keywords):
        if (result := set(keywords.keys()) - set(self._keys)) != set():
            raise KeyError(f"Invalid keys {result}. Keys must be in {set(self._keys)}.")

        out = []
        for keys, data in self._data:
            select = True
            for key, value in keywords.items():
                if keys[key] != value:
                    select = False
                    break
            if select:
                out.append(data)

        return out

    def __call__(self, **keywords):
        return self._select(**keywords)

    def add(self, data, **kwargs):
        if set(kwargs.keys()) != set(self._keys):
            raise KeyError(f"Keys must match {set(self._keys)}.")

        d = dict.fromkeys(self._keys)
        for key, value in kwargs.items():
            d[key] = value

        self._data.append((d, data))