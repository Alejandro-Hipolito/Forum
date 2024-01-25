from website.templates import create_app #I can import it bc it's in the __init__.py file, that file acts as a python package

app = create_app()

if __name__ == '__main__': #Only if we run this file (__main__) the server is going to run
    app.run(debug=True)