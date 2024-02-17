# Databricks notebook source
# DBTITLE 1,Introduction to Databricks Notebook
print("Welcome to Databricks")

# COMMAND ----------

print("Welcome to R2AE")

# COMMAND ----------

print("Databricks has launched the new UI")

# COMMAND ----------

# DBTITLE 1,Use dbutils to list all files in Databricks Storage
dbutils.fs.ls("/")

# COMMAND ----------

# DBTITLE 1,Use dbutils to obtain Notebook parameters
dbutils.widgets.text("name", "Stellar")
dbutils.widgets.dropdown("country", "Thailand", ["Thailand", "Malaysia", "Indonesia"])

# COMMAND ----------

name = dbutils.widgets.get("name")
country = dbutils.widgets.get("country")
print(f"Hello {name} I'm from {country}")

# COMMAND ----------

dbutils.widgets.removeAll()

# COMMAND ----------

# DBTITLE 1,Use Magic commands to change language execution of a cell
# MAGIC %sh
# MAGIC
# MAGIC echo "Welcome to Databricks"
# MAGIC ls

# COMMAND ----------

# MAGIC %sql
# MAGIC select 1 As1

# COMMAND ----------

# MAGIC %scala
# MAGIC println("Welcome to Databricks")

# COMMAND ----------

# MAGIC %md
# MAGIC # Header 1
# MAGIC ## Header 2
# MAGIC
# MAGIC **bold text**
# MAGIC
# MAGIC *italics text*
# MAGIC
# MAGIC ~~strikethrough text~~
# MAGIC
# MAGIC `monospace text`
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC > Block quote
# MAGIC
# MAGIC Ordered list:
# MAGIC 1. Item 1
# MAGIC 1. Item 2
# MAGIC 1. Item 3
# MAGIC
# MAGIC Unordered list:
# MAGIC - Item a
# MAGIC - Item b
# MAGIC - Item c
# MAGIC
