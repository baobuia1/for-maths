import json
import statistics

data = []
maths_score = []
user = {}

with open('./data.json')as f:
    data = json.load(f)

for user in data:
    maths_score.append(user.popitem()[1][1])

another_maths_score = maths_score.copy()
another_maths_score.sort()
another_maths_score.reverse()
maths_score.sort()

print(f'AM: {statistics.mean(maths_score)}')
print(f'GM: {statistics.geometric_mean(maths_score)}')
print(f'HM: {statistics.harmonic_mean(maths_score)}')
print(f'Median: {statistics.quantiles(maths_score)[1]}')
print(f'Quartiles: {statistics.quantiles(maths_score)[0]}, {statistics.quantiles(maths_score)[1]}, {statistics.quantiles(maths_score)[2]}')
print(f'Mode: {statistics.mode(another_maths_score)}')

print(f'Variance: {statistics.variance(maths_score)}')
print(f'Standard deviation: {statistics.variance(maths_score)**(1/2)}')