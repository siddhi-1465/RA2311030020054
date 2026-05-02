from logging_middleware.log import Log

# simulate backend actions

Log("backend", "info", "service", "Backend service started")
Log("backend", "error", "handler", "Invalid input received")
