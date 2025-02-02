import falcon.asgi
from coverage_controller import CoverageController
from coverage_service import CoverageService

app = falcon.asgi.App(cors_enable=True)

controller = CoverageController(service=CoverageService())


app.add_route('/pharmacy/v1/coverage', controller)