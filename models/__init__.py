import os

# Check the value of the environment variable
storage_type = os.getenv('HBNB_TYPE_STORAGE')

# Create an instance of the appropriate storage class based on the value
if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Execute the reload method after instantiation
storage.reload()