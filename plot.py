import parse
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms

print('enter game id (see www.nba.com)')
matchup, plays = parse.get_info_from_id(input())
size = len(plays)

times = []
diffs = []
times_disc = [0]
diffs_disc = [0]
current_time = 0
disc_interval = 60
assert(disc_interval >= 0.1)
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
            current_time += disc_interval
            times_disc.append(current_time)
            diffs_disc.append(differential)
   

times = times_disc
diffs = diffs_disc

fig,ax = plt.subplots()
plt.plot(times, diffs, 'b', lw=1)

xtrans = ax.get_xaxis_transform()
plt.axhline(y=0, color='black', linestyle='--', alpha=0.6)
plt.axvline(x=12*60, color='g', linestyle='--', alpha=0.3)
plt.axvline(x=24*60, color='g', linestyle='--', alpha=0.3)
plt.axvline(x=36*60, color='g', linestyle='--', alpha=0.3)  
plt.axvline(x=48*60, color='g', linestyle='-', lw=2)
plt.text(6*60,  0.01, '(Q1)', transform=xtrans, color='r', ha='center')
plt.text(18*60, 0.01, '(Q2)', transform=xtrans, color='r', ha='center')
plt.text(30*60, 0.01, '(Q3)', transform=xtrans, color='r', ha='center')
plt.text(42*60, 0.01, '(Q4)', transform=xtrans, color='r', ha='center')

ax.tick_params(labelright=True)


plt.xlim(xmin=0,xmax=max(48*60, max(times)))
plt.xlabel('in-game time elapsed (s)')
plt.ylabel('(home-away) point differential')
plt.title('Game Trends: {}'.format(matchup))
plt.savefig('images/diffs.jpg')
