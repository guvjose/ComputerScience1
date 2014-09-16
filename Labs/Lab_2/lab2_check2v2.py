# Jose Guvenilir
# guvenj
# lab 2 checkpoint 2 v2

def print_world_cup_data(country, num_wins, num_losses, num_draw, goals_for, goals_against):
  points = num_wins * 3 + num_draw
  goal_adv = goals_for - goals_against
  print country
  print "Win:", num_wins, "Losses:", num_losses, "Draw:", num_draw
  print "Total number of points:", points, "Goal advantage:", goal_adv

print_world_cup_data("Germany", 2, 1, 0, 7, 2)
print_world_cup_data("USA", 1, 1, 1, 4, 4)
print_world_cup_data("Argentina", 3, 0, 0, 6, 3)
print_world_cup_data("England", 0, 2, 1, 2, 4)