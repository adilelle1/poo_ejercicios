import pandas as pd
import numpy as np
import datetime


def transformar_columnas_datetime(dataframe):
    columns = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date',
               'order_delivered_customer_date', 'order_estimated_delivery_date']
    for column in columns:
        dataframe[column] = pd.to_datetime(dataframe[column])


def calcular_diferencia_de_timestamps(dataframe, new_column_name, column1, column2):
    dataframe[new_column_name] = dataframe[column1] - dataframe[column2]


def tiempo_de_espera(dataframe, is_delivered):
    one_day_delta = np.timedelta64(24, 'h')

    if is_delivered:
        dataframe.loc[dataframe.order_status == 'delivered', 'dias_de_espera'] = \
            (dataframe['order_delivered_customer_date'] - dataframe['order_purchase_timestamp']) / one_day_delta



def real_vs_esperado(dataframe, is_delivered=True):
    one_day_delta = np.timedelta64(24, 'h')
    if is_delivered:
        dataframe.loc[dataframe.order_status == 'delivered', 'real_vs_esperado'] = \
            (dataframe['order_estimated_delivery_date'] - dataframe['order_delivered_customer_date']) / one_day_delta
        dataframe.loc[dataframe.order_status != 'delivered', 'real_vs_esperado'] = 0


def real_vs_esperado_positivo(dataframe):
    dataframe.loc[dataframe.real_vs_esperado <= 0, 'real_vs_esperado'] = 0


'''
def puntaje_de_compra(dataframe):
    dataframe['es_cinco_estrellas'] = 0
    dataframe['es_cuatro_estrellas'] = 0
    dataframe['es_tres_estrellas'] = 0
    dataframe['es_dos_estrellas'] = 0
    dataframe['es_una_estrellas'] = 0
    dataframe['es_cero_estrellas'] = 0

    dataframe.review_score.apply(lambda x: dataframe['es_cinco_estrellas'] = 1 if x == 5 \
        else dataframe['es_cuatro_estrellas'] = 1 if x == 4 \
        else dataframe['es_tres_estrellas'] = 1 if x == 3 \
        else dataframe['es_dos_estrellas'] = 1 if x == 2 \
        else dataframe['es_una_estrellas'] = 1 if x == 1 \
        else dataframe['es_cero_estrellas'] = 1)

    reviews = dataframe[['order_id', 'es_cinco_estrellas', 'es_una_estrella', 'review_score']].copy()
    return reviews
'''


def puntaje_de_compra(dataframe):
    review_score_dummies = pd.get_dummies(dataframe.review_score, drop_first=False, prefix='estrellas')
    dataframe = dataframe.join(review_score_dummies)
    dataframe = dataframe[['order_id', 'estrellas_5', 'estrellas_1', 'review_score']].copy()
    return dataframe


def calcular_numero_productos(dataframe1, dataframe2):
    data = dataframe1.join(dataframe2, )
