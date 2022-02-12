
from pyspark.sql import functions as f
def nulls(sdf, column_name):
    num_nulls = sdf.where(f.col(column_name).isNull()).count()
    return num_nulls

if __name__ == '__main__' :
    nulls()