import sys
import orm
from models import User
import asyncio

@asyncio.coroutine
def test( loop ):
    yield from orm.create_pool( loop = loop, user='root', password='labcat127', db='awesome' )
    u = User(name='Test', email='te@example.com', passwd='12347890', image='about:blank')
    yield from u.save()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete( asyncio.wait([test( loop )]) )
    loop.close()
    if loop.is_closed():
        sys.exit(0)