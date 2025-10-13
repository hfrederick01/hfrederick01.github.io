#Programmer: Hannah Frederick
#Date:09/26/2025
#Program Description: Utilize a MongoDB shell to store the database and Dash to create a user-friendly dashboard that displays information from the database. The dashboard contains a dynamic geolocation map and pie chart that update based off the data shown in the table at the top of the page, which can be filtered using preset conditions at the top of the table. Additional filter options for each column using AgGrid are also available
#This page sets up and controls the CRUD functionality of the MongoDB database

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username, password, HOST, PORT, DB, COL):
        # Initialize Connection
        print("Connecting to MongoDB")
        self.client = MongoClient(f"mongodb://{username}:{password}@{HOST}:{PORT}/")
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("Connected to MongoDB")
        
        print(self.client.list_database_names())
        print(self.database.list_collection_names())


# Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            createSuccess = self.database.animals.insert_one(data)  
            # data should be dictionary
            
            #prints message to let the user know if create was successful or not
            if createSuccess.acknowledged: 
                print("Create successful") 
            else:
                 print("Create unsuccessful")
            return createSuccess.acknowledged #returns true if the create was acknowledged
        
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
# Read method to implement the R in CRUD
    def read(self, searchData):
        if searchData is not None:
            cursor = self.database.animals.find(searchData) #creates cursor with search data
            resultList = list(cursor) # makes a list of the cursor
            print("Read successful")
            return resultList #returns list if search is successful
        else:
            print("Search unsuccessful") #prints an error message and returns an emptry list if search is unsuccessful
            return []
        
# Update method to implement the U in CRUD.
    def update(self, oldData, updateData, updateAll = False):
        if updateData is not None and oldData is not None:
            if updateAll == False:
                updateResult = self.database.animals.update_one(oldData, {'$set': updateData})
            else:
                updateResult = self.database.animals.update_many(oldData, {'$set': updateData})
        else:
            raise Exception("Nothing to save, because update data parameter is empty")
        return updateResult.modified_count
    
# Delete method to implement the D in CRUD.
    def delete(self, deleteData, deleteAll = False):
        if deleteData is not None:
            if deleteAll == False:
                deleteResult = self.database.animals.delete_one(deleteData)
            else:
                deleteResult = self.database.animals.delete_many(deleteData)
        else:
            raise Exception("Nothing to delete, because delete data parameter is empty")
        return deleteResult.deleted_count