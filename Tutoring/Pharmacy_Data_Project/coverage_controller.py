import falcon
from falcon import Request, Response

class CoverageController:
    def __init__(self, service):
        self.service = service

    async def on_get(self, req, res):
        id = req.params.get('id')
        fname = req.params.get('fname')
        lname = req.params.get('lname')
        med = req.params.get('med')
        dose = req.params.get('dose')
        coverage = self.service.get_coverage(id, fname, lname, med, dose)

        res.status = falcon.HTTP_200
        data = {}
        data['coverageClass'] = coverage.coverageClass
        data['copay'] = coverage.copay
        data['outOfPocket'] = coverage.outOfPocket

        res.content_type = falcon.MEDIA_JSON
        res.media = data
        