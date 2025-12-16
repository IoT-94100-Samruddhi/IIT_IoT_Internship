def km_m(km):
    return km*1000

def m_centi(m):
    return m*100

def centi_mili(centi):
    return centi*10

def feet_inch(feet):
    return feet*12

def inch_centi(inches):
    return inches*2.54

def distance_converter(distance, conversion_type, func):
    result = func(distance)
    print(conversion_type,":",result)


distance=float(input("enter distance:"))

distance_converter(distance,"kilometer_meter:",km_m)
distance_converter(distance,"m_centi:",m_centi)
distance_converter(distance,"centimeter_mili:",centi_mili)
distance_converter(distance,"feet_inch:",feet_inch)
distance_converter(distance,"inch_centi:",inch_centi)




