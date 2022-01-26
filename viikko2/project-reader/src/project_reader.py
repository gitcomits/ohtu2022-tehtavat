import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        dependencies = []  
        dev_dependencies = []
        # tiedoston merkkijonomuotoinen sisältö
        content = toml.loads(request.urlopen(self._url).read().decode("utf-8"))
        



        name = content.get("tool", {}).get("poetry",{}).get("name")
        desc = content.get("tool", {}).get("poetry",{}).get("description")
        depen = content.get("tool", {}).get("poetry",{}).get("dependencies")
        dev = content.get("tool", {}).get("poetry",{}).get("dev-dependencies")
        for d in depen:
            dependencies.append(d)
        
        for d in dev:
            dev_dependencies.append(d)

    #    c = toml.loads(content,_dict=dict)
             
        
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, dependencies, dev_dependencies)
