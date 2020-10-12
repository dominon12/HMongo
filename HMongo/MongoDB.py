from pymongo import MongoClient


class MongoDB:
    """
    [Class for work with database]
    """
    def __init__(self, cluster_path: str, db_name: str, **kwargs) -> None:
        """
        [Init func]

        Args:
            cluster_path ([str]): [Path to the mongo cluster]
            db_name ([str]): [Name of the db]
        """
        self.cluster_path = cluster_path
        self.cluster = MongoClient(self.cluster_path, **kwargs)
        self.db = self.cluster[db_name]

    def add_one(self, collection_name: str, object) -> None:
        """
        [Adds a new object to the db]

        Args:
            collection_name (str): [Name of the collection to which object must be added]
            object ([class]): [instance of the class you created]
        """
        new_object = object.__dict__
        collection = self.db[collection_name]
        collection.insert_one(new_object)

    def add_many(self, collection_name: str, objects: list) -> None:
        """
        [Adds new objects to the db]

        Args:
            collection_name (str): [Name of the collection to which objects must be added]
            objects (list): [List of class' instances]
        """
        new_objs = []
        for obj in objects:
            new_objs.append(obj.__dict__)
        collection = self.db[collection_name]
        collection.insert_many(new_objs)

    def get_one(self, collection_name: str, **kwargs) -> dict:
        """
        [Returns an object by keyword & value]

        Args:
            collection_name (str): [Name of the collection]
            **kwargs : [Filter parameters ("_id"=1234)]

        Returns:
            [dict]: [First object from the db which fits into the conditions]
        """
        collection = self.db[collection_name]
        obj = collection.find_one(kwargs)
        return obj

    def get_many(self, collection_name: str, **kwargs) -> dict:
        """
        [Returns list of objects by keyword & value]

        Args:
            collection_name (str): [Name of the collection]
            **kwargs : [Filter parameters ("_id"=1234)]

        Returns:
            [list]: [List of all objects which satisfies to filter parameters]
        """
        collection = self.db[collection_name]
        objs = collection.find(kwargs)
        return objs
        
    def get_all(self, collection_name: str) -> dict:
        """
        [Returns list of all objects without filtering from selected collection]

        Args:
            collection_name (str): [Name of the collection]

        Returns:
            [list]: [List of all objects from the selected collection]
        """
        collection = self.db[collection_name]
        objs = collection.find({})
        return objs

    def edit_one(self, collection_name: str, keyword: str, value: all, **kwargs) -> None:
        """
        [Edits one field of an object]

        Args:
            collection_name (str): [Name of the collection]
            keyword (str): [Key for filtering]
            value (all): [Value for filtering]
            **kwargs : [Key and value which must be edited ("username"="kraken")]
        """
        collection = self.db[collection_name]
        collection.update_one(
            {keyword: value}, {"$set": kwargs})

    def delete_one(self, collection_name: str, **kwargs) -> None:
        """
        [Deletes selected object]

        Args:
            collection_name ([str]): [Name of the collection]
            **kwargs : [Filter parameters]
        """
        collection = self.db[collection_name]
        collection.delete_one(kwargs)

    def delete_all_data(self, collection_name: str) -> None:
        """
        [Deletes all the data from the the selected collection]

        Args:
            collection_name (str): [Name of the collection]
        """
        collection = self.db[collection_name]
        collection.delete_many({})