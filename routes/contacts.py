
from fastapi import APIRouter,Response
from schemas.contact import contactEntity, contactsEntity
from typing import List
from config.db import dbc
from bson import ObjectId
from models.contact import Contact
from starlette.status import HTTP_204_NO_CONTENT


contact = APIRouter() #Initialize a route for contact

contacts = dbc["contacts"] #Create a collection for db "fastapi-contacts"

#Routes
@contact.get('/contacts',response_model=List[Contact],tags=['Contacts'])
def find_contacts():
    return contactsEntity(contacts.find())

@contact.post('/contacts',response_model=Contact,tags=['Contacts'])
def create_contact(contact:Contact):
    newContact = dict(contact)
    id = contacts.insert_one(newContact).inserted_id
    contact = contacts.find_one({"_id":id})
    return contactEntity(contact)

@contact.get('/contacts/{id}',response_model=Contact,tags=['Contacts'])
def get_contact(id:str):
    contact = contacts.find_one({"_id":ObjectId(id)})
    return contactEntity(contact)

@contact.put('/contacts/{id}',response_model=Contact,tags=['Contacts'])
def update_contact(id:str,contact:Contact):
    contacts.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(contact)})
    return contactEntity(contacts.find_one({"_id":ObjectId(id)}))

@contact.delete('/contacts/{id}',response_model=Contact,tags=['Contacts'])
def delete_contact(id:str):
    contacts.find_one_and_delete({"_id":ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)