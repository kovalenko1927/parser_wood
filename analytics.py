import pandas as pd


def perform_analysis(data_set):
    data = pd.read_csv(data_set)

    product_count = len(data.index)
    count_org = len(data[data['category'] == 'Органайзери'])
    count_it = len(data[data['category'] == 'Інформаційні таблички'])
    count_sptv = len(data[data['category'] == 'Стелажі, полички, тумби та вітрини'])
    count_q = len(data[data['category'] == 'QR-коди'])
    count_bm = len(data[data['category'] == 'Багаторазове меню'])
    count_nb = len(data[data['category'] == 'Набірне меню'])
    count_n = len(data[data['category'] == 'Наліпки'])
    count_bar = len(data[data['category'] == 'Професійні інструменти бариста'])
    count_fb = len(data[data['category'] == 'Футболки з брендуванням'])
    count_r = len(data[data['category'] == 'Різне'])
    count_nocat = len(data[data['category'] == 'Без категорії'])

    mid_price = data['price'].median()

    print(f"Загальна кількість товарів: {product_count} | Середня вартість: {mid_price}")
    print("----------------------------")
    print("По категоріям:")
    print(f"'Органайзери' - {count_org}")
    print(f"'Іформаційні таблички' - {count_it}")
    print(f"'Стелажі, полички, тумби та вітрини' - {count_sptv}")
    print(f"'QR-коди' - {count_q}")
    print(f"'Багаторазове меню' - {count_bm}")
    print(f"'Набірне меню' - {count_nb}")
    print(f"'Наліпки' - {count_n}")
    print(f"'Професійні інструменти бариста' - {count_bar}")
    print(f"'Футболки з брендуванням' - {count_fb}")
    print(f"'Різне' - {count_r}")
    print("----------------------------")
    print(f"Товарів без категорії: {count_nocat}")


def main():
    data_set = 'products.csv'
    perform_analysis(data_set)


if __name__ == "__main__":
    main()
