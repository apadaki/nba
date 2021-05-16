# NBA Game Visualization Tool (unfinished)

This tool scrapes through www.nba.com/[game-id-number]/play-by-play to display score change trends cleanly. It also computes the average point differential between the teams over the course of the game. This can be used to find the **N** most balanced matches/most lopsided matches within a sequential range of NBA games.

## Usage

Run [main.py](main.py) with an appropriate directory structure and tweak the game range if necessary.

## Example

This is a generated score-change graph from a game between Utah and Houston on 05/08/2021. The `avg_diff` textbox means that on average, Utah led this match by 8.86 points. 

![example graph](ex1.jpg)