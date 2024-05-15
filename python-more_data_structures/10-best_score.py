#!/usr/bin/python3
def best_score(scores):
    if scores is None or not scores:
        return None

    best_key = None
    best_value = float('-inf')

    for key, value in scores.items():
        if value > best_value:
            best_key = key
            best_value = value

    return best_key
