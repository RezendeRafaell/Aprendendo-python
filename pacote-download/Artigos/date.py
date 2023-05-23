# from datetime import date

# data_atual = date.today()
# print(data_atual)


# data_em_texto = data_atual.strftime('%d/%m/%Y')
# print(data_em_texto)


# from datetime import datetime

# data_e_hora_atuais = datetime.now()
# data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

# print(data_e_hora_em_texto)

# from datetime import datetime, timezone, timedelta

# data_e_hora_atuais = datetime.now()
# # fuso_horario = timezone(-3)
# # print(fuso_horario)

# diferenca = timedelta(hours=-3)


# fuso_horario = timezone(diferenca)
# print(fuso_horario)


# data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
# data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime(
#     '%d/%m/%Y %H:%M')

# print(data_e_hora_sao_paulo_em_texto)


import pytz
from datetime import datetime
from pytz import timezone
# MAIS ELEGANTE E FÁCIL!
data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime(
    '%d/%m/%Y %H:%M')

print(data_e_hora_sao_paulo_em_texto)


for tz in pytz.all_timezones:
    print(tz)
