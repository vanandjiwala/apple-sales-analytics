import duckdb

query = "SELECT  * FROM ref_model";

with duckdb.connect('data/apple-retail.db') as con:
    print(con.sql(query=query).df())