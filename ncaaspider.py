import json
import matplotlib.pyplot as plt

def get_sec(time_str):
    m, s = time_str.split(':')
    return int(m) * 60 + int(s)

with open('/Users/willpride/ncaa/scoring.json') as data_file:
    data = json.load(data_file)
    playStats0 =  data["periods"][0]["playStats"]
    playStats1 = data["periods"][1]["playStats"]
    diffs = []
    times = []
    for stat in playStats0:
        if stat["score"]:
            sec = 20 * 60 + get_sec(stat["time"])
            score = stat["score"]
            split = score.split('-')
            diff = int(split[0]) - int(split[1])
            diffs.append(diff)
            times.append(sec)

    for stat in playStats1:
        if stat["score"]:
            sec = get_sec(stat["time"])
            score = stat["score"]
            split = score.split('-')
            diff = int(split[0]) - int(split[1])
            diffs.append(diff)
            times.append(sec)

            print "diffs ", diff, " times ", sec

    plt.plot(times, diffs, 'ro')
    plt.axis([0, 40 * 60, -20, 20])
    plt.show()


