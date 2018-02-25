[![PyPI](https://img.shields.io/pypi/v/yield2await.svg)](https://pypi.python.org/pypi/yield2await)
![python versions](https://img.shields.io/badge/python-3.5%2C%203.6-blue.svg)
[![license](https://img.shields.io/apm/l/vim-mode.svg)](https://github.com/alxpy/yield2await/blob/master/LICENSE)

# yield2await

Transform your python code from old syntax with `yield from` to use `async`/`await` (PEP 492).

### Usage
```bash
$ pip install yield2await
$ yield2await <path> [-i <ignore-path>]
```

### Before
```python
@asyncio.coroutine
def handler(request):
    session = yield from get_session(request)
    session['last_visit'] = time.time()
    with (yield from self.dbengine) as conn:
        ret = yield from conn.execute(query)
        user = yield from ret.fetchone()
    return web.Response(body=b'OK')
```

### After
```python
async def handler(request):
    session = await get_session(request)
    session['last_visit'] = time.time()
    async with self.dbengine as conn:
        ret = await conn.execute(query)
        user = await ret.fetchone()
    return web.Response(body=b'OK')
```

### Contribution
Feel free to contribute. Just do RP.

### Caution
This is a very alpha, check the changes manually before commit.
