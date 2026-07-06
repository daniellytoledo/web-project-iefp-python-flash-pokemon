from app.__init__ import criar_app

app = criar_app()

if __name__ == "__main__":
    app.run(debug=True)