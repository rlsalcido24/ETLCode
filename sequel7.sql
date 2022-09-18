
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