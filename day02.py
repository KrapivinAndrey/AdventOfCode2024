def security(report:list[int]):
    for i in range(len(report)-1):
        if abs(report[i] - report[i+1]) not in [1,2,3]:
            return 0

    report1=report.copy()
    report1.sort()

    report2 = report.copy()
    report2.sort(reverse=True)

    if report == report1 or report == report2:
        return 1

    return 0

def security2(report:list[int]):
    if security(report):
        return 1
    else:
        for i in range(len(report)):
            report2=report.copy()
            report2.pop(i)
            if security(report2):
                return 1
    return 0

reports = []
with open('input.txt') as f:
    for line in f:
        reports.append([int(x) for x in line.strip().split(" ")])

ans1 = sum([security(report) for report in reports])
print(ans1)

ans2 = sum([security2(report) for report in reports])
print(ans2)





