from app import create_app

app, db, ma = create_app()

from MutantTest import Model

if __name__ == "__main__":
    from MutantTest import Mutant

    app.register_blueprint(Mutant.bp)

    app.run(debug=True, host='0.0.0.0', port=8080)
