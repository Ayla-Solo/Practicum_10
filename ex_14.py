def first_match(target, pattern, start = 0, end = None):
    if end is None:
        end = len(target)

    if not pattern:
        return start if start <= end else -1

    if len(pattern) > end - start:
        return -1

    shifts = {b: i for i, b in enumerate(pattern)}

    i = start + len(pattern) - 1
    while i < end:
        j = len(pattern) - 1
        while j >= 0 and target[i - (len(pattern) - 1) + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i - len(pattern) + 1

        bad_char = target[i]
        shift = j - shifts.get(bad_char, -1)
        i += max(1, shift)

    return -1

def boyer_moore_positions(target, pattern, start = 0, end = None):
    if end is None:
        end = len(target)

    if not pattern:
        return ','.join(str(i) for i in range(start, min(end, len(target))))

    positions = []
    pos = start
    while pos < end:
        match_pos = first_match(target, pattern, pos, end)
        if match_pos == -1:
            break
        positions.append(match_pos)
        pos = match_pos + 1

    return ','.join(str(p) for p in positions)

print(first_match("ATGCAATCG", "ATC"))
print(boyer_moore_positions("ATCATCATC", "ATC"))
