seg=int(input('Digite um quantidade de segundos: '))

min=seg/60
hora=min/60
dia=hora/24

print('%.f segundos equivalem a %.f min, %.f horas e %.f dias' % (seg, min, hora, dia))
