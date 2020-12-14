import colorgram

colors = colorgram.extract("paint.jpg", 20)
rgb_colors = []

LIMIT_BRIGHT = 235

for color in colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    if (r, g, b) < (LIMIT_BRIGHT, LIMIT_BRIGHT, LIMIT_BRIGHT):
        rgb_colors.append((r, g, b))