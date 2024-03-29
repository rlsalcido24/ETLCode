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

# COMMAND ----------

string = """
-- Databricks notebook source

CREATE LIVE TABLE customers
COMMENT "The customers buying finished products, ingested from /databricks-datasets."
TBLPROPERTIES ("quality" = "mapping")
AS SELECT * FROM robertotpch.customers c
order by c.customer_key

-- COMMAND ----------


CREATE LIVE TABLE customers
COMMENT "The customers buying finished products, ingested from /databricks-datasets."
TBLPROPERTIES ("quality" = "mapping")
AS SELECT * FROM robertotpch.customers c
order by c.customer_key


-- COMMAND ----------

CREATE LIVE TABLE orders
COMMENT "Orders"
TBLPROPERTIES ("quality" = "mapping")
AS SELECT * FROM robertotpch.orders o
order by o.order_date


"""

# COMMAND ----------

f = open("sequel7.sql", "w")
f.write(string)
f.close()

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC ls

# COMMAND ----------


