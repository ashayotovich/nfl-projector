import random
import pandas as pd


class Team(object):
    def __init__(self, team_name, off_run_avg, off_run_std, off_fum_rate,
                 off_pass_rate, off_comp_pct, off_comp_pass_avg, off_comp_pass_std, off_int_rate,
                 off_kick_rate, off_punt_avg, off_punt_std, fg_pct,
                 def_run_avg, def_run_std, def_fum_rate,
                 def_pass_rate, def_comp_pct, def_comp_pass_avg, def_comp_pass_std, def_int_rate,
                 def_kick_rate, def_punt_avg, def_punt_std, off_play_per_game, def_play_per_game):
        self.team_name = team_name
        self.off_run_avg = off_run_avg
        self.off_run_std = off_run_std
        self.off_fum_rate = off_fum_rate
        self.off_pass_rate = off_pass_rate
        self.off_comp_pct = off_comp_pct
        self.off_comp_pass_avg = off_comp_pass_avg
        self.off_comp_pass_std = off_comp_pass_std
        self.off_int_rate = off_int_rate
        self.off_kick_rate = off_kick_rate
        self.off_punt_avg = off_punt_avg
        self.off_punt_std = off_punt_std
        self.fg_pct = fg_pct
        self.def_run_avg = def_run_avg
        self.def_run_std = def_run_std
        self.def_fum_rate = def_fum_rate
        self.def_pass_rate = def_pass_rate
        self.def_comp_pct = def_comp_pct
        self.def_comp_pass_avg = def_comp_pass_avg
        self.def_comp_pass_std = def_comp_pass_std
        self.def_int_rate = def_int_rate
        self.def_kick_rate = def_kick_rate
        self.def_punt_avg = def_punt_avg
        self.def_punt_std = def_punt_std
        self.off_play_per_game = off_play_per_game
        self.def_play_per_game = def_play_per_game
        self.off_play_per_half = int(self.off_play_per_game / 2)
        self.def_play_per_half = int(self.def_play_per_game / 2)
        self.plays = 0
        self.score = 0


class Yardline(object):
    def __init__(self, df, yard):
        self.run_score_rate = df['run_td_rate'][yard - 1]
        self.run_no_score_rate = 1 - self.run_score_rate

        self.pass_score_rate = df['pass_td_rate'][yard - 1]
        self.pass_no_score_rate = 1 - self.pass_score_rate


team_data = pd.read_csv("data_dictionary.csv")
scoring_rates = pd.read_csv("score_rate_dictionary.csv")


