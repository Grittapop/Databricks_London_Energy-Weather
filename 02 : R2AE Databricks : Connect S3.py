# Databricks notebook source
# DBTITLE 1,Pull secrets without explicitly exposing them in the notebook
s3_access_key = dbutils.secrets.get(scope="R2AE", key="S3_ACCESS_KEY")
s3_access_secret = dbutils.secrets.get(scope="R2AE", key="S3_ACCESS_SECRET")

# COMMAND ----------

# DBTITLE 1,Set up configurations
sc._jsc.hadoopConfiguration().set("fs.s3a.access.key",s3_access_key)
sc._jsc.hadoopConfiguration().set("fs.s3a.secret.key",s3_access_secret)
sc._jsc.hadoopConfiguration().set("fs.s3a.endpoint","s3.ap-southeast-1.amazonaws.com")

# COMMAND ----------

# MAGIC %md
# MAGIC From now on DO NOT FORGET TO CHANGE SHANE TO YOUR BUCKET NAME (r2ae-data-landing-{YOUR NAME})

# COMMAND ----------

# DBTITLE 1,Try reading Data from S3 to see if Databricks connects to S3 properly 
df = spark.read.csv("s3://r2ae-data-landing-stellar/london_weather.csv",inferSchema=True,header=True)
df.show()

# COMMAND ----------

display(df)

# COMMAND ----------

# DBTITLE 1,Mount DBFS with S3
aws_bucket_name = "r2ae-data-landing-stellar"
mount_name = "r2ae-data-landing-stellar"
dbutils.fs.mount(f"s3a://{aws_bucket_name}", f"/mnt/{mount_name}")
display(dbutils.fs.ls(f"/mnt/{mount_name}"))

# COMMAND ----------

df = spark.read.csv("dbfs:/mnt/r2ae-data-landing-stellar/london_weather.csv",inferSchema=True,header=True)
display(df)
