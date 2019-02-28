from scipy import special

## Permutation and Combination Problems

# 1. Out of 7 consonants and 4 vowels:
# A) How many words of 3 consonants and 2 vowels can be formed?

consonants = special.comb(7,3, exact=False)
vowels = special.comb(4,2, exact=False)
num_of_ways = consonants * vowels
print("Total number of ways1:" , num_of_ways)

# B) Find the probability that there are 3 consonants and 2 vowels
total = special.comb(11,5, exact=False)
prob = num_of_ways/total *100

print("Probability1:", prob, "%")

# 2. There are 6 boys, 4 girls. Find the probability that they can be selected so that there 
# are 6 boys and 0 girls?
# A) Number of Ways
boys = special.comb(6,6,exact=False)
girls = special.comb(4,0,exact=False)
print("Total number of ways2:", boys*girls)

# B) Probability:
total = special.comb(10,6, exact=False)
prob2 = (boys*girls)/total *100
print("Probability2:", prob2, "%")

# Easier way to do this is to create a function to answer questions similar to those two
# Similiarities:
# - Two distinct groups (vowels vs. consonants, girls vs.boys)
# - Finding the number of ways and finding the probability
# - Total number of items given
def ways(grp1_total, grp1_wanted, grp2_total, grp2_wanted):
    grp1_ways = special.comb(grp1_total, grp1_wanted, exact=False)
    grp2_ways = special.comb(grp2_total, grp2_wanted,exact=False)
    return grp1_ways * grp2_ways

def probability(grp1_total, grp1_wanted, grp2_total, grp2_wanted):
    total = grp1_total + grp2_total 
    total_wanted = grp1_wanted + grp2_wanted
    total_ways = special.comb(total, total_wanted, exact=False)
    num_ways = ways(grp1_total, grp1_wanted, grp2_total, grp2_wanted)
    return num_ways/total_ways * 100

# Testing it out:
# Question #1: 
print("Fn1 Number of Ways:", ways(7,3,4,2))
print("Fn1 Probability: ", probability(7,3,4,2), "%")


# Question # 2:
print("Fn2 Number of Ways 2:", ways(6,6,4,0))
print("Fn2 Probability:", probability(6,6,4,0), "%")


