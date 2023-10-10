from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class ScrapedData(Base):
    __tablename__ = 'data'
    id = Column(Integer, Sequence('data_id_seq'), primary_key=True)
    content = Column(String)

engine = create_engine('sqlite:///scraped_data.db')
Session = sessionmaker(bind=engine)

def store_data_in_db(data_list):
    session = Session()
    for data in data_list:
        new_data = ScrapedData(content=data)
        session.add(new_data)
    session.commit()
    session.close()
