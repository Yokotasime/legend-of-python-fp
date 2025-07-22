

# Write code below 💖

kcc_player1 = {
  'name': 'Patrick Mahomes',
  'position': 'Quarterback',
  'jersey_no': 15,
  'passing_yards': 30,
  'touch_downs': 219,
}

kcc_player2 = {
  'name': 'Tyreek Hill',
  'position': 'Wide Receiver',
  'jersey_no': 10,
  'passing_yards': 150,
  'touch_downs': 2,
}

kcc_player3 = {
  'name': 'Travis Kelce',
  'position': 'Tight End',
  'jersey_no': 87,
  'passing_yards': 12,
  'touch_downs': 74,
}

kcc_team = [kcc_player1, kcc_player2, kcc_player3]
new_yards = 100
new_touchdowns = 5

# Display the team members and their positions :), here I added the names in the case we have more than 1 person on the same position.

for player in kcc_team:
    print(f'Name: {player["name"]} | Position: {player["position"]}')

# Update the stats for player 1

kcc_player1['passing_yards'] += new_yards
kcc_player1['touch_downs'] += new_touchdowns
    
print(f'Updated passing yards for {kcc_player1["name"]}: {kcc_player1["passing_yards"]}')
print(f'Updated touchdowns for {kcc_player1["name"]}: {kcc_player1["touch_downs"]}')

# calculate the average passing yards and touchdowns for all players and print the results

total_yards = 0
total_touchdowns = 0

for player in kcc_team:
    total_yards += player['passing_yards']
    total_touchdowns += player['touch_downs']

average_yards = total_yards / len(kcc_team) # Calculate the average passing yards
average_touchdowns = total_touchdowns / len(kcc_team)
average_yards = round(average_yards, 1)  #Rounding the averages to 1 decimal
average_touchdowns = round(average_touchdowns, 1) 

print(f'Average passing yards: {average_yards}')
print(f'Average touchdowns: {average_touchdowns}')
