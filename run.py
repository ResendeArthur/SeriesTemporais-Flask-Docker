import datetime
import logging

from Flask import Flask
import papermill as pm

app = Flask(__name__)

@app.route('/')
def main(request=None):
    logging.info("Starting job...")


    pm.execute_notebook(
        '1.serie_temporal_.pynb',
        '2.decomposicao_.ipynb',
        '3.previsoes_arima_.ipynb',
    )

    logging.info("Job completed.")
    return 'ok'

if __name__ == '__main__':
    import os

    port = os.environ.get('PORT', '8080')
    app.run(port=port)
