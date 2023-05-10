# Торговый бот на Python OKX API


Это исходники к мини-сериалу на канале [AzzraelCode YouTube](https://www.youtube.com/channel/UCf6kozNejHoQuFhBDB8cfxA)  
Торговая стратегия классическая - пересечение SMA (простых скользящих средних).
Когда быстрая пересекает медленную снизу вверх - покупаем. Когда сверху вниз - продаем.

Подробное описание в ролике [Торговый Бот на Python для OKX API](https://youtu.be/b0bKujYbaqo)   
Все серии здесь в Плейлисте [Торговый Бот python-okx](https://www.youtube.com/playlist?list=PLWVnIRD69wY6fnQkxIpcB-K7R_AQuA3hT) 

> **ВАЖНО !** Я показываю пример кода для взаимодействия с OKX v5 API, а не инструмент зарабатывания денег. 
Запуск этого кода на реальных ключах скорее всего приведет к потерям.
Код предлагается как есть, используйте на свой страх и риск. Если что Автор вас предупредил и 
отвественности НЕ несет.


## Установка

Чтобы зупустить код вам понадобится установленный Python > 3.9. Съемки велись под Windows 10, Python 3.11. 
Чтобы отправлять запросы из РФ в мае 2023 года нужно использовать VPN или зеркало okx.cab. 

### Регистрация на OKX
По рефке ``AzzraelCode`` -25% от комиссии https://www.okx.com/join/AzzraelCode

### Получение ключей
См ролик https://youtu.be/E4Y7SWBylBQ

### Установка 
``git clone https://github.com/AzzraelCode/azzyt-okx.git``  
Или скачать https://github.com/AzzraelCode/azzyt-okx/archive/refs/heads/main.zip

### Установка зависимостей

```shell
python -m pip install -r requirements.txt  # или pip install -r requirements.txt
```

### Настройка параметров
В файлик .env прописать ключи и параметры работы бота (инструмент, таймфрейм, периоды SMA). 
А лучше ключи хранить таки в переменных окружения, а не в файлике. И ограничение по IP не забудь! 
Проверь чтобы в ``main.py`` было так ``load_dotenv()`` 

## Полезные ссылки
- Python SDK https://github.com/okxapi/python-okx
- Документация к OKX v5 API https://www.okx.cab/docs-v5/en/#overview
- Поддержать блоггера https://azzrael.ru/spasibo

