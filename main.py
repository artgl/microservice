from flask import render_template, send_from_directory
import connexion

#from api import configuration, log


# Create the application instance
app = connexion.App(__name__, specification_dir='./')

app.add_api('yaml/configuration.yaml')
app.add_api('yaml/log.yaml')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=False)
