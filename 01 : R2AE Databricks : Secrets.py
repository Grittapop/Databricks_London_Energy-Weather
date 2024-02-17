# Databricks notebook source
# DBTITLE 1,Check if databricks commands are ready
# MAGIC %sh
# MAGIC
# MAGIC databricks --version
# MAGIC

# COMMAND ----------

# DBTITLE 1,How many secret scope do we have ?
# MAGIC %sh
# MAGIC databricks secrets list-scopes
# MAGIC

# COMMAND ----------

# DBTITLE 1,Create secret scope
# MAGIC %sh
# MAGIC
# MAGIC databricks secrets create-scope --scope R2AE

# COMMAND ----------

# DBTITLE 1,Create S3_ACCESS_KEY
# MAGIC %sh
# MAGIC
# MAGIC databricks secrets put --scope R2AE --key S3_ACCESS_KEY --string-value xxxxxxxxxxxxxxxxxxxxx

# COMMAND ----------

# DBTITLE 1,Create S3_ACCESS_SECRET
# MAGIC %sh
# MAGIC
# MAGIC databricks secrets put --scope R2AE --key S3_ACCESS_SECRET --string-value xxxxxxxxxxxxxxxxxxxxxxxxxx

# COMMAND ----------

# MAGIC %sh
# MAGIC
# MAGIC databricks secrets list --scope R2AE
