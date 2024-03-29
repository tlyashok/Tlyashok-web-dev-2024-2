def passengers_in_metro(N, passenger_data, T):
    count = 0
    for entry_time, exit_time in passenger_data:
        if entry_time <= T <= exit_time:
            count += 1
    return count

N = int(input().strip())

passenger_data = []
for _ in range(N):
    entry, exit = map(int, input().strip().split())
    passenger_data.append((entry, exit))

T = int(input().strip())

print(passengers_in_metro(N, passenger_data, T))