import parse
from queue import PriorityQueue
from functools import total_ordering
import time

@total_ordering # for use in PriorityQueue
class GameNode:
    def __init__(self, id, max=0):
        self.id = id
        self.times = []
        self.diffs = []
        self.times_inter = []
        self.diffs_inter = []
        self.volume = 0
        self.matchup = ''
        self.max = max
    def __repr__(self):
        return 'GameNode(id={})'.format(self.id)
    def set_matchup(self, matchup):
        self.matchup = matchup
    def set_times_and_diffs(self, times, diffs, times_inter, diffs_inter):
        self.times = times
        self.diffs = diffs
        self.times_inter = times_inter
        self.diffs_inter = diffs_inter
        self.volume = total_volume(self.times, self.diffs) / times[-1]
    def __gt__(self, other):
        val = abs(self.volume) > abs(other.volume)
        if self.max:
            return (not val)
        return val
    def __eq__(self, other):
        return abs(self.volume) == abs(other.volume)

def total_volume(times, diffs):
    vol = 0
    for i in range(0,len(times)-1):
        vol += diffs[i]*(times[i+1]-times[i])
    return vol

def times_and_diffs_only(id):
    matchup, plays = parse.get_info_from_id(id)
    size = len(plays)

    times = []
    diffs = []
    times_inter = [0]
    diffs_inter = [0]
    current_time = 0
    time_interval = 60
    assert(time_interval >= 0.1)
    for i in range(size):
        if plays[i]['scoreHome']:
            differential = int(plays[i]['scoreHome']) - int(plays[i]['scoreAway'])

            # reformat clock
            time = plays[i]['clock']
            period = plays[i]['period']
            period_offset = (min(4, period-1))*12*60 + (max(0, period-5))*5*60 # 12-minute quarters, 5-minute OTs
            period_length = 12*60 if period <= 4 else 5*60
            minutes = int(time[2:4])
            seconds = float(time[5:10])
            elapsed = period_offset + period_length - (60*minutes + seconds)
            
            # data append
            times.append(elapsed)       
            diffs.append(differential)

            # discrete data append
            while current_time < elapsed:
                current_time += time_interval
                times_inter.append(current_time)
                diffs_inter.append(differential)
    return times, diffs, times_inter, diffs_inter
def times_and_diffs(game):
    matchup, plays = parse.get_info_from_id(game.id)
    game.set_matchup(matchup)
    size = len(plays)

    times = []
    diffs = []
    times_inter = [0]
    diffs_inter = [0]
    current_time = 0
    time_interval = 60
    assert(time_interval >= 0.1)
    for i in range(size):
        if plays[i]['scoreHome']:
            differential = int(plays[i]['scoreHome']) - int(plays[i]['scoreAway'])

            # reformat clock
            time = plays[i]['clock']
            period = plays[i]['period']
            period_offset = (min(4, period-1))*12*60 + (max(0, period-5))*5*60 # 12-minute quarters, 5-minute OTs
            period_length = 12*60 if period <= 4 else 5*60
            minutes = int(time[2:4])
            seconds = float(time[5:10])
            elapsed = period_offset + period_length - (60*minutes + seconds)
            
            # data append
            times.append(elapsed)       
            diffs.append(differential)

            # discrete data append
            while current_time < elapsed:
                current_time += time_interval
                times_inter.append(current_time)
                diffs_inter.append(differential)
    
    game.set_times_and_diffs(times, diffs, times_inter, diffs_inter)
    return game


def get_volume_queue(start_id, end_id, max=0):
    q = PriorityQueue()
    id = start_id
    max_vol = 0
    while (id <= end_id):
        print(id)
        game = GameNode('00'+str(id), max)
        game = times_and_diffs(game)
        q.put(game)
        id += 1
    return q
