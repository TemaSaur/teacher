from fastapi.templating import Jinja2Templates


class Config:
    jinja: Jinja2Templates


server = Config()
