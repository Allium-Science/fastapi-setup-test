from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
async def world():
    return "world"
