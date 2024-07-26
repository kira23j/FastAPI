import fastapi

router=fastapi.APIRouter()

@router.get("/cources")
async def read_cources():
    return {"cources":[]}

@router.post("/cources")
async def create_cource():
    return {"cources":[]}

@router.get("/cources/{ud}")
async def read_cource():
    return {"cources":[]}

@router.patch("/cources/{id}")
async def update_cource():
    return {"cources":[]}


@router.delete("/cources/{id}")
async def delete_cource():
    return {"cources":[]}