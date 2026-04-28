import requests
import psycopg2
from psycopg2.extras import execute_values
import datetime
import time 
import re

SEARCH_QUERIES = [
    'data engineer',
    'инженер данных',
    'dwh разработчик',
    'разработчик dwh',
    'хранилище данных',
    'etl разработчик',
    'big data инженер'
]

TECH_KEYWORDS = [
    # Базы данных
    'postgresql','greenplum','oracle','clickhouse','redis','t-sql','mssql','mysql',
    # ETL/Оркестрация
    'python','airflow','kafka','hadoop','dbt','spark',
    # Облака
    'aws','redshift','azure','bigquery',
    # DevOps
    'docker','terraform','kibernetes',
    # Визуализация
    'power bi','tableau'
]