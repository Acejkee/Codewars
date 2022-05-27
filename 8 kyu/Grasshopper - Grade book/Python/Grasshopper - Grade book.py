def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if 0 <= score < 60:
        return 'F'
    elif 60 <= score < 70:
        return 'D'
    elif 70 <= score < 80:
        return 'C'
    elif 80 <= score < 90:
        return 'B'
    else:
        return 'A'
    return score
    