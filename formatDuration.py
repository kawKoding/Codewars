def format_duration(seconds):
    if seconds == 0:
        return "now"

    duration = {
        "year": 31536000,
        "day": 86400,
        "hour": 3600,
        "minute": 60,
        "second": 1,
    }

    totalCount = [0, 0, 0, 0, 0]

    durationVals = {
        0: "year",
        1: "day",
        2: "hour",
        3: "minute",
        4: "second",
    }

    finalStrings = []

    for element, dur in enumerate(duration, 0):
        while seconds >= duration[dur]:
            totalCount[element] += 1
            seconds = seconds - duration[dur]

    print(totalCount)

    for pos, num in enumerate(totalCount, 0):
        if num != 0:
            if num != 1:
                finalStrings.append(f"{num} {durationVals[pos]}s, and")
            elif num == 1:
                finalStrings.append(f"{num} {durationVals[pos]}, and")

    for pos, val in enumerate(finalStrings, 0):
        if pos != (len(finalStrings) - 2):
            finalStrings[pos] = val.replace(" and", "")
        else:
            finalStrings[pos] = val.replace(",", "")

    returnString = ' '.join(finalStrings)
    returnString = returnString[:len(returnString) - 1]

    return returnString

#test
if __name__ == "__main__":
    print(format_duration(12313))