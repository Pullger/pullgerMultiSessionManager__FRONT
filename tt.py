from django.apps import apps
from pyPullgerExceptions import *
import logging

logger = logging.getLogger("test.operations")

def test():
    # url = 'http://pares.mcu.es/MovimientosMigratorios/buscadorRaw.form?d-3602157-p=1&objectsPerPage=25'
    #
    # squirrel = SquairrelCore.Squirrel('selenium')
    # result1 = squirrel.initialize()
    # result2 = squirrel.get(url)

    reglament_app = apps.get_app_config('MultisessionManagerCore');

    # try:
    #     raise excTest('info test')
    # except excTest as e:
    #     logger.info(f'test: {str(e)}')
    # except Exception as e:
    #     logger.info(f'test: {str(e)}')
    #
    #
    # logger.info('test')

    # reglament_app.multisessionManager.addNewSession(authorizationsServers.linkedin, authorizationsServers.LINKEDIN.general)
    try:
        from pullger import AccountManagerCore
        reglament_app.multisessionManager.addNewSession(authorization=AccountManagerCore.authorizationsServers.linkedin())
        reglament_app.multisessionManager.makeAllAutorization()

        # reglament_app.multisessionManager.generateSessinPackage(None, None, 5)
        # reglament_app.multisessionManager.closeAllSessions()
    except excSqirrel_InterfaceData as e:
        print(e)
    except excSqirrel as e:
        print(e)
    except Exception as e:
        print(e)

    pass
