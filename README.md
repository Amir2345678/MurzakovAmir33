# Цифровой паспорт нефтяной скважины и погружного насоса

# Чернов Дмитрий Павлович - разработчик
# Мурзаков Амир Денисович - аналитик


# Рассчёт индивидуальных данных

N1 = 31
N2 = 19
N = 50
well_id = f"W-{100 + N}" = W - 150
field_name = "Кампусовское"
depth_m = 1500 + 50 * (N % 40) = 2000
q_liq = 45.0 + 3.5 * (N % 30) = 115.0
w_pct = 12.0 + 2.0 * (N % 35) = 42.0
power_kw = 40.0 + 5.0 * (N % 20) = 90.0


```mermaid
erDiagram
 WELL_PASSPORT ||--|| PUMP_UNIT : "содержит (pump)"
 WELL_PASSPORT {
 string well_id "Код скважины"
 string field_name "Название месторождения"
 integer depth_m "Глубина, м"
 number q_liq "Дебит жидкости, м3/сут"
 number w_pct "Обводненность, %"
 boolean is_active "Статус активности"
 }
 PUMP_UNIT {
 string model "Модель насоса ЭЦН"
 number power_kw "Мощность, кВт"
 }