# Returns the probability that a string of length l came from strs, when sampled uniformly. Assumes strs is nonempty.
def len_prob(l, strs):
    return sum([len(s) == l for s in strs]) / len(strs)


print(len_prob(5, ["happi", "coat", "happy", "kampuchea"]) == .5)

# Given are two strings (the strings to guess between) and the lists of arxiv and snarxiv strings. Output is the probability with which our model guesses string zero to be from arxiv.


def length_model(s0, s1, arxiv_strs, snarxiv_strs):
    l0, l1 = len(s0), len(s1)
    p0_given_arxiv = len_prob(l0, arxiv_strs)
    p1_given_snarxiv = len_prob(l1, snarxiv_strs)
    p0_given_snarxiv = len_prob(l0, snarxiv_strs)
    p1_given_arxiv = len_prob(l1, arxiv_strs)
    numer = p0_given_arxiv * p1_given_snarxiv
    denom = numer + p0_given_snarxiv * p1_given_arxiv
    return numer / denom


astrs = ["happi", "coat", "happy", "kampuchea"]
sstrs = ["celebration", "trabecula", "derogatory", "samps", "samplings"]

print(length_model("cramp", "hammerkop", astrs, sstrs) == .8)
