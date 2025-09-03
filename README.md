## Instructions

Install uv https://docs.astral.sh/uv/getting-started/installation/

```
>> uv sync
>> source .venv/bin/activate
>> uv run start
```

---

## Test that the server runs

1. go to `http://0.0.0.0:8000/docs#/default/world_hello_get`
2. call the endpoint and make sure it works

## Make sure tests work

```
uv add --dev pytest pytest-asyncio
pytest tests/
```

You should see

```
tests/test_issues_feed.py::TestHelloWorld::test_hello_world PASSED                                                                                                                      [100%]

====================================================================================== 1 passed in 0.00s ======================================================================================
```
