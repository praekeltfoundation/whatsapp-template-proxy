import requests
from urllib.parse import urljoin

from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
app.config.from_object("config.Config")
api = Api(app)


class TemplateView(Resource):
    def get(self, fb_business_id):
        if app.config["TEMPLATE_URL"] and app.config["ACCESS_TOKEN"]:
            response = requests.get(
                urljoin(
                    app.config["TEMPLATE_URL"],
                    f"/v3.3/{fb_business_id}/message_templates",
                ),
                params=dict(access_token=app.config["ACCESS_TOKEN"], limit=255),
            )
            return response.json()
        else:
            return {}


api.add_resource(TemplateView, "/v3.3/<string:fb_business_id>/message_templates")
