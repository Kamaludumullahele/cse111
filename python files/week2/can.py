import math
def main():
    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    cost = 0.28
    volume = can_vol(radius, height)
    area = can_area(radius, height)
    eff = volume/area
    ceff = volume/ cost
    print(f"{name} volume: {volume:.2f} Surface area: {area:.2f} Efficiency: {eff:.2f} Cost efficiency: {ceff:.2f}")

    name = "#1 Tall"
    radius = 7.78
    height = 11.91
    cost = 0.43
    can_eff(name, radius, height)
    

    name = "#2"
    radius = 8.73
    height = 11.59
    can_eff(name, radius, height)
    
    
    name = "#2.5"
    radius = 10.32
    height = 11.91
    can_eff(name, radius, height)
    

    name = "#3 Cylinder"
    radius = 10.79
    height = 17.78
    can_eff(name, radius, height)
    


    name = "#5"
    radius = 13.02
    height = 14.29
    can_eff(name, radius, height)
    

    name = "6Z"
    radius = 5.40
    height = 8.89
    can_eff(name, radius, height)
    

    name = "8Z Short"
    radius = 6.83
    height = 7.62
    can_eff(name, radius, height)
    

    name = "#10"
    radius = 15.72
    height = 17.78
    can_eff(name, radius, height)

    name = "#211"
    radius = 6.83
    height = 12.38
    can_eff(name, radius, height)
    
    name = "#300"
    radius = 7.62
    height = 11.27
    can_eff(name, radius, height)


    name = "#303"
    radius = 8.10
    height = 11.11
    can_eff(name, radius, height)
    
    
def can_eff(name, radius, height):
    volume = can_vol(radius, height)
    area = can_area(radius, height)
    eff = volume/area
    print(f"{name} volume: {volume:.2f} Surface area: {area:.2f} Efficiency: {eff:.2f}")

    
def can_vol (radius, height):
    volume = math.pi* radius**2 * height
    return volume

def can_area (radius, height):
    area = 2* math.pi* radius* (radius+height)
    return area

main()
