# Databricks notebook source
# DBTITLE 1,Clean data from Bronze and put it in Silver
from pyspark.sql.functions import col, to_date, from_unixtime

# COMMAND ----------

# DBTITLE 1,SELECT ALL FROM BRONZE TABLE {london_weather}
df_london_weather = spark.sql("SELECT * FROM r2ae.bronze.london_weather")
display(df_london_weather)

# COMMAND ----------

# DBTITLE 1,Clean data by converting date from this format {19790101} to this format {1979-01-01}
df_london_weather_silver = df_london_weather\
    .withColumn("date", to_date(col("date").cast("string"), 'yyyyMMdd'))\
    .withColumn("cloud_cover", col("cloud_cover").cast("decimal(6,2)"))\
    .withColumn("sunshine", col("sunshine").cast("decimal(6,2)"))\
    .withColumn("global_radiation", col("global_radiation").cast("int"))\
    .withColumn("max_temp", col("max_temp").cast("decimal(6,2)"))\
    .withColumn("mean_temp", col("mean_temp").cast("decimal(6,2)"))\
    .withColumn("min_temp", col("min_temp").cast("decimal(6,2)"))\
    .withColumn("precipitation", col("precipitation").cast("decimal(6,2)"))\
    .withColumn("pressure", col("pressure").cast("int"))\
    .withColumn("snow_depth", col("snow_depth").cast("int"))

# COMMAND ----------

display(df_london_weather_silver)

# COMMAND ----------

# DBTITLE 1,SELECT ALL FROM BRONZE TABLE {london_energy}
df_london_energy = spark.sql("SELECT * FROM r2ae.bronze.london_energy")
display(df_london_energy)

# COMMAND ----------

# DBTITLE 1,Clean data by changing proper column names and decimal points
df_london_energy_silver = df_london_energy\
    .withColumn("KWH", col("KWH").cast("decimal(6,2)"))\
    .withColumnRenamed("LCLid", "lcl_id")\
    .withColumnRenamed("Date", "date")\
    .withColumnRenamed("KWH", "kwh")

# COMMAND ----------

display(df_london_energy_silver)

# COMMAND ----------

df_london_weather_silver.write.saveAsTable('r2ae.silver.cleaned_london_weather', format='delta', mode='overwrite', path='s3://r2ae-data-silver-stellar/cleaned_london_weather')

# COMMAND ----------

df_london_energy_silver.write.saveAsTable('r2ae.silver.cleaned_london_energy', format='delta', mode='overwrite', path='s3://r2ae-data-silver-stellar/cleaned_london_energy')
