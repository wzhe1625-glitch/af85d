#!/usr/bin/env python3
import math
import time
import os
import random

R = 10
SHADES = " .:-=+*#%@"

# 伪随机大陆函数（固定种子，形状稳定）
def land(lon, lat):
    return (
        math.sin(lon * 3) +
        math.sin(lat * 4) +
        math.sin(lon * 2 + lat)
    ) > 0.8

def render(rot):
    lines = []
    for y in range(-R, R):
        line = ""
        for x in range(-R*2, R*2):
            nx = x / (R*2)
            ny = y / R
            d = nx*nx + ny*ny

            if d <= 1:
                z = math.sqrt(1 - d)
                lon = math.atan2(nx, z) + rot
                lat = math.asin(ny)

                # 光照（简单模拟）
                light = math.sin(lon) * math.cos(lat)
                shade = int((light + 1) / 2 * (len(SHADES) - 1))

                if land(lon, lat):
                    line += SHADES[min(shade + 2, len(SHADES)-1)]
                else:
                    line += SHADES[shade]
            else:
                # 星空
                line += "." if random.random() < 0.02 else " "
        lines.append(line)
    return "\n".join(lines)

rot = 0.0
while True:
    os.system("clear")
    print(render(rot))
    rot += 0.12
    time.sleep(0.08)