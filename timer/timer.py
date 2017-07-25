"""
This module contains the Timer Class.
"""

from time import time


class Timer(object):
    """Timer is a generic timer used to time duration of code execution."""

    # _allowed_units is used for three purposes.
    # First: to make sure any change to the unit property is supported.
    # Second: to display the name of the unit.
    # Third: to do the conversion math.
    _allowed_units = {'ms': ('milliseconds', 0.001), 's': (
        'seconds', 1), 'm': ('minutes', 60), 'h': ('hours', 60 * 60)}
    _default_unit = 's'

    def __init__(self,name='Timer',unit=_default_unit):
        """__init__ method of the Timer class.

        Args:
            unit (str, optional): User can specify the unit to return during initialization but
                this is not required.
        """

        self._name = name
        self._unit = unit
        self._start_time = 0
        self._result_time = None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.end()

    @property
    def result_time(self):
        """float: The most recent Timer result in seconds."""
        return self._result_time

    @property
    def unit(self):
        """str: The unit of time returned."""
        return self._unit

    @unit.setter
    def unit(self, new_unit):
        # Only change 'unit' if it's a valid unit.
        if Timer.valid_unit(new_unit):
            self._unit = new_unit
        else:
            raise TypeError('Invalid unit. Allowed units: ' + str(self._allowed_units.keys()))

    @property
    def name(self):
        """str: The name of the timer."""
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def start(self,display_start=False):
        """Starts the timer."""

        # Only start the timer if it's not currently running.
        if not self._start_time:
            if display_start:
                print 'Starting Timer...'
            self._start_time = time()
        else:
            raise RuntimeError('Timer already running.')

    def end(self):
        """Ends the timer and prints the time taken."""

        # Only end the timer if it's currently running.
        if not self._start_time:
            raise RuntimeError('Timer is not currently running.')
        else:
            self._result_time = time() - self._start_time
            self._start_time = 0

            unit_result_time = self._result_time / float(self._allowed_units[self._unit][1])
            unit_name = self._allowed_units[self._unit][0]

            print '{n}: {t} {u}'.format(n=self._name,t=unit_result_time,u=unit_name)

    def last_result(self):
        """Returns the most recent timer result."""

        # Only display the most recent result if the timer has already been run
        # once.
        if self._result_time is None:
            raise ValueError('The timer has not been run yet. Nothing to return.')
        else:
            unit_result_time = self._result_time / float(self._allowed_units[self._unit][1])
            unit_name = self._allowed_units[self._unit][0]

            return 'Most recent result for {n}: {t} {u}'.format(n=self._name,t=unit_result_time,u=unit_name)

    def current_result(self):
        """Returns the current result of a running timer in seconds."""

        # Only display the current result if the timer is running.
        if not self._start_time:
            raise RuntimeError('Timer is not currently running.')
        else:
            return time() - self._start_time

    @classmethod
    def valid_unit(cls, unit):
        """Checks whether a given unit of time is valid."""
        return unit in cls._allowed_units
