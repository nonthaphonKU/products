from pymongo import MongoClient

client = MongoClient("theory.cpe.ku.ac.th", username="user07", password="pass07")
db = client.db07
products = db.products

for p in products.find():
    print(p["name"], p["price"])

# Add comment here!