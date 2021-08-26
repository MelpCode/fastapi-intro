from fastapi import FastAPI
from routes.contacts import contact
from docs import tags_metadata

app = FastAPI(
    title="REST API WITH FASTAPI AND MONGODB",
    description="This is simple API with MongoDB",
    version="0.1",
    openapi_tags=tags_metadata
)

app.include_router(contact)