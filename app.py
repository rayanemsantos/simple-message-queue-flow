# -*- coding: utf-8 -*-
import sys, os, threading
from order import app
from order.utils import ActiveMQ


def start_connection():
    ActiveMQ()

if __name__ == '__main__':
    try:
        thread_1 = threading.Thread(target=start_connection)
        thread_1.start()
        thread_1.join(0)
        app.run(debug=True)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

            