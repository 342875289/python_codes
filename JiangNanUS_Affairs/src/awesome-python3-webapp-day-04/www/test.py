import sys

import orm
from models import User
import asyncio

async def test( loop ):
    await orm.create_pool( loop = loop, user='root', password='labcat127', db='awesome' )
    u = User(name='Ttdasd', email='tsdae@example.com', passwd='1234567890', image='about:blank')
    await u.save()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete( test( loop=loop ) )
    loop.close()
    if loop.is_closed():
        sys.exit(0)
print('OK')