with open("input.txt","r") as f: 
    banks = [line.strip() for line in f]

# part 1 
def max_joltage(bank):
    n = len(bank)
    max_val = 0
    for i in range(n):
        for j in range(i+1, n):
            pair = int(bank[i] + bank[j])
            if pair > max_val:
                max_val = pair
    return max_val

results = [max_joltage(bank) for bank in banks]
print(sum(results))

# part 2
def max_12digit_joltage(bank):
    n = len(bank)
    dp = [[0] * 13 for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(13):
            dp[i][j] = dp[i-1][j]
            if j > 0:
                take = dp[i-1][j-1] * 10 + int(bank[i-1])
                dp[i][j] = max(dp[i][j], take)
    return dp[n][12]

results = [max_12digit_joltage(bank) for bank in banks]
print(sum(results))