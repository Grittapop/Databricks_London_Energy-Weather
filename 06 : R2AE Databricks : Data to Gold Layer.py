# Databricks notebook source
# DBTITLE 1,Join 2 silver tables by dates
df_london_weather_silver = spark.sql("SELECT * FROM r2ae.silver.cleaned_london_weather")

df_london_energy_silver = spark.sql("SELECT * FROM r2ae.silver.cleaned_london_energy")

df_energy_comsumption_trend = df_london_energy_silver.join(df_london_weather_silver, on=["date"], how="left")

# COMMAND ----------

# MAGIC %md
# MAGIC First three columns are from cleaned_london_energy, the others are from cleaned_london_weather

# COMMAND ----------

display(df_energy_comsumption_trend)

# COMMAND ----------

df_energy_comsumption_trend.write.saveAsTable('r2ae.gold.london_energy_consumption_trend', format='delta', mode='overwrite', path='s3://r2ae-data-gold-stellar/london_energy_consumption_trend')
