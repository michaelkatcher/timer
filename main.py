"""
Name: Michael Katcher
Date: 07/25/2017
Desc: This is a demonstration of my updated Timer class.
"""

from timer.timer import Timer

def main():
    """Demonstrate the Timer class' print feature."""

    print
    print '** Demonstrating new Timer print statement:'

    with Timer('Test Timer') as tm:
        current_second = 0
        while tm.current_result() < 5:
            if current_second != int(tm.current_result()):
                print '{s} second(s) elapsed.'.format(s=int(tm.current_result()))
                current_second = int(tm.current_result())

    print
    print '** Changing Timer unit and printing last result:'
    tm.unit = 'ms'
    print tm.last_result()


if __name__ == '__main__':
    main()