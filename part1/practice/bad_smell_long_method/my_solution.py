csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_user_list() -> dict:
    data = _read(csv)
    sorted = _sort(data)
    return _filter(sorted)


def _read(strs):
    result = strs.replace(";", "\n").split("\n")
    return {result[i]: result[i + 1] for i in range(0, len(result), 2)}


def _sort(data):
    return sorted(data.items(), key=lambda t: int(t[1]))


def _filter(dicts):
    return {x[0]: x[1] for x in dicts if int(x[1]) > 10}


print(get_user_list())
