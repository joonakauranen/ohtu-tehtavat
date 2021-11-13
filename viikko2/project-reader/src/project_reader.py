from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_dict = toml.loads(content, _dict=dict)

        vaihe = toml_dict['tool']
        vaihe = vaihe['poetry']
        nimi = vaihe['name']
        kuvaus = vaihe['description']
        riippuvuudet = vaihe['dependencies']
        dev_riippuvuudet = vaihe['dev-dependencies']
        

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(nimi, kuvaus, riippuvuudet, dev_riippuvuudet)
