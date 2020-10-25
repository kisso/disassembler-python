import json


def mips_decoder(x):
    if isinstance(x, dict):
        new_dict = {}
        for k, v in x.items():
            try:
                new_dict[int(k)] = v
            except ValueError:
                new_dict[k] = v

                if isinstance(v, str) and v.startswith('0b'):
                    new_dict[k] = int(v, 2)

        return new_dict

    return x


def load_file(path: str):
    with open(file=path) as f:
        return f.read().splitlines()


def load_json(path: str):
    with open(file=path) as json_file:
        return json.load(json_file, object_hook=mips_decoder)
