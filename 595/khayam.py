n = int(input())
frame = []
for i in range(n):
    row = [1]
    if i >0:
        for j in range(1,i):
            row.append(frame[i-1][j-1] + frame[i-1][j])
        row.append(1)
    frame.append(row)

for row in frame:
    for item in row:
        print(item, end=' ')
    print("")

