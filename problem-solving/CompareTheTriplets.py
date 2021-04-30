
# Compare the rating from alice and bob.
# If Alice's rating is > than Bob, return 1, 0 if equal. Return Alice's score first and Bob's score second.
def compare_triplets(alice_ratings, bob_ratings):
    alice_score = bob_score = 0

    for i in range(len(alice_ratings)):
        if alice_ratings[i] > bob_ratings[i]:
            alice_score += 1
        elif bob_ratings[i] > alice_ratings[i]:
            bob_score += 1

    return [alice_score, bob_score]


if __name__ == '__main__':
    print(compare_triplets([17, 28, 30], [99, 16, 8]))
