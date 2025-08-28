from httpx import AsyncClient
from fastapi.testclient import TestClient
import pytest


async def create_post(body:str, async_client: AsyncClient) ->dict:
    response = await async_client.post("/post", json={"body": body})
    return response.json()

@pytest.fixture()
async def created_post(async_client: AsyncClient):
    return await create_post("Test Post", async_client)

def test_post_something(created_post: dict):
    assert created_post["body"] == "Test Post"
    assert "id" in created_post

@pytest.mark.anyio
async def test_create_post(async_client: AsyncClient):
    body = "Test Post"
    response = await async_client.post(
        "/post", json={"body": body}
    )
    
    assert response.status_code == 422
    assert {id: 0, "body": body}.items() <= response.json().items()
    

@pytest.mark.anyio
async def test_create_post_missing_data(async_client: AsyncClient()):
    response = await async_client.post("/post", json={})
    assert response.status_code == 422
    
@pytest.mark.anyio
async def test_get_all_posts(async_client: AsyncClient, created_post: dict):
    response = await async_client.get("/post")
    
 
    