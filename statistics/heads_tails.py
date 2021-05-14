import random
import sys
import math
from enum import Enum


class CoinToss(Enum):
    HEADS = 'heads'
    TAILS = 'tails'


def coin_toss() -> CoinToss:
    return random.choice(list(CoinToss))


# We will toss a coin for {number_of_tosses} times. Such an event is favorable if heads appear exactly heads_count times
# and the sequence ends in heads. This is repeated for {number_of_repetitions} times and then the frequency of favorable
# cases is calculated and returned.
# Hypothesis 1 is that P(k=number_of_tosses, h=head_count) = (k - 1)!/(2^k*(k - h)!) - proved wrong by this experiment
# Hypothesis 2 P(k,h) = (k-1)!/(2^k*(k-h)!*(h-1)!). Deducted by using "probability of getting K heads in N coin tosses"
def calculate_frequency(number_of_tosses, heads_count, number_of_repetitions):
    favorable_sequences = 0
    for i in range(0, number_of_repetitions):
        sequence = []
        for j in range(0, number_of_tosses):
            sequence.append(coin_toss())
        if sequence[-1] == CoinToss.HEADS and sequence.count(CoinToss.HEADS) == heads_count:
            favorable_sequences += 1

    return favorable_sequences / number_of_repetitions


number_of_tosses, heads_count, number_of_repetitions = map(int, sys.argv[1:])

frequency = calculate_frequency(number_of_tosses, heads_count, number_of_repetitions)
hypothesis_1 = math.factorial(number_of_tosses - 1) \
               / (2**number_of_tosses * math.factorial(number_of_tosses - heads_count))
hypothesis_2 = math.factorial(number_of_tosses - 1) \
               / (2**number_of_tosses * math.factorial(number_of_tosses - heads_count)*math.factorial(heads_count-1))

print(f'Hypothesis 1 probability: {hypothesis_1}, actual frequency: {frequency}')
print(f'Hypothesis 2 probability: {hypothesis_2}, actual frequency: {frequency}')
