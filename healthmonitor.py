import logging
import psutil

# Configure logging
logging.basicConfig(filename="system_health.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Thresholds
CPU_THRESHOLD = 80  # percent
MEMORY_THRESHOLD = 80  # percent
DISK_THRESHOLD = 90  # percent

def check_system_health():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        message = f"High CPU usage detected: {cpu_usage}%"
        logging.warning(message)
        print(message)  # Print to console

    # Check Memory usage
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        message = f"High Memory usage detected: {memory.percent}%"
        logging.warning(message)
        print(message)  # Print to console

    # Check Disk usage
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        message = f"Low Disk space: {disk.percent}% used"
        logging.warning(message)
        print(message)  # Print to console

    # Check the number of running processes
    num_processes = len(psutil.pids())
    message = f"Running processes count: {num_processes}"
    logging.info(message)
    print(message)  # Print to console

    print("System health check completed. Check logs for alerts.")

# Run the health check
check_system_health()