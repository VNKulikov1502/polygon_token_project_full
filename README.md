API-сервер на Django + DRF для взаимодействия с токеном `TBY` (Storage Gastoken V3) в сети **Polygon**  
Контракт токена: `0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0`
(Переменная окружения .env осталась специально)
---

## Запуск

```bash
# Установить зависимости
pip install -r requirements.txt

# Установить переменную окружения
export POLYGONSCAN_API_KEY=your_api_key

# Запуск сервера
python manage.py runserver

# Polygon Token API

## Эндпоинты

1. GET /api/get_balance/?address=<адрес>

- Получить баланс токена у одного адреса.

Пример:
GET /api/get_balance/?address=0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0

Ответ:
{
  "balance": 3.2680318192644577
}

---

2. POST /api/get_balance_batch/

- Получить балансы токена у нескольких адресов.

Тело запроса:
{
  "addresses": [
    "0x51f1774249Fc2B0C2603542Ac6184Ae1d048351d",
    "0x4830AF4aB9cd9E381602aE50f71AE481a7727f7C"
  ]
}

Ответ:
{
  "balances": [0.01, 0.01]
}

---

3. GET /api/get_top/?n=<число>

- Получить топ n адресов с максимальным балансом токена.

Пример:
GET /api/get_top/?n=3

Ответ:
{
  "top_holders": [
    ["0x0000...", 0.01],
    ["0x1111...", 0.005],
    ["0x2222...", 0.002]
  ]
}

---

4. GET /api/get_top_with_last_tx/?n=<число>

- Получить топ n адресов с балансами и датами последних транзакций.

Пример:
GET /api/get_top_with_last_tx/?n=2

Ответ:
{
  "top_with_last_tx": [
    ["0x0000...", 0.01, "2024-11-12T12:33:00"],
    ["0x1111...", 0.005, "2024-08-20T08:44:12"]
  ]
}

---

5. GET /api/get_token_info/

- Получить информацию о токене.

Пример:
GET /api/get_token_info/

Ответ:
{
  "symbol": "TBY",
  "name": "Storage Gastoken V3",
  "totalSupply": 9988413140122608420902
}
