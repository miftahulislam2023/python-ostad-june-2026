height=20
aspect_ratio=0.5
filled=False

width = height
center_x = (width - 1) / 2.0
center_y = (height - 1) / 2.0

radius = min(center_x, center_y) - 0.5

for y in range(height):
    row = []
    for x in range(width):
        dx = (x - center_x) * aspect_ratio
        dy = (y - center_y)
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if filled:
            if distance <= radius * aspect_ratio:
                row.append("*")
            else:
                row.append(" ")
        else:
            if (radius * aspect_ratio - 0.45) <= distance <= (radius * aspect_ratio + 0.45):
                row.append("*")
            else:
                row.append(" ")
    print(" ".join(row))