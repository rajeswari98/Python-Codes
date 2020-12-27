from itertools import combinations as cob
numRooms=int(input())
lNR=list(map(int,input().split()))[0:numRooms]
numGuests=int(input())
count=0
for i in range(1,numRooms+1):
    for j in cob(lNR,i):
        if sum(j)==numGuests:
            count+=1
print(count)



'''

Hotel Rooms – Guests Accommodation: N rooms are there in a hotel. The number of guests each room can accommodate is passed as input. G guests are to be accommodated in these N rooms in such a way that a room containing at least one guest is filled to it’s maximum capacity. The program must print the number of ways W in which the accommodation can be arranged for G guests.

Input Format:
The first line contains N.
The second line contains the capacity of these N rooms separated by a space.
The third line contains G.

Output Format:
The first line contains W.

Boundary Conditions:
1 <= N <= 50
1 <= G <= 100

Example Input/Output 1:
Input:
5
1 2 3 4 6
8

Output:
2

Explanation:
The possible ways are
(2+6)- choosing rooms with capacity 2 and 6
(1+3+4) – choosing rooms with capacity 1,3 and 4
'''

