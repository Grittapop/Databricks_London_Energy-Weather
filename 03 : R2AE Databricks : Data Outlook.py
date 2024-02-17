# Databricks notebook source
# MAGIC %md
# MAGIC From now on DO NOT FORGET TO CHANGE SHANE TO YOUR BUCKET NAME (r2ae-data-landing-{YOUR NAME})

# COMMAND ----------

df = spark.read.csv("dbfs:/mnt/r2ae-data-landing-stellar/london_weather.csv",inferSchema=True,header=True)
display(df)

# COMMAND ----------

df = spark.read.csv("dbfs:/mnt/r2ae-data-landing-stellar/london_energy.csv",inferSchema=True,header=True)
display(df)
