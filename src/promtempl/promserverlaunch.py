from prometheus_client import start_http_server, Gauge
import random
import time
import argparse
import logging
import sys

# logging setup
log = logging.getLogger('promserverlauncher')
log.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)

def update_metrics(metrics):
    """Function for updating metrics"""
    metrics['my_gauge_metric_one'].set(1.0)   # Set to a given value
    metrics['my_gauge_metric_two'].set(2.0)   # Set to a given value

def create_metrics():
    """Function for creatingmetrics"""
    metrics = {}
    metrics.update({'my_gauge_metric_one': Gauge('my_gauge_metric_one', 'My first dummy gauge metric')})
    metrics.update({'my_gauge_metric_two': Gauge('my_gauge_metric_two', 'My second dummy gauge metric')})
    return metrics

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(
            description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument('--port', nargs='?', const=9091,
                            help='The TCP port to listen on', default=9091)
        parser.add_argument('--addr', nargs='?', const='0.0.0.0',
                            help='The interface to bind to', default='0.0.0.0')
        parser.add_argument('--sleeptime', nargs='?', const=2,
                            help='Sleep time (seconds) for updating metrics', default=2)
        args = parser.parse_args()
        log.info('listening on http://%s:%d/metrics' % (args.addr, args.port))
        # Start up the server to expose the metrics.

        # Create metrics
        log.info('creating metrics...')
        metrics = create_metrics()
        
        #Start the http server
        start_http_server(int(args.port))
        # Generate some requests.

        while True:
            #Update metrics every tot seconds (see options)
            time.sleep(int(args.sleeptime))
            update_metrics(metrics)

    except KeyboardInterrupt:
        print(" Interrupted")
        exit(0)
