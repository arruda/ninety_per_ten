# -*- coding: utf-8 -*-
from datetime import datetime

EVALUATION_POSITIVE = True
EVALUATION_NEGATIVE = False


class Event(object):
    """An event"""
    def __init__(self, date=datetime.now(), evaluation=True):
        super(Event, self).__init__()
        self.date = date
        self.evaluation = evaluation

    @classmethod
    def get_rate(cls, events):
        total_events = len(events)
        positives = len(filter(lambda e: e.evaluation, events))
        positive_perc = (positives * 100) / total_events
        negative_perc = 100 - positive_perc
        return positive_perc, negative_perc
