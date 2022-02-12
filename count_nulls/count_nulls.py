
from pyspark.sql import functions as f
def cnt_nulls(sdf, column_name):
    num_nulls = sdf.where(f.col(column_name).isNull()).count()
    return num_nulls