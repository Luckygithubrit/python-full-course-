# A sports coach stores the jersey numbers of 12 players in a list. Write a program to divide the players into two equal teams and exchange the positions of both teams.

team=[1,2,3,4,5,6,7,8,9,10,11,12]
team1=team[0:6]
team2=team[6:]
print("team1:",team1)#team1: [1, 2, 3, 4, 5, 6]
print("team2:",team2)#team2: [7, 8, 9, 10, 11, 12]

# exchange the positions
print(team2+team1)#[7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6]
