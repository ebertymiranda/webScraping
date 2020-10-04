# import pandas as pd
#
# # -8.947866 , -60.515091 esquerda cima
# # -9.836922 , -50.416322
# # -17.736736 , -52.311547
#
#
# dados_nasa = pd.read_csv('Dados.csv')
#
# pontos_mato_grosso = dados_nasa[dados_nasa['longitude'] >= -61];
# print(pontos_mato_grosso.head())

# -15.592320, -56.086179

def check_coordinates(lat, long):
    top_left = (-8.947866, -60.515091)
    top_right = (-9.836922, -50.416322)
    bottom_right = (-17.736736, -52.311547)
    bottom_left = (-17.039872, -60.437406)

    if (top_left[0] >= lat >= bottom_left[0]
            and top_right[0] >= lat >= bottom_right[0]):
        if (top_left[1] <= long <= top_right[1]
                and bottom_left[1] <= long <= bottom_right[1]):
            print('sucesso')


def main():
    check_coordinates(-15.592320, -56.086179)


if __name__ == '__main__':
    main()
