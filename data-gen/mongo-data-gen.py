#!/bin/env python3
##
##  Generate fake data for mongo db test
##
import os
from asyncio import sleep
from pymongo import MongoClient
from faker import Faker

# Initialize Faker instance
fake = Faker(['en_US', 'fr_FR', 'pl_PL'])  # You can add more locales if needed

username = os.getenv('MONGO_USERNAME', 'default_username')
password = os.getenv('MONGO_PASSWORD', 'default_password')
auth_database = os.getenv('MONGO_AUTH_DATABASE', 'admin')
mongo_host = os.getenv('MONGO_HOST', 'localhost')
mongo_port = os.getenv('MONGO_PORT', '27017')

# MongoDB connection setup
client = MongoClient(f"mongodb://{username}:{password}@{mongo_host}:{mongo_port}/{auth_database}")
db = client['test_database']
collection = db['profiles_collection']

# Function to generate and insert random data (e.g., names, addresses) into MongoDB
def insert_random_profiles(n):
    for _ in range(n):
        profile = {
            "name": fake.name(),
            "address": fake.address(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "job": fake.job(),
            "birthdate": fake.date_of_birth(),
            "company": fake.company(),
            "ssn": fake.ssn()  # US Social Security Number
        }

        # Insert the random profile into MongoDB
        collection.insert_one(profile)

# Insert 10 random profiles
while True:
    insert_random_profiles(100)
    sleep(5)

# Close MongoDB connection
client.close()
