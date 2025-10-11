from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'Cs340'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32145
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
        self.database = self.client['AAC']
        self.collection = self.database['animals']
        
        print(self.client.list_database_names())
        print(self.database.list_collection_names())
        print(self.collection.find_one())

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