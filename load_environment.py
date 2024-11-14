from dotenv import load_dotenv
from snowflake.snowpark.session import Session
import os

load_dotenv()

connection_params = {
  "account":  os.getenv["SNOWFLAKE_ACCOUNT"],
  "user": os.getenv["SNOWFLAKE_USER"],
  "password": os.getenv["SNOWFLAKE_USER_PASSWORD"],
  "role": os.getenv["SNOWFLAKE_ROLE"],
  "database": os.getenv["SNOWFLAKE_DATABASE"],
  "schema": os.getenv["SNOWFLAKE_SCHEMA"],
  "warehouse": os.getenv["SNOWFLAKE_WAREHOUSE"]
}

snowpark_session = Session.builder.configs(connection_params).create()
