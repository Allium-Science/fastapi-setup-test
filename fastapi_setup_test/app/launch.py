import uvicorn  # noqa: E402


def start():
    """Launched with `uv run start` at root level"""
    uvicorn.run(
        "fastapi_setup_test.app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        access_log=False,
    )
