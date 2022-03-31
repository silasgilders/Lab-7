

def main():
    
    team_info = {
        'name': 'Maple Leafs',
        'city': 'Toronto',
        'players' : [
            'Campbell',
            'Matthews',
            'Bunting',
        ],
        'games' : [
            {'opponent' : 'Montreal',
            'goals_for': 2,
            'goals_against': 4
            },
            {'opponent' : 'Detroit',
            'goals_for': 6,
            'goals_against': 1
            }        
        
        ],


    }


    new_game = {'opponent': 'Boston', 'goals_for' : 9, 'goals_against' : 0}
    team_info['games'].append(new_game)

    new_game = {'opponent': 'Florida', 'goals_for' : 3, 'goals_against' : 2}
    team_info['games'].insert(1, new_game)
    
    new_players = ('Marner', 'Nylander', 'Giordano')
    add_new_players(team_info, new_players)

    print_game_opponents(team_info)
    #for g in team_info['games']:
        #print(g['opponent'])
    #full_name = "The " + team_info['city'] + ' ' + team_info['name']    
    #print(full_name)

    pass

def add_new_players(team, players):
    for p in players:
        team['players'].append(p)


def print_game_opponents(team_data):

    sentence = "The" + " " + team_data['city']+ ' ' + team_data['name'] + ' ' + "have played games against "

    for i,g in enumerate(team_data['games']):
        sentence += g['opponent']
        if i < len(team_data['games']) - 1:
            sentence += ', '
        else:
            sentence += '.'

    print(sentence)

main()