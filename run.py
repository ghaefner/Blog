from flaskblog import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensures that the database tables are created before running the app
    app.run(debug=True, host='0.0.0.0')
