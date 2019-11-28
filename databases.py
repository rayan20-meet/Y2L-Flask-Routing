from model import *
from sqlalchemy.pool import SingletonThreadPool

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlite3

conn = sqlite3.connect('databases.py')

engine = create_engine('sqlite:///database.db',poolclass=SingletonThreadPool)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name,price,pictureLink,description):

	Product_object = Product(
		name=name,
		price=price,
		pictureLink=pictureLink,
		description=description)
	session.add(Product_object)
	session.commit()


def update_product(name,price,pictureLink,description,id):

	Product = session.query(Product).filter_by(id=id).first()
	Product.name=name
	Product.price=price
	product.pictureLink=pictureLink
	description=description
	product.id=id

	session.commit()


def delete_product(their_id):

	session.query(Product).filter_by(id=their_id).delete()
	session.commit()


def query_all():

	return session.query(Product).all()
	

def specific_product(its_id):
	return session.query(Product).filter_by(id=its_id)


def Add_To_Cart(productID):
	productID_object = Cart()
	productID_object.productID = productID
	session.add(productID_object)
	session.commit()

# add_product("Scarf",500,"temp","Very warm")