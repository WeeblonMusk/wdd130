import math

def main ():
    name='#1 Picnic'
    radius=6.83
    height=10.16
    volume=can_vol(radius,height)
    area=can_area(radius,height)
    eff=volume/area
    cost=0.28
    print(f'{name} volume: {volume:.2f} area: {area:.2f} efficiency: {eff:.2f}')
    cost_eff(6.83, 10.16, cost)

    name='#1 Tall'
    radius=7.78
    height=11.91
    cost=0.43
    can_eff(name,radius,height)
    cost_eff(7.78, 11.91, cost)

    can_eff('#2', 8.73, 11.59)
    cost_eff(8.73, 11.59, 0.45)

def can_vol (radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

def can_area (radius, height):
    area = ((2*math.pi)*radius) * (radius+height) 
    return area

def can_eff(name,radius,height):
    volume=can_vol(radius,height)
    area=can_area(radius,height)
    eff=volume/area
    print(f'{name} volume: {volume:.2f} area: {area:.2f} efficiency: {eff:.2f}')
    return area


def cost_eff(radius,height,cost):
    volume = can_vol(radius,height)
    c_eff=(volume/cost)
    print(f'Cost efficiency is: {c_eff:.2f}')


main()
