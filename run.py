import calculate
import team_comps


user_input = []


def get_user_input():
    user_input_string = input("What champions do you have?")
    if '-' in user_input_string:
        team_comps.delete_champ(user_input_string)
    else:
        team_comps.add_champ(user_input_string)
    calculate.match(user_input, team_comps.tier_S)


while 1:
    team_comps.get_team_data()
    get_user_input()
