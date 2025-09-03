from fastapi import FastAPI

from fastapi_setup_test.app.routes.hello_world import router

app = FastAPI(title="FastAPI Setup Test", dependencies=[])

app.include_router(router)
