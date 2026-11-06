import json
from typing import Any

def build_well_passport() -> dict[str, Any]:
    """Создаёт словарь паспорта скважины с индивидуальными данными пары."""
    return {
        "well_id": "W-115",
        "field_name": "Кампусовское",
        "depth_m": 2000,
        "q_liq": 115.0,
        "w_pct": 42.0,
        "is_active": True,
        "pump": {
            "model": "ЭЦН5-80-1800",
            "power_kw": 90.0,
        },
    }
def save_to_json(data: dict[str, Any], filename: str = "data.json") -> None:
    """Сериализует словарь Python в текстовый файл формата JSON."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_from_json(filename: str = "data.json") -> dict[str, Any]:
    """Десериализует (читает) JSON-файл с диска обратно в словарь Python."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def print_passport_summary(passport: dict[str, Any]) -> None:
    """Выводит красивую сводку по прочитанному из JSON паспорту и считает дебит чистой нефти."""
    q_oil = passport["q_liq"] * (1.0 - passport["w_pct"] / 100.0)
    pump_info = passport["pump"]
    print("=" * 56)
    print(f"ПАСПОРТ СКВАЖИНЫ ИЗ JSON: {passport['well_id']}")
    print("=" * 56)
    print(f"Месторождение:{passport['field_name']}")
    print(f"Глубина: {passport['depth_m']} м")
    print(f"Дебит жидкости: {passport['q_liq']:.2f} м3/сут (обводнённость {passport['w_pct']:.1f}%)")
    print(f"Расчёт чистой нефти: {q_oil:.2f} м3/сут")
    print(f"Насосная установка: {pump_info['model']} (мощность {pump_info['power_kw']} кВт)")
    print("=" * 56)

if __name__ == "__main__":
    # 1. Формируем словарь в памяти Python
    my_passport = build_well_passport()

    # 2. Сохраняем его в файл data.json (сериализация)
    save_to_json(my_passport, "data.json")
    print("[OK] Файл 'data.json' успешно записан на диск!")

    # 3. Читаем файл обратно с диска (десериализация) и проверяем, что данные не потерялись
    loaded_passport = load_from_json("data.json")
    assert loaded_passport == my_passport, "Ошибка: прочитанный словарь не совпадает с исходным!"
    print("[OK] Обратное чтение через json.load() прошло без потерь!")

    # 4. Печатаем инженерную сводку по прочитанным данным
    print_passport_summary(loaded_passport)
