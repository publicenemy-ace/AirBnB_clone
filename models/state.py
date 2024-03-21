#!/usr/bin/python3
"""This module creates a User class"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class for managing state objects"""
	    """ Represents a State
	name(str): The name of the state"""

    name = ""
