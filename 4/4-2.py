n = int(input())

hour = [i for i in range(0, n + 1) if '3' not in str(i)]
minute = [i for i in range(0, 60) if '3' not in str(i)]
sec = [i for i in range(0, 60) if '3' not in str(i)]

print(((n+1) * 60 * 60) - (len(hour) * len(minute) * len(sec)))
