import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(file_path):
    """Загрузка данных из CSV файла."""
    if not os.path.exists(file_path):
        print(f"Ошибка: файл {file_path} не найден!")
        return None
    
    try:
        data = pd.read_csv(file_path, encoding="utf-8")
        return data
    except Exception as e:
        print("Ошибка при загрузке данных:", e)
        return None

def analyze_data(df):
    """Проводит базовый анализ данных и строит визуализацию."""
    print("Статистика по данным:")
    print(df.describe())

    if "id" not in df.columns or "value" not in df.columns:
        print("Ошибка: Ожидаемые столбцы 'id' и 'value' отсутствуют в данных!")
        return

    plt.figure(figsize=(10, 5))
    plt.bar(df["id"], df["value"], color="skyblue", edgecolor="black")
    plt.xlabel("ID")
    plt.ylabel("Значение")
    plt.title("Диаграмма значений по ID")
    plt.xticks(df["id"])  # Устанавливаем подписи ID

    plt.show()

def main():
    file_path = "../data/data.csv"  # Исправленный путь
    df = load_data(file_path)
    if df is not None:
        analyze_data(df)

if __name__ == "__main__":
    main()
