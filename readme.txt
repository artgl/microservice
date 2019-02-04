1. Create virtualenv with packages from deps file:
   'virtualenv -p python3 venv; venv/bin/pip install -r deps'

2. Run server:
   'venv/bin/python main.py'

3. Swagger:
   http://localhost:8000/log/ui
   http://localhost:8000/configuration/ui

4. Test sequence:

   First attempt to log something will fail. To make logger work correctly we need first configure correct log target, and try once more.

   curl -w "%{http_code}\n" -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d 'message=test' 'http://localhost:8000/log/message1'
   > "No log target is configured"
   > 422

   curl -w "%{http_code}\n" -X PUT --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d 'value=console' 'http://localhost:8000/configuration/target'
   > "console"
   > 200

   curl -w "%{http_code}\n" -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d 'message=test' 'http://localhost:8000/log/message1'
   > "Message 'test' logged to console"
   > 200
