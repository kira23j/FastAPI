import fastapi
router=fastapi.APIRouter()

@router.get("/sections/:id")
async def read_section():
    return {"cources":[]}

@router.get("/sections/:id/content-block")
async def read_content_block():
    return {"cources":{}}