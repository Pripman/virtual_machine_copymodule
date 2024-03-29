# Standard libraries
import logging

# Third party libraries
from flask import Flask, request

# Our libraries
import copyingModule
from hest.decorators import routelog


log = logging.getLogger()
log.setLevel(logging.DEBUG)
logging.basicConfig()

class SuperFlasker(Flask):
    def make_response(self, rv):
        if hasattr(rv, "toclient"):
            return Flask.make_response(self, rv.toclient())
        return Flask.make_response(self, rv)


app = SuperFlasker(__name__)

class it:
    def toclient(self):
        return "sax"


@app.route("/test")
@routelog
def test():
    return it()
    return "Hello " + request.remote_addr

app.register_blueprint(copyingModule.bp)

def main():
    app.debug = True
    app.run("0.0.0.0", port = 5010)

if __name__ == "__main__":
    main()
