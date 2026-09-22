from dotenv import load_dotenv
load_dotenv()

# Importaciones especificas 
from app import create_app
# Importaciones totales (toda la informacion del archivo)
# import app

app = create_app()

if __name__ == "__main__":
    app.run()