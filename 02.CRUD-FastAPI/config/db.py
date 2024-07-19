from sqlalchemy import create_engine, MetaData
engine=create_engine("sqlmysql+pymsql://root@localhost:3306/sample")
meta=MetaData()
conn=engine.connect()