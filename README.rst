|PyPI| |python versions| |license|

yield2await
===========

Transform your python code from old syntax with ``yield from`` to use ``async``/``await`` (PEP 492).

Usage
~~~~~

.. code:: bash

    $ pip install yield2await
    $ yield2await <path> [-i <ignore-path>]

Before
~~~~~~

.. code:: python

    @asyncio.coroutine
    def handler(request):
        session = yield from get_session(request)
        session['last_visit'] = time.time()
        with (yield from self.dbengine) as conn:
            ret = yield from conn.execute(query)
            user = yield from ret.fetchone()
        return web.Response(body=b'OK')

After
~~~~~

.. code:: python

    async def handler(request):
        session = await get_session(request)
        session['last_visit'] = time.time()
        async with self.dbengine as conn:
            ret = await conn.execute(query)
            user = await ret.fetchone()
        return web.Response(body=b'OK')

Contribution
~~~~~~~~~~~~

Feel free to contribute. Just do RP.

Caution
~~~~~~~

This is a very alpha, check the changes manually before commit.

.. |PyPI| image:: https://img.shields.io/pypi/v/yield2await.svg
   :target: https://pypi.python.org/pypi/yield2await
.. |python versions| image:: https://img.shields.io/badge/python-3.5%2C%203.6-blue.svg
.. |license| image:: https://img.shields.io/apm/l/vim-mode.svg
   :target: https://github.com/alxpy/yield2await/blob/master/LICENSE
