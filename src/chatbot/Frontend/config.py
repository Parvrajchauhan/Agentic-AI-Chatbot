from pathlib import Path
from configparser import ConfigParser

class Config:
    def __init__(self):
        self.config = ConfigParser()

        config_path = Path(__file__).parent / "config.ini"

        print("Loading:", config_path)

        loaded = self.config.read(config_path)

        print("Loaded files:", loaded)
        print("Sections:", self.config.sections())
        print("Defaults:", dict(self.config.defaults()))
        
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE").split(",")
    
    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(",")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(",")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(",")

    