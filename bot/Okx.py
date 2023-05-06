import logging
import os

import pandas as pd
from okx.Account import AccountAPI
from okx.MarketData import MarketAPI
from okx.Trade import TradeAPI

logger = logging.getLogger('azzraelcode-yt')

class Okx:
    """
    Класс OKX реализует логику взаимодействия с биржей ОКХ
    торговой логике в нем нет
    """
    def __init__(self):
        logger.info(f"{os.getenv('NAME', 'Anon')} OKX Auth loaded")

        # загрузка значения из переменных окружения,
        # чтобы при изменении окружения после запуска бота, бот продолжал нормально работать
        self.symbol = os.getenv('SYMBOL')
        self.qty = float(os.getenv('QTY'))

        # На данный момент SDK python-okx предоставляет отдельные классы к каждой секции
        # вместо единого клиента (хотя он в SDK есть, поэтому, надеюсь такой расклад не надолго)
        # чтобы не дублировать параметры для каждого класса - в конструкторе инициализирую словарь настроек
        self.params = dict(
            domain='https://www.okx.cab',
            flag=os.getenv('IS_DEMO', '1'),
            api_key=os.getenv('API_KEY', '1'),
            api_secret_key=os.getenv('SECRET', '1'),
            passphrase=os.getenv('PASSPHRASE', '1'),
            debug=False
        )

    def check_permissions(self):
        """
        Простой запрос к состоянию баланса Аккаунта
        для проверки прав доступа предоставленных ключей,
        если ключи не правильные выкинет ошибку

        :raises: OkxAPIException
        :return:
        """
        r = AccountAPI(**self.params).get_account_balance()

    def close_prices(self, instId, timeframe='1m', limit = 100):
        """
        Возвращаю серию цен закрытия (close) Pandas для обработки в библиотеке ta
        :param timeframe:
        :param instId:
        :param limit:
        :return:
        """
        klines = MarketAPI(**self.params).get_candlesticks(instId, limit=limit, bar=timeframe).get('data', [])
        klines.reverse()
        return pd.Series([float(e[4]) for e in klines])


    def place_order(self, side):
        """
        Размещение заявки
        :param side:
        :return:
        """
        r = TradeAPI(**self.params).place_order(
            instId=self.symbol,
            tdMode='cash',
            side=side,
            ordType='market',
            sz=self.qty,
            tgtCcy='base_ccy'
        )

        if r.get('code') == '0':
            # ордер успешно отправлен (но не обязательно исполнен)
            order_id = r.get('data', [])[0].get('ordId')
            logger.info(f"{side} {order_id}")
        else: logger.error(r)

        return r
