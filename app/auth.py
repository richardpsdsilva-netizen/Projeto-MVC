# LOGICA DE AUTENTICAÇÃO

# 1. HASH E VERICAÇÃO DE SENHAS COM BCRYPT
# 2. GERAÇÃO DE TOKEN JWT
# 3. LEITURA E VALIDAÇÃO DO TOLEM VINDO DO COOKIE

from datetime import datetime, timedelta , timezone
from jose import JOSEError , jwt
from fastapi import Request , HTTPException , status
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACESS_TOKEN_EXPIRE_MINUTE = os.getenv("ACESS_TOKEN_EXPIRE_MINUTE")

# CONFIGURAR O ALGORITIMO DO HASH = BCRYPT
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# TESTE DE SENHA
# senha = "1234"
# senha_hash = pwd_context.hash(senha)

# print(senha)
# print("Senha com hash: ")
# print(senha_hash)

# senha_atual = "minhasenha"

# print(pwd_context.verify(senha_atual , senha_hash ) )

# FUNÇÕES DE SENHA
def hash_senha (senha : str):
    return pwd_context.hash (senha)
def verificar_senha(senha: str , senha_hash : str):
    return pwd_context.verify(senha , senha_hash)
