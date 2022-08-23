from app import create_app
from config import ProductionConfig

# Gets called from wsgi server.
application = create_app(ProductionConfig)