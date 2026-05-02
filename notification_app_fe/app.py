from logging_middleware.log import Log

# simulate frontend actions

Log("frontend", "info", "component", "User opened homepage")
Log("frontend", "warn", "component", "Slow response detected")
