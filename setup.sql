USE ROLE ACCOUNTADMIN;

CREATE OR REPLACE WAREHOUSE LLMOPS_WH_M WAREHOUSE_SIZE=MEDIUM;
CREATE OR REPLACE DATABASE LLMOPS_DB;
CREATE OR REPLACE SCHEMA LLMOPS_SCHEMA;

USE LLMOPS_DB.LLMOPS_SCHEMA