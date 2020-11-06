from socket import gethostname
from app import app


if __name__=="__main__":

    if 'liveconsole' not in gethostname():
        app.run(host="0.0.0.0", port=8080, debug=True)
