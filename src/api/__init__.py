from flask import Blueprint

BP_NAME = 'checkifbestseller'
bp = Blueprint(BP_NAME, __name__)

from . import views
