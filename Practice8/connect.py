import psycopg2
from config import config

conn = psycopg2.connect(**config())
cursor = conn.cursor()
