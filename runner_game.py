import projector_utils as util
import matplotlib.pyplot as plt
import pandas as pd
from fpdf import FPDF
import numpy as np

week = 10
game = 0

j = 5000


class PDF(FPDF):
    def header(self):
        # Logo
        self.image('logos/xNational_Football_League_logo.png', 10, 8, 15)
        # Arial bold 15
        self.set_font('Times', 'B', 15)
        # Title
        self.cell(210, 0, f'Single Game Report', 0, 0, 'C')
        # Line break
        self.ln(30)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Times', '', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/16', 0, 0, 'C')


team_data_book = pd.read_csv("team_data_book.csv")
# game_book = pd.read_csv(f"week{week}_game_book.csv")
game_book = pd.read_csv(f"week{week}/week{week}_game_book.csv")
pdf = PDF()
fig, ax = plt.subplots()

game_scores = []
home_deltas = []
game_totals = []

home_name = game_book['home_team_name'][game]
home_id = game_book['home_team_id'][game]
away_name = game_book['away_team_name'][game]
away_id = game_book['away_team_id'][game]
home_line = game_book['home_line'][game]
o_u = game_book['total'][game]
date = game_book['date'][game]
time = game_book['time'][game]
print(home_name, away_name)

home_color1 = team_data_book['color_1'][home_id]
home_color2 = team_data_book['color_2'][home_id]
home_full_name = team_data_book['full_name'][home_id]
home_win = int(team_data_book['win'][home_id])
home_loss = int(team_data_book['loss'][home_id])
home_tie = int(team_data_book['tie'][home_id])
home_ats_win = int(team_data_book['ats_win'][home_id])
home_ats_loss = int(team_data_book['ats_loss'][home_id])
home_ats_push = int(team_data_book['ats_push'][home_id])
home_over = int(team_data_book['over'][home_id])
home_under = int(team_data_book['under'][home_id])
home_total_push = int(team_data_book['total_push'][home_id])
home_mc1 = team_data_book['margin_color_1'][home_id]
home_mc2 = team_data_book['margin_color_2'][home_id]
home_mc3 = team_data_book['margin_color_3'][home_id]
home_mc4 = team_data_book['margin_color_4'][home_id]

away_color1 = team_data_book['color_1'][away_id]
away_color2 = team_data_book['color_2'][away_id]
away_full_name = team_data_book['full_name'][away_id]
away_win = int(team_data_book['win'][away_id])
away_loss = int(team_data_book['loss'][away_id])
away_tie = int(team_data_book['tie'][away_id])
away_ats_win = int(team_data_book['ats_win'][away_id])
away_ats_loss = int(team_data_book['ats_loss'][away_id])
away_ats_push = int(team_data_book['ats_push'][away_id])
away_over = int(team_data_book['over'][away_id])
away_under = int(team_data_book['under'][away_id])
away_total_push = int(team_data_book['total_push'][away_id])
away_mc1 = team_data_book['margin_color_1'][away_id]
away_mc2 = team_data_book['margin_color_2'][away_id]
away_mc3 = team_data_book['margin_color_3'][away_id]
away_mc4 = team_data_book['margin_color_4'][away_id]

plt.cla()
fig, ax = plt.subplots()
i = 1
while i <= j:
    a_score, b_score = util.ProjectGame(home_id, away_id, i, j)
    game_scores.append((a_score, b_score))

    home_delta = a_score - b_score
    home_deltas.append(home_delta)

    total = a_score + b_score
    game_totals.append(total)
    i = i + 1

    if home_delta > (-1 * home_line):
        ax.scatter(home_delta, total, c=home_color1)
    elif home_delta < (-1 * home_line):
        ax.scatter(home_delta, total, c=away_color1)
    else:
        ax.scatter(home_delta, total, c='k')

plt.axhline(y=o_u, color='k', linestyle='--', linewidth=1)
plt.axvline(x=(-1 * home_line), color='k', linestyle='--', linewidth=1)
plt.title(f"{away_name} @ {home_name} - Week {week} ({j} Simulations)")
plt.xlabel(f"Home Margin (Line {home_line})")
plt.ylabel(f'Total Points (O/U {o_u})')

