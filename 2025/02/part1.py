with open("actual.in", "r") as f:
    input = f.read()
    ranges = input.split(",")
    counter = 0
    for item in ranges:
        start, end = item.split("-")
        print(f"now on: {start}-{end}")
        cur = 0;
        for num in range(int(start), int(end)):
            string = str(num)
            if len(string) % 2 != 0:
                continue
            mid = len(string) // 2
            first_half = string[:mid]
            second_half = string[mid:]
            if first_half == second_half:
                print(f"hit: {num}")
                cur += num
        print(f"sum: {cur}")
        counter += cur
    print(f"The answer is {counter}.")