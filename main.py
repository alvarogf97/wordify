from wordify.wsgi import make_app


if __name__ == "__main__":
    app = make_app()
    app.run(host='127.0.0.1', port=8080, debug=True)
