# Использование %:
name_team_1 = "Мастера кода"
name_team_2 = "Волшебники данных"
team1_num = 5
team2_num = 6
print("В команде '%s' участников: %s" % (name_team_1, team1_num))
print("В команде '%s' участников: %s" % (name_team_2, team2_num))
print("Итого сегодня в командах учвстников %s и %s!" % (team1_num, team2_num))

# Использование format():
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = f"{score_1 + score_2}"
time_avg = f"{(team1_time + team2_time) / int(tasks_total)}"
print("Команда '{}' решила задач: {}".format(name_team_1, score_1))
print("'{}' решили задачи за {} секунд!".format(name_team_1, team1_time))
print("Команда '{}' решила задач: {}".format(name_team_2, score_2))
print("'{}' решили задачи за {} секунд!".format(name_team_2, team2_time))

# Использование f-строк:
print(f"Команды решили {score_1} и {score_2} задач!")

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f"Победа команды '{name_team_1}'!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f"Победа команды '{name_team_2}'!"
else:
    challenge_result = "Ничья!"
print(f"Результать битвы: {challenge_result}!")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {round(float(time_avg), 2)} секунды на задачу!.")