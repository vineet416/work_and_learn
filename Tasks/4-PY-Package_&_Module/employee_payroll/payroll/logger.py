import logging

logging.basicConfig(
    filename="payroll.log",
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)
