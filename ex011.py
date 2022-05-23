l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
print('A sua parede tem dimensão de {} x {} e a sua área é de {:.3f}m².'.format(l, a, area))
print('Para pintar essa parede, vocé precisará de {:.2f} L de tinta.'.format(area / 2))

