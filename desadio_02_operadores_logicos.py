# Os Trabalhos
TUESDAY_WORK = True
THURSDAY_WORK = False

"""
- Confirmando os 2: TV 50' + sorvete
- Confirmando apenas 1: TV 32' + sorvete
- Nenhum confirmado: Fica em casa
"""

TV_50 = TUESDAY_WORK and THURSDAY_WORK
ICECREAM = TUESDAY_WORK or THURSDAY_WORK
TV_32 = TUESDAY_WORK != THURSDAY_WORK  # XOR
MORE_HEALTHY = not ICECREAM

print("Tv50 = {} Tv32 = {} Icecream = {} Healthy = {}"
      .format(TV_50, TV_32, ICECREAM, MORE_HEALTHY))

# print("{}, {} = {}".format(1, False, "resultado")) -> 1, False = resultado
# print("{1}, {2} = {0}".format(1, False, "resultado")) -> False, resultado = 1
