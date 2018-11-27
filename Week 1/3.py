

def calc_three_bonacci(prefix, n):
    past_results = dict()
    for i in range(0, n + 1):
        if i < 3:
            past_results[i] = prefix[i]
        else:
            past_results[i] = past_results[i - 1] + past_results[i - 2] - past_results[i - 3]
    
    #print(past_results)
    return past_results[n]    
    
with open('input.txt', 'r') as input:
    a, b, c, n = [int(x) for x in input.readline().split(' ')]

with open('output.txt', 'w') as output:
    result = calc_three_bonacci((a,b,c), n)
    output.write(str(result))
    output.write('\n')