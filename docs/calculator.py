import pandas as pd
from fractions import Fraction

fractions = pd.DataFrame(
    [Fraction(x, 8) for x in range(2, 11)] + [Fraction(8, x) for x in range(2, 11)],
    index=list(range(2, 11)) + list(range(-2, -11, -1)),
)


fractions2 = pd.DataFrame(
    [Fraction(8, x) for x in range(2, 11)] + [Fraction(x, 8) for x in range(2, 11)],
    index=list(range(-2, -11, -1)) + list(range(2, 11)),
)

fractions2.dot(fractions.T).to_csv("kleingorium_tones.csv")
