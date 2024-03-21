#!/usr/bin/python3
"""This module creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects"""
	    """User Details:
		    email(str)
		    password(str)
		    user_first_name(str)
		    user_last_name(str)"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
