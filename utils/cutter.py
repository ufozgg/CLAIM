import os
import json
import thulac

cutter = thulac.thulac(seg_only=True)
frequency = {}

path_list = [
    ["/home/zhangjunqi/zrz/legal/data",
     "/home/zhangjunqi/zrz/legal/data_cutted"],
]


def cut(s):
    arr = list(cutter.fast_cut(s))
    for a in range(0, len(arr)):
        arr[a] = arr[a][0]
    for word in arr:
        if not (word in frequency):
            frequency[word] = 0
        frequency[word] += 1
    return arr


if __name__ == "__main__":
    for input_path, output_path in path_list:
        os.makedirs(output_path, exist_ok=True)
        for filename in os.listdir(input_path):
            print(os.path.join(input_path, filename))
            data = []

            f = open(os.path.join(input_path, filename), "r", encoding="utf8")

            for line in f:
                x = json.loads(line)
                x["fact"] = cut(x["fact"])

                data.append(x)

            f = open(os.path.join(output_path, filename), "w", encoding="utf8")
            for x in data:
                print(json.dumps(x, ensure_ascii=False, sort_keys=True), file=f)
            f.close()

    json.dump(frequency, open("/home/zhangjunqi/zrz/legal/data/ljp/frequency.txt", "w", encoding="utf8"),
              indent=2,
              ensure_ascii=False)
