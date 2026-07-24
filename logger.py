import logging
import os

# Create logs folder automatically
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/security.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)

# Silence telegram library logs
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("telegram").setLevel(logging.WARNING)


def log_event(event):
    logging.info(event)
