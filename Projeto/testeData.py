from datetime import date

DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]
dataString = '2018-12-20'
year, month, day = map(int ,dataString.split('-'))

print('year ' ,day)
data = date(year=year, month=month, day=day)
print(data)

indice_da_semana = data.weekday()
print(indice_da_semana)

dia_da_semana = DIAS[indice_da_semana]
print(dia_da_semana)

numero_do_dia_da_semana = data.isoweekday()
print(numero_do_dia_da_semana)