plt.plot()
plt.draw()
plt.savefig(f"single_game_runs/figures/{away_name}_at_{home_name}_scatter_w{week}")
plt.cla()

fig, ax = plt.subplots()
for score in range(j):
    if home_deltas[score] > (-1 * home_line):
        ax.scatter(game_scores[score][0], game_scores[score][1], c=home_color1)
    elif home_deltas[score] < (-1 * home_line):
        ax.scatter(game_scores[score][0], game_scores[score][1], c=away_color1)
    else:
        ax.scatter(game_scores[score][0], game_scores[score][1], c='k')

x = np.linspace(0, o_u, 10)
scoring_line = 1*x + home_line
total_line = -1*x + o_u
plt.plot(x, scoring_line, color='k', linestyle='--', linewidth=1, label=f"{home_name} ({home_line})")
plt.plot(x, total_line, color='k', linestyle='-', linewidth=1, label=f"O/U {o_u}")
plt.xlabel(f"{home_name} Score")
plt.ylabel(f"{away_name} Score")
plt.xlim((-1,60))
plt.ylim((-1,60))
plt.legend()
plt.savefig(f"single_game_runs/figures/{away_name}_at_{home_name}_scores_w{week}")

plt.cla()
fig, ax = plt.subplots()
overs = 0
unders = 0
push = 0
games_played = j
for tot in game_totals:
    if tot >= o_u + 4:
        overs += 1
    elif tot <= o_u - 4:
        unders += 1
    else:
        push += 1
over_pct = 100 * (overs / games_played)
under_pct = 100 * (unders / games_played)
o_u_pct = 100 - over_pct - under_pct
# Setting labels for items in Chart
labels = ['Total + 5', 'Total - 5', 'O/U +/- 5']
values = [over_pct, under_pct, o_u_pct]
colors = ['#009c08', '#990000', '#000000']
explode = (0.05, 0.05, 0.05)
_, _, autotexts1 = plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors,
                           pctdistance=0.85, startangle=90, explode=explode,
                           wedgeprops={'edgecolor': 'k'}, rotatelabels=False)
for autotext in autotexts1:
    autotext.set_color('white')

centre_circle = plt.Circle((0, 0), 0.70, fc='white', ec='black')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.savefig(f"single_game_runs/figures/{away_name}_at_{home_name}_totals_w{week}")

plt.cla()
fig, ax = plt.subplots()

ties = 0
a_05 = 0
a_610 = 0
a_1115 = 0
a_16 = 0
b_05 = 0
b_610 = 0
b_1115 = 0
b_16 = 0

for dif in home_deltas:
    if dif == 0:
        ties += 1
    elif dif >= 16:
        a_16 += 1
    elif dif >= 11:
        a_1115 += 1
    elif dif >= 6:
        a_610 += 1
    elif dif >= 0:
        a_05 += 1
    elif dif >= -5:
        b_05 += 1
    elif dif >= -10:
        b_610 += 1
    elif dif >= -15:
        b_1115 += 1
    elif dif <= -16:
        b_16 += 1
    else:
        pass

labels = [f'{home_name} 0-5', f'{home_name} 6-10', f'{home_name} 11-15', f'{home_name} 16+',
          f'{away_name} 0-5', f'{away_name} 6-10', f'{away_name} 11-15', f'{away_name} 16+', 'Tie/OT']
values = [a_05, a_610, a_1115, a_16, b_05, b_610, b_1115, b_16, ties]
colors = [home_mc1, home_mc2, home_mc3, home_mc4,
          away_mc1, away_mc2, away_mc3, away_mc4, '#000000']
explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
_, _, autotexts2 = plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors,
                           pctdistance=0.80, startangle=90, explode=explode,
                           wedgeprops={'edgecolor': 'k'}, rotatelabels=True)
for autotext in autotexts2:
    autotext.set_color('white')
