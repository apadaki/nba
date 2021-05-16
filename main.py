import plot, volume

mostbalanced = volume.get_volume_queue(22000500, 22001000, 0)
print('smallest volumes:')
for i in range(20):
    game = mostbalanced.get()
    plot.plot_trends(game.times_disc, game.diffs_disc, game.matchup, 'images/balanced/bal{}.jpg'.format(i), game.volume)
    print(game.volume)

mostlopsided = volume.get_volume_queue(22000500, 22001000, 1)
print('largest volumes:')
for i in range(20):
    game = mostlopsided.get()
    plot.plot_trends(game.times_disc, game.diffs_disc, game.matchup, 'images/lopsided/lop{}.jpg'.format(i), game.volume)
    print(game.volume)
