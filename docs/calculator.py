import pandas as pd
import numpy as np
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

df_cents = fractions2.dot(fractions.T).apply(lambda col: [np.round((np.log(x.numerator) - np.log(x.denominator))/np.log(2**(1/1200))).astype(int) for x in col], axis=0)


# from matplotlib import colormaps
# import seaborn as sns
# colors = colormaps['hsv'](np.linspace(0, 1, 12))
# colors = np.array(sns.color_palette("hls", 12))

# colors from:
# https://www.flutopedia.com/sound_color.htm
colors = ["#740000",
          "#b30000",
          "#ee0000",
          "#ff6300",
          "#ffec00",
          "#99ff00",
          "#28ff00",
          "#00ffe8",
          "#007cff",
          "#0500ff",
          "#4500ea",
          "#57009e",
          ]
colors = ["#520000",
          "#740000",
          "#b30000",
          "#ee0000",
          "#ff6300",
          "#ffec00",
          "#99ff00",
          "#28ff00",
          "#007cff",
          "#0500ff",
          "#4500ea",
          "#57009e",
          ]

# modified from matlab hsv palette
colors = ["#ffffff",
          "#ff0000",
          "#ff5800",
          "#ffaa00",
          "#eeff00",
          "#99ff00",
          "#00ff90",
          "#00c7ff",
          "#0000ff",
          "#6f65ff",
          "#d655ff",
          "#ff00a0",
          ]

text_color = ["black"] + ["white"] + ["black"] * 6 + ["white"] * 2 + ["black"] + ["white"]

df_cents["intervals"] = ["U", "m2", "M2", "m3", "M3", "P4", "TT", "P5", "m6", "M6", "m7", "M7"] + [""] * 6

def styler(col):
    if col.name != "intervals":
        return ["background-color: #%.2x%.2x%.2x" % tuple(np.round(255*colors[int(x/100 % 12)]).astype(int)[:3]) for x in col]
    else:
        return ["background-color: #%.2x%.2x%.2x" % tuple(np.round(255*colors[x]).astype(int)[:3]) for x in range(0, 12)] + [""] * 6

def styler(col):
    if col.name != "intervals":
        return ["background-color: " + colors[int(np.round(x/100) % 12)] + "; color: " + text_color[int(np.round(x/100) % 12)] for x in col]
    else:
        return ["background-color: " + colors[x] + "; color: " + text_color[x] for x in range(0, 12) ]  + [""] * 6
df_cents = df_cents.style.apply(styler)
df_cents.to_excel('cents.xlsx')
