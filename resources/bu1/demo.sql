-- Databricks notebook source
-- Databricks notebook source
-- Create streaming table
CREATE OR REFRESH STREAMING TABLE st_orders
AS
SELECT * FROM STREAM(samples.tpch.orders)

-- COMMAND ----------

CREATE OR REPLACE VIEW agg_orders AS
SELECT
  count(o_orderkey) as cnt_orders,
  o_orderstatus
FROM samples.tpch.orders
GROUP BY o_orderstatus
