import requests
from urllib.parse import urljoin

from flask import Flask, request
from flask_restful import Api, Resource


app = Flask(__name__)
app.config.from_object("config.Config")
api = Api(app)


class TemplateView(Resource):
    def get(self, _ignore):
        access_token = request.args.get("access_token")
        if access_token and app.config["TEMPLATE_URL"]:
            fb_business_id = app.config["FB_BUSINESS_ID"]
            response = requests.get(
                urljoin(
                    app.config["TEMPLATE_URL"],
                    f"/v3.3/{fb_business_id}/message_templates",
                ),
                params=dict(access_token=access_token, limit=255),
            )
            return response.json()
        else:
            return {}


api.add_resource(TemplateView, "/v3.3/<string:_ignore>/message_templates")
