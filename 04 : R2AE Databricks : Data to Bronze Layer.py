# Databricks notebook source
# DBTITLE 1,Read data from r2ae-data-landing to r2ae-data-bronze
input_csv_path = "s3://r2ae-data-landing-stellar/london_energy.csv"
output_s3_bucket = "s3://r2ae-data-bronze-stellar/london_energy/"

df = spark.read.csv(input_csv_path, header=True, inferSchema=True)
df.write.saveAsTable('r2ae.bronze.london_energy', format='delta', mode='overwrite', path=output_s3_bucket)

# COMMAND ----------

input_csv_path = "s3://r2ae-data-landing-stellar/london_weather.csv"
output_s3_bucket = "s3://r2ae-data-bronze-stellar/london_weather/"

df = spark.read.csv(input_csv_path, header=True, inferSchema=True)
df.write.saveAsTable('r2ae.bronze.london_weather', format='delta', mode='overwrite', path=output_s3_bucket)

# COMMAND ----------

# DBTITLE 1,With Delta Lake, we can track version of changes
# MAGIC %sql
# MAGIC DESCRIBE HISTORY r2ae.bronze.london_weather

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT COUNT(*) FROM r2ae.bronze.london_weather 

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT COUNT(*) FROM r2ae.bronze.london_weather VERSION AS OF 0
