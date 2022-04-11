from app import create_app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = create_app()

db = SQLAlchemy(app)
ma = Marshmallow(app)

from MutantTest import Model

if __name__ == "__main__":
    from MutantTest import Mutant

    app.register_blueprint(Mutant.bp)

    app.run(debug=True, host='0.0.0.0', port=8080)