def ProjectGame(a, b, i=1, j=1):
    team_a = Team(team_data['team'][a], team_data['off_run_avg'][a], team_data['off_run_std'][a],
                  team_data['off_fum_rate'][a], team_data['off_pass_rate'][a], team_data['off_comp_pct'][a],
                  team_data['off_comp_pass_avg'][a], team_data['off_comp_pass_std'][a], team_data['off_int_rate'][a],
                  team_data['off_kick_rate'][a], team_data['off_punt_avg'][a], team_data['off_punt_std'][a],
                  team_data['fg_pct'][a], team_data['def_run_avg'][a], team_data['def_run_std'][a],
                  team_data['def_fum_rate'][a], team_data['def_pass_rate'][a], team_data['def_comp_pct'][a],
                  team_data['def_comp_pass_avg'][a], team_data['def_comp_pass_std'][a], team_data['def_int_rate'][a],
                  team_data['def_kick_rate'][a], team_data['def_punt_avg'][a], team_data['def_punt_std'][a],
                  team_data['off_play_per_game'][a], team_data['def_play_per_game'][a])

    team_b = Team(team_data['team'][b], team_data['off_run_avg'][b], team_data['off_run_std'][b],
                  team_data['off_fum_rate'][b], team_data['off_pass_rate'][b], team_data['off_comp_pct'][b],
                  team_data['off_comp_pass_avg'][b], team_data['off_comp_pass_std'][b], team_data['off_int_rate'][b],
                  team_data['off_kick_rate'][b], team_data['off_punt_avg'][b], team_data['off_punt_std'][b],
                  team_data['fg_pct'][b], team_data['def_run_avg'][b], team_data['def_run_std'][b],
                  team_data['def_fum_rate'][b], team_data['def_pass_rate'][b], team_data['def_comp_pct'][b],
                  team_data['def_comp_pass_avg'][b], team_data['def_comp_pass_std'][b], team_data['def_int_rate'][b],
                  team_data['def_kick_rate'][b], team_data['def_punt_avg'][b], team_data['def_punt_std'][b],
                  team_data['off_play_per_game'][b], team_data['def_play_per_game'][b])

    off_factor = 0.5
    def_factor = 1 - off_factor
    team_a.off_run_avg = (off_factor * team_a.off_run_avg + def_factor * team_b.def_run_avg)
    team_a.off_run_std = (off_factor * team_a.off_run_std + def_factor * team_b.def_run_std)
    team_a.off_fum_rate = (off_factor * team_a.off_fum_rate + def_factor * team_b.def_fum_rate)
    team_a.off_pass_rate = (off_factor * team_a.off_pass_rate + def_factor * team_b.def_pass_rate)
    team_a.off_comp_pct = (off_factor * team_a.off_comp_pct + def_factor * team_b.def_comp_pct)
    team_a.off_comp_pass_avg = (off_factor * team_a.off_comp_pass_avg + def_factor * team_b.def_comp_pass_avg)
    team_a.off_comp_pass_std = (off_factor * team_a.off_comp_pass_std + def_factor * team_b.def_comp_pass_std)
    team_a.off_int_rate = (off_factor * team_a.off_int_rate + def_factor * team_b.def_int_rate)
    team_a.off_kick_rate = (off_factor * team_a.off_kick_rate + def_factor * team_b.def_kick_rate)
    team_a.off_punt_avg = (off_factor * team_a.off_punt_avg + def_factor * team_b.def_punt_avg)
    team_a.off_punt_std = (off_factor * team_a.off_punt_std + def_factor * team_b.def_punt_std)
    team_a.off_play_per_half = (off_factor * team_a.off_play_per_half + def_factor * team_b.def_play_per_half)
    team_a.off_play_per_game = (off_factor * team_a.off_play_per_game + def_factor * team_b.def_play_per_game)

    team_b.off_run_avg = (off_factor * team_b.off_run_avg + def_factor * team_a.def_run_avg)
    team_b.off_run_std = (off_factor * team_b.off_run_std + def_factor * team_a.def_run_std)
    team_b.off_fum_rate = (off_factor * team_b.off_fum_rate + def_factor * team_a.def_fum_rate)
    team_b.off_pass_rate = (off_factor * team_b.off_pass_rate + def_factor * team_a.def_pass_rate)
    team_b.off_comp_pct = (off_factor * team_b.off_comp_pct + def_factor * team_a.def_comp_pct)
    team_b.off_comp_pass_avg = (off_factor * team_b.off_comp_pass_avg + def_factor * team_a.def_comp_pass_avg)
    team_b.off_comp_pass_std = (off_factor * team_b.off_comp_pass_std + def_factor * team_a.def_comp_pass_std)
    team_b.off_int_rate = (off_factor * team_b.off_int_rate + def_factor * team_a.def_int_rate)
    team_b.off_kick_rate = (off_factor * team_b.off_kick_rate + def_factor * team_a.def_kick_rate)
    team_b.off_punt_avg = (off_factor * team_b.off_punt_avg + def_factor * team_a.def_punt_avg)
    team_b.off_punt_std = (off_factor * team_b.off_punt_std + def_factor * team_a.def_punt_std)
    team_b.off_play_per_half = (off_factor * team_b.off_play_per_half + def_factor * team_a.def_play_per_half)
    team_b.off_play_per_game = (off_factor * team_b.off_play_per_game + def_factor * team_a.def_play_per_game)

    game_teams = [team_a, team_b]
    kickoff_receive = random.choice(game_teams)
    print(f"\nKICKOFF of GAME {i} of {j}"
          f"\n{kickoff_receive.team_name} to Receive Opening Kick\n")

    poss_team = kickoff_receive
    if poss_team == team_a:
        def_team = team_b
    else:
        def_team = team_a

    first_half = True
    second_half = False

    def TogglePossession(possession_team):

        if possession_team.team_name == team_a.team_name:
            possession_team = team_b
            defensive_team = team_a
        else:
            possession_team = team_a
            defensive_team = team_b

        return defensive_team, possession_team

    def YardConverter(current_yard):

        global relative_yard
        if current_yardline < 50:
            relative_yard = f"OPP {current_yard}"
        elif current_yardline > 50:
            relative = 100 - current_yardline
            relative_yard = f"OWN {relative}"
        return relative_yard

    current_yardline = 75
    down = 1
    distance = 10
    td_play = ['TD', 'No TD']
    pass_run = ['Pass', 'Run']
    fumble_play = ['Fumble', 'No Fumble']
    int_play = ['INT', 'No INT']
    pass_play = ['Pass Complete', 'Pass Incomplete']
    kick_made = ['GOOD', 'MISSED']
    fourth_play = ['Kick', 'Go']

    while first_half:
        possession = True
        if poss_team.plays > int(poss_team.off_play_per_half):
            print(f"\nHALFTIME")
            print(f"{poss_team.team_name} {poss_team.score}     {def_team.team_name} {def_team.score}\n")
            print("-------------------------------------------------")
            first_half = False
            second_half = True
        else:
            while possession:
                poss_team.plays = poss_team.plays + 1
                if down in [1, 2, 3]:
                    play_type = random.choices(pass_run, [poss_team.off_pass_rate, (1 - poss_team.off_pass_rate)])
                    if current_yardline < 0:
                        td_result[0] = 'TD'
                    else:
                        pass
                    td_rate = Yardline(scoring_rates, current_yardline)
                    relative_yardline = YardConverter(current_yardline)

                    if play_type[0] == 'Pass':
                        td_result = random.choices(td_play, [td_rate.pass_score_rate, td_rate.pass_no_score_rate])
                        int_result = random.choices(int_play, [poss_team.off_int_rate, (1 - poss_team.off_int_rate)])
                        if int_result[0] == 'INT':
                            turnover = True
                            turnover_type = 'INT'
                        else:
                            turnover = False
                            turnover_type = None

                    else:
                        td_result = random.choices(td_play, [td_rate.run_score_rate, td_rate.run_no_score_rate])
                        fum_result = random.choices(fumble_play, [poss_team.off_fum_rate, (1 - poss_team.off_fum_rate)])
                        if fum_result[0] == 'Fumble':
                            turnover = True
                            turnover_type = 'Fumble'
                        else:
                            turnover = False
                            turnover_type = None

                    if td_result[0] == 'TD':

                        xp_result = random.choices(kick_made, [95, 5])
                        if xp_result[0] == 'GOOD':
                            poss_team.score = poss_team.score + 7
                        else:
                            poss_team.score = poss_team.score + 6

                        print(
                            f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                            f"TOUCHDOWN {play_type[0]} ({current_yardline} yards) - Extra Point {xp_result[0]}")
                        print(f"\n{poss_team.team_name} {poss_team.score}   {def_team.team_name} {def_team.score}\n")
                        down = 1
                        distance = 10
                        current_yardline = 75
                        def_team, poss_team = TogglePossession(poss_team)
                        possession = False

                    elif turnover:
                        print(
                            f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                            f"Turnover - {turnover_type}\n")
                        down = 1
                        current_yardline = 100 - current_yardline
                        if current_yardline <= 10:
                            distance = current_yardline
                        else:
                            distance = 10
                        def_team, poss_team = TogglePossession(poss_team)
                        possession = False

                    else:
                        if play_type[0] == 'Pass':
                            pass_type = random.choices(pass_play,
                                                       [poss_team.off_comp_pct, (1 - poss_team.off_comp_pct)])
                            if pass_type[0] == 'Pass Complete':
                                yardage_gained = int(
                                    random.normalvariate(poss_team.off_comp_pass_avg, poss_team.off_comp_pass_std))
                                play_rp = 'Pass COMPLETE'
                            else:
                                yardage_gained = 0
                                play_rp = 'Pass INCOMPLETE'

                        else:
                            yardage_gained = int(random.normalvariate(poss_team.off_run_avg, poss_team.off_run_std))
                            play_rp = 'Run'

                        print(
                            f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                            f"{play_rp} for {yardage_gained} yards")

                        if yardage_gained >= current_yardline:
                            xp_result = random.choices(kick_made, [95, 5])
                            if xp_result[0] == 'GOOD':
                                poss_team.score = poss_team.score + 7
                            else:
                                poss_team.score = poss_team.score + 6

                            print(
                                f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                f"TOUCHDOWN {play_rp} ({current_yardline} yards) - Extra Point {xp_result[0]}")
                            print(
                                f"\n{poss_team.team_name} {poss_team.score}   "
                                f"{def_team.team_name} {def_team.score}\n")
                            current_yardline = 75
                            distance = 10
                            def_team, poss_team = TogglePossession(poss_team)
                            possession = False
                        elif yardage_gained >= distance:
                            down = 1
                            current_yardline = current_yardline - yardage_gained
                            if current_yardline <= 10 and yardage_gained > distance:

                                distance = current_yardline

                            else:
                                distance = 10

                        elif (current_yardline - yardage_gained) > 99:
                            def_team.score = def_team.score + 2
                            print(
                                f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                f"SAFETY {play_type[0]} attempt for {yardage_gained} yards)")
                            print(
                                f"\n{poss_team.team_name} {poss_team.score}   {def_team.team_name} {def_team.score}\n")
                            current_yardline = 75
                            down = 1
                            distance = 10
                            def_team, poss_team = TogglePossession(poss_team)
                            possession = False

                        else:

                            down = down + 1
                            distance = distance - yardage_gained
                            current_yardline = current_yardline - yardage_gained

                else:
                    fourth_decision = random.choices(fourth_play,
                                                     [poss_team.off_kick_rate, (1 - poss_team.off_kick_rate)])
                    if fourth_decision[0] == 'Go':
                        play_type = random.choices(pass_run, [poss_team.off_pass_rate, (1 - poss_team.off_pass_rate)])
                        td_rate = Yardline(scoring_rates, current_yardline)
                        relative_yardline = YardConverter(current_yardline)

                        if play_type[0] == 'Pass':
                            td_result = random.choices(td_play, [td_rate.pass_score_rate, td_rate.pass_no_score_rate])
                            int_result = random.choices(int_play,
                                                        [poss_team.off_int_rate, (1 - poss_team.off_int_rate)])
                            if int_result[0] == 'INT':
                                turnover = True
                                turnover_type = 'INT'
                            else:
                                turnover = False
                                turnover_type = None

                        else:
                            td_result = random.choices(td_play, [td_rate.run_score_rate, td_rate.run_no_score_rate])
                            fum_result = random.choices(fumble_play,
                                                        [poss_team.off_fum_rate, (1 - poss_team.off_fum_rate)])
                            if fum_result[0] == 'Fumble':
                                turnover = True
                                turnover_type = 'Fumble'
                            else:
                                turnover = False
                                turnover_type = None

                        if td_result[0] == 'TD':

                            xp_result = random.choices(kick_made, [95, 5])
                            if xp_result[0] == 'GOOD':
                                poss_team.score = poss_team.score + 7
                            else:
                                poss_team.score = poss_team.score + 6

                            print(
                                f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                f"TOUCHDOWN {play_type[0]} ({current_yardline} yards) - Extra Point {xp_result[0]}")
                            print(
                                f"\n{poss_team.team_name} {poss_team.score}   {def_team.team_name} {def_team.score}\n")
                            down = 1
                            distance = 10
                            current_yardline = 75
                            def_team, poss_team = TogglePossession(poss_team)
                            possession = False

                        elif turnover:
                            print(
                                f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                f"Turnover - {turnover_type}\n")
                            down = 1
                            current_yardline = 100 - current_yardline
                            if current_yardline <= 10:
                                distance = current_yardline
                            else:
                                distance = 10
                            def_team, poss_team = TogglePossession(poss_team)
                            possession = False

                        else:
                            if play_type[0] == 'Pass':
                                pass_type = random.choices(pass_play,
                                                           [poss_team.off_comp_pct, (1 - poss_team.off_comp_pct)])
                                if pass_type[0] == 'Pass Complete':
                                    yardage_gained = int(
                                        random.normalvariate(poss_team.off_comp_pass_avg, poss_team.off_comp_pass_std))
                                    play_rp = 'Pass COMPLETE'
                                else:
                                    yardage_gained = 0
                                    play_rp = 'Pass INCOMPLETE'

                            else:
                                yardage_gained = int(random.normalvariate(poss_team.off_run_avg, poss_team.off_run_std))
                                play_rp = 'Run'

                            if yardage_gained >= distance:
                                down = 1
                                current_yardline = current_yardline - yardage_gained
                                if current_yardline <= 0:
                                    xp_result = random.choices(kick_made, [95, 5])
                                    if xp_result[0] == 'GOOD':
                                        poss_team.score = poss_team.score + 7
                                    else:
                                        poss_team.score = poss_team.score + 6

                                    print(
                                        f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                        f"TOUCHDOWN {play_rp} ({current_yardline} yards) - Extra Point {xp_result[0]}")
                                    print(
                                        f"\n{poss_team.team_name} {poss_team.score}   "
                                        f"{def_team.team_name} {def_team.score}\n")
                                    current_yardline = 75
                                    down = 1
                                    distance = 10
                                    def_team, poss_team = TogglePossession(poss_team)
                                    possession = False

                                elif current_yardline <= 10:
                                    print(
                                        f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                        f"{play_rp} for {yardage_gained} yards")
                                    distance = current_yardline

                                else:
                                    print(
                                        f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                        f"{play_rp} for {yardage_gained} yards")
                                    distance = 10

                            elif (current_yardline - yardage_gained) > 99:
                                def_team.score = def_team.score + 2
                                print(
                                    f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                    f"SAFETY {play_type[0]} attempt for {yardage_gained} yards)")
                                print(
                                    f"\n{poss_team.team_name} {poss_team.score}   "
                                    f"{def_team.team_name} {def_team.score}\n")
                                down = 1
                                current_yardline = 75
                                distance = 10
                                def_team, poss_team = TogglePossession(poss_team)
                                possession = False

                            else:
                                print(
                                    f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                    f"{play_rp} for {yardage_gained} yards - TURNOVER ON DOWNS\n")

                                down = 1
                                current_yardline = 100 - current_yardline + yardage_gained
                                if current_yardline <= 10:
                                    distance = current_yardline
                                else:
                                    distance = 10
                                def_team, poss_team = TogglePossession(poss_team)
                                possession = False
                    else:
                        if current_yardline <= 40:
                            kick_outcome = random.choices(kick_made, [poss_team.fg_pct, (1 - poss_team.fg_pct)])
                            fg_dist = current_yardline + 17
                            if kick_outcome[0] == 'GOOD':
                                poss_team.score = poss_team.score + 3
                                print(f"{poss_team.team_name} {down} and {distance}: {fg_dist} yard FG Attempt GOOD")
                                print(
                                    f"\n{poss_team.team_name} {poss_team.score}   "
                                    f"{def_team.team_name} {def_team.score}\n")
                                current_yardline = 75

                            else:
                                print(
                                    f"{poss_team.team_name} {down} and {distance}: {fg_dist} yard FG Attempt MISSED\n")
                                current_yardline = 100 - current_yardline - 7

                            down = 1
                            distance = 10
                            def_team, poss_team = TogglePossession(poss_team)
                            possession = False

                        else:
                            punt_yards = int(random.normalvariate(poss_team.off_punt_avg, poss_team.off_punt_std))
                            if punt_yards >= current_yardline:
                                relative_yardline_pre = YardConverter(current_yardline)
                                print(f"{poss_team.team_name} {down} and {distance} from {relative_yardline_pre}: "
                                      f"PUNTS {relative_yardline_pre} yards for TOUCHBACK\n")
                                down = 1
                                distance = 10
                                current_yardline = 80
                                def_team, poss_team = TogglePossession(poss_team)
                                possession = False

                            else:
                                relative_yardline_pre = YardConverter(current_yardline)
                                current_yardline = current_yardline - punt_yards
                                relative_yardline_post = YardConverter(current_yardline)
                                print(f"{poss_team.team_name} {down} and {distance} from {relative_yardline_pre}: "
                                      f"PUNTS {punt_yards} yards to {relative_yardline_post}\n")
                                down = 1
                                current_yardline = 100 - current_yardline
                                if current_yardline <= 10:
                                    distance = current_yardline
                                else:
                                    distance = 10
                                def_team, poss_team = TogglePossession(poss_team)
                                possession = False

    current_yardline = 75
    down = 1
    distance = 10
    if kickoff_receive == team_a:
        poss_team = team_b
    else:
        poss_team = team_a

    while second_half:
        possession = True
        if poss_team.plays > int(poss_team.off_play_per_game):
            print(f"\nFINAL SCORE - GAME {i} of {j}")
            print(f"{poss_team.team_name} {poss_team.score}     {def_team.team_name} {def_team.score}")
            second_half = False
        else:
            while possession:
                poss_team.plays = poss_team.plays + 1
                if down in [1, 2, 3]:
                    play_type = random.choices(pass_run, [poss_team.off_pass_rate, (1 - poss_team.off_pass_rate)])
                    if current_yardline < 0:
                        td_result[0] = 'TD'
                    else:
                        pass
                    td_rate = Yardline(scoring_rates, current_yardline)
                    relative_yardline = YardConverter(current_yardline)

                    if play_type[0] == 'Pass':
                        td_result = random.choices(td_play, [td_rate.pass_score_rate, td_rate.pass_no_score_rate])
                        int_result = random.choices(int_play, [poss_team.off_int_rate, (1 - poss_team.off_int_rate)])
                        if int_result[0] == 'INT':
                            turnover = True
                            turnover_type = 'INT'
                        else:
                            turnover = False
                            turnover_type = None

                    else:
                        td_result = random.choices(td_play, [td_rate.run_score_rate, td_rate.run_no_score_rate])
                        fum_result = random.choices(fumble_play, [poss_team.off_fum_rate, (1 - poss_team.off_fum_rate)])
                        if fum_result[0] == 'Fumble':
                            turnover = True
                            turnover_type = 'Fumble'
                        else:
                            turnover = False
                            turnover_type = None

                    if td_result[0] == 'TD':

                        xp_result = random.choices(kick_made, [95, 5])
                        if xp_result[0] == 'GOOD':
                            poss_team.score = poss_team.score + 7
                        else:
                            poss_team.score = poss_team.score + 6

                        print(
                            f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                            f"TOUCHDOWN {play_type[0]} ({current_yardline} yards) - Extra Point {xp_result[0]}")
                        print(f"\n{poss_team.team_name} {poss_team.score}   {def_team.team_name} {def_team.score}\n")
                        down = 1
                        distance = 10
                        current_yardline = 75
                        def_team, poss_team = TogglePossession(poss_team)
                        possession = False

                    elif turnover:
                        print(
                            f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                            f"Turnover - {turnover_type}\n")
                        down = 1
                        current_yardline = 100 - current_yardline
                        if current_yardline <= 10:
                            distance = current_yardline
                        else:
                            distance = 10
                        def_team, poss_team = TogglePossession(poss_team)
                        possession = False

                    else:
                        if play_type[0] == 'Pass':
                            pass_type = random.choices(pass_play,
                                                       [poss_team.off_comp_pct, (1 - poss_team.off_comp_pct)])
                            if pass_type[0] == 'Pass Complete':
                                yardage_gained = int(
                                    random.normalvariate(poss_team.off_comp_pass_avg, poss_team.off_comp_pass_std))
                                play_rp = 'Pass COMPLETE'
                            else:
                                yardage_gained = 0
                                play_rp = 'Pass INCOMPLETE'

                        else:
                            yardage_gained = int(random.normalvariate(poss_team.off_run_avg, poss_team.off_run_std))
                            play_rp = 'Run'

                        print(
                            f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                            f"{play_rp} for {yardage_gained} yards")

                        if yardage_gained >= current_yardline:
                            xp_result = random.choices(kick_made, [95, 5])
                            if xp_result[0] == 'GOOD':
                                poss_team.score = poss_team.score + 7
                            else:
                                poss_team.score = poss_team.score + 6

                            print(
                                f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                f"TOUCHDOWN {play_rp} ({current_yardline} yards) - Extra Point {xp_result[0]}")
                            print(
                                f"\n{poss_team.team_name} {poss_team.score}   "
                                f"{def_team.team_name} {def_team.score}\n")
                            current_yardline = 75
                            distance = 10
                            def_team, poss_team = TogglePossession(poss_team)
                            possession = False
                        elif yardage_gained >= distance:
                            down = 1
                            current_yardline = current_yardline - yardage_gained
                            if current_yardline <= 10 and yardage_gained > distance:

                                distance = current_yardline

                            else:
                                distance = 10

                        elif (current_yardline - yardage_gained) > 99:
                            def_team.score = def_team.score + 2
                            print(
                                f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                f"SAFETY {play_type[0]} attempt for {yardage_gained} yards)")
                            print(
                                f"\n{poss_team.team_name} {poss_team.score}   {def_team.team_name} {def_team.score}\n")
                            current_yardline = 75
                            down = 1
                            distance = 10
                            def_team, poss_team = TogglePossession(poss_team)
                            possession = False

                        else:

                            down = down + 1
                            distance = distance - yardage_gained
                            current_yardline = current_yardline - yardage_gained

                else:
                    fourth_decision = random.choices(fourth_play,
                                                     [poss_team.off_kick_rate, (1 - poss_team.off_kick_rate)])
                    if fourth_decision[0] == 'Go':
                        play_type = random.choices(pass_run, [poss_team.off_pass_rate, (1 - poss_team.off_pass_rate)])
                        td_rate = Yardline(scoring_rates, current_yardline)
                        relative_yardline = YardConverter(current_yardline)

                        if play_type[0] == 'Pass':
                            td_result = random.choices(td_play, [td_rate.pass_score_rate, td_rate.pass_no_score_rate])
                            int_result = random.choices(int_play,
                                                        [poss_team.off_int_rate, (1 - poss_team.off_int_rate)])
                            if int_result[0] == 'INT':
                                turnover = True
                                turnover_type = 'INT'
                            else:
                                turnover = False
                                turnover_type = None

                        else:
                            td_result = random.choices(td_play, [td_rate.run_score_rate, td_rate.run_no_score_rate])
                            fum_result = random.choices(fumble_play,
                                                        [poss_team.off_fum_rate, (1 - poss_team.off_fum_rate)])
                            if fum_result[0] == 'Fumble':
                                turnover = True
                                turnover_type = 'Fumble'
                            else:
                                turnover = False
                                turnover_type = None

                        if td_result[0] == 'TD':

                            xp_result = random.choices(kick_made, [95, 5])
                            if xp_result[0] == 'GOOD':
                                poss_team.score = poss_team.score + 7
                            else:
                                poss_team.score = poss_team.score + 6

                            print(
                                f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                f"TOUCHDOWN {play_type[0]} ({current_yardline} yards) - Extra Point {xp_result[0]}")
                            print(
                                f"\n{poss_team.team_name} {poss_team.score}   {def_team.team_name} {def_team.score}\n")
                            down = 1
                            distance = 10
                            current_yardline = 75
                            def_team, poss_team = TogglePossession(poss_team)
                            possession = False

                        elif turnover:
                            print(
                                f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                f"Turnover - {turnover_type}\n")
                            down = 1
                            current_yardline = 100 - current_yardline
                            if current_yardline <= 10:
                                distance = current_yardline
                            else:
                                distance = 10
                            def_team, poss_team = TogglePossession(poss_team)
                            possession = False

                        else:
                            if play_type[0] == 'Pass':
                                pass_type = random.choices(pass_play,
                                                           [poss_team.off_comp_pct, (1 - poss_team.off_comp_pct)])
                                if pass_type[0] == 'Pass Complete':
                                    yardage_gained = int(
                                        random.normalvariate(poss_team.off_comp_pass_avg, poss_team.off_comp_pass_std))
                                    play_rp = 'Pass COMPLETE'
                                else:
                                    yardage_gained = 0
                                    play_rp = 'Pass INCOMPLETE'

                            else:
                                yardage_gained = int(random.normalvariate(poss_team.off_run_avg, poss_team.off_run_std))
                                play_rp = 'Run'

                            if yardage_gained >= distance:
                                down = 1
                                current_yardline = current_yardline - yardage_gained
                                if current_yardline <= 0:
                                    xp_result = random.choices(kick_made, [95, 5])
                                    if xp_result[0] == 'GOOD':
                                        poss_team.score = poss_team.score + 7
                                    else:
                                        poss_team.score = poss_team.score + 6

                                    print(
                                        f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                        f"TOUCHDOWN {play_rp} ({current_yardline} yards) - Extra Point {xp_result[0]}")
                                    print(
                                        f"\n{poss_team.team_name} {poss_team.score}   "
                                        f"{def_team.team_name} {def_team.score}\n")
                                    current_yardline = 75
                                    down = 1
                                    distance = 10
                                    def_team, poss_team = TogglePossession(poss_team)
                                    possession = False

                                elif current_yardline <= 10:
                                    print(
                                        f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                        f"{play_rp} for {yardage_gained} yards")
                                    distance = current_yardline

                                else:
                                    print(
                                        f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                        f"{play_rp} for {yardage_gained} yards")
                                    distance = 10

                            elif (current_yardline - yardage_gained) > 99:
                                def_team.score = def_team.score + 2
                                print(
                                    f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                    f"SAFETY {play_type[0]} attempt for {yardage_gained} yards)")
                                print(
                                    f"\n{poss_team.team_name} {poss_team.score}   "
                                    f"{def_team.team_name} {def_team.score}\n")
                                down = 1
                                current_yardline = 75
                                distance = 10
                                def_team, poss_team = TogglePossession(poss_team)
                                possession = False

                            else:
                                print(
                                    f"{poss_team.team_name} {down} and {distance} from {relative_yardline}: "
                                    f"{play_rp} for {yardage_gained} yards - TURNOVER ON DOWNS\n")

                                down = 1
                                current_yardline = 100 - current_yardline + yardage_gained
                                if current_yardline <= 10:
                                    distance = current_yardline
                                else:
                                    distance = 10
                                def_team, poss_team = TogglePossession(poss_team)
                                possession = False
                    else:
                        if current_yardline <= 40:
                            kick_outcome = random.choices(kick_made, [poss_team.fg_pct, (1 - poss_team.fg_pct)])
                            fg_dist = current_yardline + 17
                            if kick_outcome[0] == 'GOOD':
                                poss_team.score = poss_team.score + 3
                                print(f"{poss_team.team_name} {down} and {distance}: {fg_dist} yard FG Attempt GOOD")
                                print(
                                    f"\n{poss_team.team_name} {poss_team.score}   "
                                    f"{def_team.team_name} {def_team.score}\n")
                                current_yardline = 75

                            else:
                                print(
                                    f"{poss_team.team_name} {down} and {distance}: {fg_dist} yard FG Attempt MISSED\n")
                                current_yardline = 100 - current_yardline - 7

                            down = 1
                            distance = 10
                            def_team, poss_team = TogglePossession(poss_team)
                            possession = False

                        else:
                            punt_yards = int(random.normalvariate(poss_team.off_punt_avg, poss_team.off_punt_std))
                            if punt_yards >= current_yardline:
                                relative_yardline_pre = YardConverter(current_yardline)
                                print(f"{poss_team.team_name} {down} and {distance} from {relative_yardline_pre}: "
                                      f"PUNTS {relative_yardline_pre} yards for TOUCHBACK\n")
                                down = 1
                                distance = 10
                                current_yardline = 80
                                def_team, poss_team = TogglePossession(poss_team)
                                possession = False

                            else:
                                relative_yardline_pre = YardConverter(current_yardline)
                                current_yardline = current_yardline - punt_yards
                                relative_yardline_post = YardConverter(current_yardline)
                                print(f"{poss_team.team_name} {down} and {distance} from {relative_yardline_pre}: "
                                      f"PUNTS {punt_yards} yards to {relative_yardline_post}\n")
                                down = 1
                                current_yardline = 100 - current_yardline
                                if current_yardline <= 10:
                                    distance = current_yardline
                                else:
                                    distance = 10
                                def_team, poss_team = TogglePossession(poss_team)
                                possession = False

    return team_a.score, team_b.score
