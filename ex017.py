# hipotenusa² = cateto oposto² + cateto adjacente²
# a² = b² + c²
from math import sqrt
b = float(input('Qual é o comprimento do cateto oposto? : '))
c = float(input('Qual é o comprimeto do cateto adjacente? : '))
a = b ** 2 + c ** 2
print('Se o cateto oposto é {} e o adjacente é {} o comprimento da Hipotenusa corresponde a:{:.2f}'.format(b, c, sqrt(a)))