centre_circle = plt.Circle((0, 0), 0.70, fc='white', ec='black')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.savefig(f"single_game_runs/figures/{away_name}_at_{home_name}_spread_w{week}")

a_scores = []
b_scores = []
for score in game_scores:
    a_scores.append(score[0])
    b_scores.append(score[1])

a_average = int(np.average(a_scores))
b_average = int(np.average(b_scores))

if (a_average - b_average) > (-1 * home_line):
    ats_pick = home_name
    ats_value = (a_average - b_average) + home_line
    ats_line = home_line
elif (a_average - b_average) < (-1 * home_line):
    ats_pick = away_name
    ats_value = (a_average - b_average) + home_line
    ats_line = -1 * home_line
else:
    ats_pick = 'No ATS Pick'
    ats_value = ''
    ats_line = ''

if (a_average + b_average) > o_u:
    total_pick = 'Over'
    total_value = (a_average + b_average) - o_u
elif (a_average + b_average) < o_u:
    total_pick = 'Under'
    total_value = o_u - a_average + b_average
else:
    total_pick = 'No Total Pick'
    total_value = ''
pdf.add_page()
pdf.set_font('Times', '', 12)
pdf.cell(210, 0, f"{away_full_name} @ {home_full_name}", 0, 1, 'C')
pdf.ln(5)
pdf.cell(210, 0, f"{date}", 0, 1, 'C')
pdf.ln(5)
pdf.cell(210, 0, f"{time} PM", 0, 1, 'C')
pdf.ln(10)
pdf.set_font('Times', 'b', 12)
pdf.cell(210, 0, "Pick                Value", 0, 1, 'C')
pdf.ln(7)
pdf.set_font('Times', '', 12)
pdf.cell(210, 0, f"{ats_pick} ({ats_line})          {ats_value}", 0, 1, 'C')
pdf.ln(5)
pdf.cell(210, 0, f"{total_pick} ({o_u})          {total_value}", 0, 1, 'C')
pdf.ln(10)
pdf.set_font('Times', '', 12)
pdf.cell(105, 0, f"Overall: {away_win} - {away_loss} - {away_tie}", 0, 0, 'C')
pdf.cell(105, 0, f"Overall: {home_win} - {home_loss} - {home_tie}", 0, 1, 'C')
pdf.ln(5)
pdf.cell(105, 0, f"ATS: {away_ats_win} - {away_ats_loss} - {away_ats_push}", 0, 0, 'C')
pdf.cell(105, 0, f"ATS: {home_ats_win} - {home_ats_loss} - {home_ats_push}", 0, 1, 'C')
pdf.ln(5)
pdf.cell(105, 0, f"Overs: {away_over} - {away_under} - {away_total_push}", 0, 0, 'C')
pdf.cell(105, 0, f"Overs: {home_over} - {home_under} - {home_total_push}", 0, 1, 'C')
pdf.set_font('Times', 'B', 18)
pdf.ln(2)
pdf.cell(210, 0, f"Projected Score", 0, 1, 'C')
pdf.ln(10)
pdf.cell(105, 0, f"{b_average}", 0, 0, 'C')
pdf.cell(105, 0, f"{a_average}", 0, 1, 'C')

pdf.image(f"logos/{away_name}.png", 52, 55, 20)
pdf.image(f"logos/{home_name}.png", 158, 55, 20)
pdf.image(f'single_game_runs/figures/{away_name}_at_{home_name}_scatter_w{week}.png', 15, 115, 90)
pdf.image(f'single_game_runs/figures/{away_name}_at_{home_name}_scores_w{week}.png', 115, 115, 90)
pdf.image(f'single_game_runs/figures/{away_name}_at_{home_name}_spread_w{week}.png', 15, 200, 90)
pdf.image(f'single_game_runs/figures/{away_name}_at_{home_name}_totals_w{week}.png', 115, 200, 90)

pdf.output(f"single_game_runs/{away_name}_at_{home_name}_w{week}.pdf", 'F')
