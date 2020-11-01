def get_knockout_sequence(n, depth=0, indices=[1, 2], complements=[]):
    """ Return a list of indices disposing n competitors in
        a knockout/eliminatory turn (recursive implementation).
        Based on http://stackoverflow.com/questions/13792213/"""
    if len(complements) <= depth:
        complements.append(2 ** (depth + 2) + 1)
    complement = complements[depth]
    i = 0
    while i < n / (2 ** depth):
        if complement - indices[i] <= n:
            if i == 1 or indices[i] % 2 == 0:
                indices[i] = [complement - indices[i], indices[i]]
            else:
                indices[i] = [indices[i], complement - indices[i]]
            indices = indices[:i] + get_knockout_sequence(
                n, depth + 1, indices[i], complements) + indices[i + 1:]
            i += len(indices) - 1
        else:
            i += 1
    return indices


# Per Antonio: cambia questa lista
sequence_to_order = ['1A', '2A', '3A', '1B', '3A']

if len(sequence_to_order) % 2 != 0:
    sequence_to_order.append('tie')

n = len(sequence_to_order)
indices = get_knockout_sequence(n)
for i, j in zip(indices[::2], indices[1::2]):
    print sequence_to_order[i-1], sequence_to_order[j-1]
