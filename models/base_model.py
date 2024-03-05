#!/usr/bin/python3
"""
Write a class BaseModel that defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ The BaseModel class defines all common 
        attributes/methods for other classes 
    """
    def __init__(self, *args, **kwargs) -> None:
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.fromisoformat(val))
                    else:
                        setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        
    def __str__(self):
        """override the __str__ method so it returns [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """returns a dictionary containing all key/value pairs of __dict__ of the instance"""
        attrs = {k: getattr(self, k) for k in self.__dict__}
        attrs["created_at"] = self.created_at.isoformat()
        attrs["updated_at"] = self.updated_at.isoformat()
        attrs["__class__"] = f"{self.__class__.__name__}"
        return attrs
