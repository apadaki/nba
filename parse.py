import requests, json

def get_info_from_id(id):
    url = 'https://www.nba.com/game/{}/play-by-play'.format(id)
    response = requests.get(url)
    raw_html = response.text

    matchup_token = '\"gameMatchup\":\"'
    matchup_index_left = raw_html.index(matchup_token) + len(matchup_token)
 
    matchup_index_right = matchup_index_left
    while (raw_html[matchup_index_right] != '\"'):
        matchup_index_right+=1
    
    matchup = raw_html[matchup_index_left:matchup_index_right]

    start = "\"actions\":["
    end = '],\"source\":'
    start_index = raw_html.index(start)
    sub_left = raw_html[start_index:]
    end_index = sub_left.index(end) + 1
    plays_raw = '{' + sub_left[:end_index] + '}'

    with open('debug.txt', 'w') as f:
        print(raw_html, file=f)
    
    plays = json.loads(plays_raw)["actions"]
    return matchup, plays