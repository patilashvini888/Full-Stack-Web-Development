from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import *
from database_setup import Base, Category, CategoryItem
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Clear the tables if any table exists with same name.
session.query(Category).delete()
session.query(CategoryItem).delete()

# Add categories
sample_categories = ['Soccer', 'Basketball', 'Baseball', 'Frisbee',
                     'Snowboarding', 'Rock Climbing', 'Foosball', 'Skating',
                     'Hockey']

for category_name in sample_categories:
    category = Category(category_name)
    session.add(category)
session.commit()

# Add items
sample_items = {'Footwear': 1, 'Soccer Socks': 1, 'Shin Guard': 1,
                'Ball': 2, 'Basket/Hoop': 2, 'Backboard': 2, 'Bat': 3,
                'Ball': 3, 'Base': 3, 'Glove': 3, 'Disc': 4,
                'Knee Pads': 5, 'Helmet': 5, 'Rope': 6, 'Carabiners': 6,
                'Ball': 7, 'Gloves': 8, 'Mouth Guard': 9, 'Chest Pad': 9}

for item_title, item_category in sample_items.iteritems():
    item = CategoryItem(item_title, "Sample description", item_category)
    session.add(item)
session.commit()
