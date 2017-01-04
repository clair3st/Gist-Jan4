import os
import sys
import transaction
import faker
import random

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
from ..models import User


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    fake = faker.Faker()

    foods = [
        'Sushi',
        'Pizza',
        'Cookies',
        'Chinese',
        'Steak',
        'Thai',
        'Kebab',
        'Taco'
    ]

    users = [User(
        firstname=fake.name().split(' ')[0],
        lastname=fake.name().split(' ')[1],
        email=fake.email(),
        username=fake.user_name(),
        password=fake.password(),
        food=random.choice(foods),
    ) for i in range(10)]

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

    dbsession.add_all(users)
