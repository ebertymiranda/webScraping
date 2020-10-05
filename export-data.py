import pandas as pd
import json, os


def check_coordinates(lat, long):
    top_left = (-8.947866, -60.515091)
    top_right = (-9.836922, -50.416322)
    bottom_right = (-17.736736, -52.311547)
    bottom_left = (-17.039872, -60.437406)

    if (top_left[0] >= lat >= bottom_left[0]
            and top_right[0] >= lat >= bottom_right[0]):
        if (top_left[1] <= long <= top_right[1]
                and bottom_left[1] <= long <= bottom_right[1]):
            return True


def main():
    # check_coordinates(-15.592320, -56.086179)
    dados_nasa = 'Dados.csv'
    array = []

    #selecionadas apenas as colunas de latitude e longitude
    col_lat_long = pd.read_csv(dados_nasa, usecols=['latitude', 'longitude','acq_date'])

    for index, linha in col_lat_long.iterrows():
        if (check_coordinates(linha.latitude, linha.longitude)):
            array.append({"latitude":linha.latitude, "longitude": linha.longitude, "data":linha.acq_date})

    # convert into JSON:
    formatted_json = json.dumps(array)

    file = open("exported-data.json", "w")
    file.write(formatted_json);

    # the result is a JSON string:


if __name__ == '__main__':
    main()
