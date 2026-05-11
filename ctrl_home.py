"""
Esse arquivo é um exemplo de controller
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from werkzeug.security import check_password_hash, generate_password_hash

from database import db
from models import User

bp = Blueprint(__name__, "HomeController")

@bp.route("/") # cria uma rota
def index(): # função que gerencia rota
    """ Página inicial"""
    if '_user_id' not in session:
        return redirect(url_for("auth.login"))
    
    return render_template("dashboard/index.html") # Renderiza um template

@bp.route("/dashboard") # cria uma rota
def dashboard(): # função que gerencia rota
    """ Painel de Vendas"""
    # if 'user' not in session:
    #     return redirect(url_for("auth.login"))
    
    # remova o login
    import locale
    # Configura para o formato brasileiro
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    vendas: list = [
        {"mes":"Janeiro","total": 139519.19},
        {"mes":"Fevereiro","total": 131571.23},
        {"mes":"Março","total": 140571.25},
        {"mes":"Abril","total": 145681.30},
        {"mes":"Maio","total": 147761.20},
        {"mes":"Junho","total": 142591.65},
        {"mes":"Julho","total": 119996.18},
        {"mes":"Agosto","total": 132199.89},
        {"mes":"Setembro","total": 129889.69},
        {"mes":"Outubro","total": 138598.29},
        {"mes":"Novembro","total": 145599.99},
        {"mes":"Dezembro","total": 211641.69}
    ] #fim lista

    return render_template("dashboard/index.html", title="Painel de Venda", vendas=vendas, locale=locale) # Renderiza um template