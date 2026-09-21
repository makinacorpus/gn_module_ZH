from pypnusershub.tests.utils import set_logged_user

from flask import url_for

from geonature.tests.fixtures import *
from .fixtures import *


@pytest.mark.usefixtures("client_class")
class TestFilters:
    # def test_no_filter(self, users, zh_data, ref_geo_data):
    #     set_logged_user(self.client, users["self_user"])
    #     response = self.client.get(url_for("pr_zh.get_zh"))
    #     assert response.status_code == 200
    #     data = response.get_json()
    #     assert len(data["items"]["features"]) == 2

    def test_get_zh_with_filter(self, users, zh_data, ref_geo_data):
        for ref_geo in ref_geo_data:
            if ref_geo.area_code == "930012713":
                print({c.name: getattr(ref_geo, c.name) for c in ref_geo.__table__.columns})
                # print("\n\n\n ref_geo", ref_geo[""], " \n\n\n")
        set_logged_user(self.client, users["admin_user"])

        response = self.client.post(url_for("pr_zh.get_zh"),json=
        {
            "territories":
                {"ZNIEFF2":
                     [
                         {"code": "930012713",
                          "name": "Clue de vergons - barre de pinadoux"
                          }]}})
        # for larea in ref_geo_data:
            # break
        assert response.status_code == 200
        data = response.get_json()
        #
        print("\n\n\n data => ", data)
        assert len(data["items"]["features"]) == 1
