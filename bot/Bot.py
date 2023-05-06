import logging
import os
from time import sleep
import ta.trend

from bot.Okx import Okx

logger = logging.getLogger('azzraelcode-yt')

class Bot(Okx):
    """
    Класс Bot реализует логику торговли,

    а методы взаимодествия с биржей OKX наследуются из класса OKX (декомпозиция)
    при желании можно наследоваться от класса где будет реализовано взаимодействие
    или с др биржей, или с др секцией биржи (фиючерсы)

    """

    def __init__(self):
        super(Bot, self).__init__()

        # загрузка значения из переменных окружения,
        # чтобы при изменении окружения после запуска бота, бот продолжал нормально работать
        self.timeout = int(os.getenv('TIMEOUT', 60))
        self.timeframe = os.getenv('TIMEFRAME', '1m')
        self.sma_fast = int(os.getenv('SMA_FAST', '14'))
        self.sma_slow = int(os.getenv('SMA_SLOW', '28'))

    def is_cross(self):
        """
        Определяю пересечение простых скользящих средних
        Возвращает:
         0 - если на текущем баре пересечения нет
         1 - быстрая пересекает медленную снизу вверх, crossover, сигнал на покупку
        -1 - быстрая пересекает медленную снизу вверх, crossover, сигнал на продажу
        :return:
        """
        # Серия Пандас с ценами закрытия, в обратном (для ОКХ) порядке
        close = self.close_prices(self.symbol, self.timeframe)

        # Расчет простых скользящих средних,
        # более свежие значение в конце списка
        # нам нужны 2 последних значения
        fast = ta.trend.sma_indicator(close, self.sma_fast).values
        slow = ta.trend.sma_indicator(close, self.sma_slow).values

        r = 0
        if   fast[-1] > slow[-1] and fast[-2] < slow[-2]: r = 1 # crossover быстрая снизу вверх
        elif fast[-1] < slow[-1] and fast[-2] > slow[-2]: r =-1 # crossunder быстрая свверху вниз

        if r != 0: logger.info(f"{r} = now {fast[-1]:.6f} / {slow[-1]:.6f}, prev {fast[-2]:.6f} / {slow[-2]:.6f}")
        return r

    def check(self):
        """
        Проверка сигналов и постановка ордеров

        !! ВАЖНО !!

        :return:
        """
        try:
            cross = self.is_cross()

            if cross > 0 and not self.is_position():
                self.place_order('buy')
            elif cross < 0 and self.is_position():
                self.place_order('sell')

        except Exception as e:
            logger.error(str(e))

    def loop(self):
        """
        Цикл проверки.
        Лучше таки это делать опрос не в цикле, а использовать Websocket
        :return:
        """
        while True:
            self.check()
            sleep(self.timeout)

    def run(self):
        """
        Инициализация бота
        :return:
        """
        logger.info("The Bot is started!")
        self.check_permissions()

        # Можно запускать вечный цикл, если бот локально
        self.loop()
        # Или дергать по крону на ВДСке, по триггеру в Cloud Functions ...
        # self.check()

