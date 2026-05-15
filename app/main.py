# PONTE DE ENTRADA DO MEU SISTEMA 
from fastapi import FastAPI , Request , Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse , RedirectResponse

from app.controllers import auth_controller
app = FastAPI(title = "Sistema de Ponto de venda")

#CONFIGURAR A PASTA PARA SERVIR OS ARQUIVOS ESTÁTICOS (CSS , JS E IMG)
app.mount("/static" , StaticFiles (directory = "app/static") , name = "static")

#CONFIGURAR O JINJA2 PARA RENDERIZAR OS HTML
templates = Jinja2Templates(directory = "app/templates" )

from fastapi import FastAPI
# 1. Importe o router que você criou no outro arquivo
from app.controllers.auth_controller import router as auth_router

app = FastAPI(title="Sistema de Ponto de Venda")

# 2. Registre o roteador na instância principal do app
app.include_router(auth_router)

@app.get("/")
def raiz():
    return {"message": "API Online"}