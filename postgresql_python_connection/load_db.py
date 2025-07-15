# Python script to connect to PostgreSQL using PySpark and perform basic operations
# here I loaded back the transformaed table (df) in the postresql database

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

#read the movies table from postgresql
def extract_movies_table():
    movies = spark.read \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/data_engineering") \
        .option("dbtable", "movies") \
        .option("user", "postgres") \
        .option("password", "4510") \
        .option("driver", "org.postgresql.Driver") \
        .load()
    return movies
    


#read the ratings table from postgresql
def extract_ratings_table():
    ratings = spark.read \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/data_engineering") \
        .option("dbtable", "ratings") \
        .option("user", "postgres") \
        .option("password", "4510") \
        .option("driver", "org.postgresql.Driver") \
        .load()
    return ratings

# transforming average ratings
def transform_average_ratings(movies, ratings):
    average_ratings = ratings.groupby('id').mean('rating')
    df = movies.join(average_ratings, movies.id == average_ratings.id)
    df = df.drop('id')
    return df

# load the df table back to postgresql database
def load_df_to_postgresql(df):
    mode = "overwrite"
    url = "jdbc:postgresql://localhost:5432/data_engineering"
    properties = {
        "user", "postgres",
        "password", "4510",
        "driver", "org.postgresql.Driver"
        }
    df.write.jdbc(
        url = url,
        table = "average_ratings",
        properties = properties
        )

if __name__ == "__main_":
    movies = extract_movies_table()
    ratings = extract_ratings_table()
    average_ratings = transform_average_ratings(movies, ratings)
    load_df_to_postgresql(average_ratings)

print('All functions executed')