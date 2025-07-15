# Python script to connect to PostgreSQL using PySpark and perform basic operations

# import pyspark
import pyspark 
print('pyspark loaded')

#create spark session
spark = pyspark.sql.SparkSession \
    .builder \
    .appName("Spark SQL Basic Example") \
    .config("spark.driver.extraClassPath", "C:/Program Files/spark/spark-4.0.0-bin-hadoop3/jars/postgresql-42.7.7.jar") \
    .getOrCreate() 
print('spark configured')

##read the movies table from postgresql
movies = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/data_engineering") \
    .option("dbtable", "movies") \
    .option("user", "postgres") \
    .option("password", "4510") \
    .option("driver", "org.postgresql.Driver") \
    .load()
print('database connected')

#print the movies dataset
print(movies.show())

