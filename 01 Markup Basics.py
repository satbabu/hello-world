# Databricks notebook source
# This is a comment text
print("Hello World 2024!")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Hello world from SQL languague!"

# COMMAND ----------

# MAGIC %md
# MAGIC #Notepad Basics
# MAGIC ##Title1
# MAGIC ###Title2
# MAGIC
# MAGIC Tutorial: https://www.databricks.com/resources/demos/videos/developer-experience/notebook-basics#:~:text=What%20you'll%20learn,the%20Databricks%20Industry%20Solution%20Accelerators.
# MAGIC
# MAGIC ##Databricks:
# MAGIC ![Associate-badge](https://www.databricks.com/wp-content/uploads/2022/04/associate-badge-eng.svg)
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

# MAGIC %run ./includes/config

# COMMAND ----------

print("This notebook user is " + user + " and he is using it for " + use)

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.fs.help("ls")

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/Workspace/Repos/"))
