# Databricks notebook source
df1 = spark.sql("select * from roberto.testfinrec")
df2 = spark.sql("select * from roberto.testfinrec2")
df1rp = df1.repartition(2000, "join_id")
df2rp = df2.repartition(2000, "join_id")
display(df1rp)
display(df2rp)

# COMMAND ----------

dfjoin = df1rp.join(df2rp,df1rp.join_id ==  df2rp.join_id,"inner") 
display(dfjoin)
#very simple change here
# very simole change part 2
