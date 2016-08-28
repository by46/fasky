HTTP_HOST = ''
HTTP_PORT = 8080

SECRET_KEY = "\x02|\x86.\\\xea\xba\x89\xa3\xfc\r%s\x9e\x06\x9d\x01\x9c\x84\xa1b+uC"

LOG = "/var/flasky"

# WSGI Settings
WSGI_LOG = 'default'

# Flask-Log Settings
LOG_LEVEL = 'debug'
LOG_FILENAME = "logs/error.log"
LOG_BACKUP_COUNT = 10
LOG_MAX_BYTE = 1024 * 1024 * 10
LOG_FORMATTER = '%(asctime)s - %(levelname)s - %(message)s'
LOG_ENABLE_CONSOLE = True
