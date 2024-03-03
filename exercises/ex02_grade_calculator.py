"""Calculate the final grade for COMP110"""

__author__: str = "730657739"


Scores = tuple[float, ...]
"""Scores is a tuple of floats representing percent credit from 0.0 to 1.0."""


EX: Scores = (105.0 / 100.0, 105.0 / 100.0)
"""Exercise scores"""

RD: Scores = (1.0 / 1.0,)
"""Reading scores"""

LS: Scores = (
    27.0 / 31.0,
    2.0 / 2.0,
    13.0 / 14.0,
    11.0 / 13.0,
    7.0 / 7.0,
    17.0 / 24.0,
    14.0 / 14.0,
)
"""Lesson scores"""

CL: Scores = (1.0 / 1.0, 1.0 / 1.0, 1.0 / 1.0)
"""Class scores"""

QZ: Scores = (38.0 / 42.0, 0.95, 0.9, 0.92)
"""Quiz scores"""

FN: float = 0.95
"""Hopefully my final exam grade"""


def average(grades: Scores) -> float:
    """Calculate the average score for a type of assignment"""
    if len(grades) == 0.0:
        return 0.0
    else:
        return sum(grades) / len(grades)


def ppp_components(ex: Scores, rd: Scores, ls: Scores, cl: Scores) -> float:
    """Calculate the Preparation, Practice, and Participation grade"""
    EX_WEIGHT: float = 0.25
    RD_WEIGHT: float = 0.05
    LS_WEIGHT: float = 0.05
    CL_WEIGHT: float = 0.05
    return (
        average(ex) * EX_WEIGHT
        + average(rd) * RD_WEIGHT
        + average(ls) * LS_WEIGHT
        + average(cl) * CL_WEIGHT
    )


def quiz_average(qz: Scores, fn: float) -> float:
    """Calculates the quiz average for COMP110"""
    if len(qz) == 0:
        return fn
    elif min(qz) >= fn:
        return average(qz)
    else:
        return (sum(qz) - min(qz) + fn) / len(qz)


def mastery_components(qz: Scores, fn: float) -> float:
    """Calculates the mastery components grade"""
    QZ_WEIGHT: float = 0.48
    FN_WEIGHT: float = 0.12
    return quiz_average(qz=qz, fn=fn) * QZ_WEIGHT + fn * FN_WEIGHT


def count_zeros(qz: Scores, count: int = 0, i: int = 0) -> int:
    """Count number of quizzes taken"""
    if i >= len(qz):
        return count
    else:
        if qz[i] == 0.0:
            return count_zeros(qz=qz, count=count + 1, i=i + 1)
        else:
            return count_zeros(qz=qz, count=count, i=i + 1)


def has_min_mastery(qz: Scores, fn: float) -> bool:
    """Determine if student has minimum mastery requirement"""
    return len(qz) >= 4 and count_zeros(qz=qz) <= 1 and fn >= 0.4


def letter_grade(total: float, has_min_mastery: bool) -> str:
    """Produces a letter grade for COMP110"""
    if has_min_mastery == False:
        return "F"
    elif total < 0.595:
        return "F"
    elif total < 0.695:
        return "D"
    elif total < 0.725:
        return "C-"
    elif total < 0.765:
        return "C"
    elif total < 0.795:
        return "C+"
    elif total < 0.825:
        return "B-"
    elif total < 0.865:
        return "B"
    elif total < 0.895:
        return "B+"
    elif total < 0.925:
        return "A-"
    else:
        return "A"


def calculate_grade(
    ex: Scores, rd: Scores, ls: Scores, cl: Scores, qz: Scores, fn: float
) -> str:
    """Produce a final grade"""
    return f"Final Grade: {letter_grade(total=ppp_components(ex=ex, rd=rd, ls=ls, cl=cl) + mastery_components(qz=qz,fn=fn), has_min_mastery = has_min_mastery(qz=qz, fn=fn))} ({round((ppp_components(ex=ex, rd=rd, ls=ls, cl=cl) + mastery_components(qz=qz, fn=fn)) * 100)}%)"


if __name__ == "__main__":
    print(calculate_grade(ex=EX, rd=RD, ls=LS, cl=CL, qz=QZ, fn=FN))
