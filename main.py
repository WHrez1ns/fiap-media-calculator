print("===================================")
print("           FIAP CALCULATOR         ")
print("===================================")

nota1s = float(input("Digite a média parcial do primeiro semestre: "))
nota1s_value = nota1s * 0.4

nota2s = float(input("Digite a média parcial do segundo semestre: "))
nota2s_value = nota2s * 0.6

media_final = nota1s_value + nota2s_value

if (media_final < 60 and media_final > 40):
    print(f"Você está de exame | Média final \033[31m{media_final}\033[30m")

    exame_calc = (120 - media_final)
    print(f"Obs: você precisa tirar \033[32m{exame_calc}\033[30m para passar no exame")
elif (media_final < 40):
        print(f"Você está de DP | Média final \033[35m{media_final}\033[30m")
else:
    print(f"Você não está de exame | Média final \033[32m{media_final}\033[30m")