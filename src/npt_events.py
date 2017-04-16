# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil.parser import parse as date_parse

EVALUATION_POSITIVE = True
EVALUATION_NEGATIVE = False


class Event(object):
    """An event"""
    def __init__(self, date, evaluation=True):
        super(Event, self).__init__()
        self.date = date
        self.iso_date = date.isoformat()
        self.evaluation = evaluation

    def __unicode__(self):
        return "{}: {}".format(self.iso_date, self.evaluation)

    def save(self, store):
        print "saving %s" % unicode(self)
        store.put(self.iso_date, evaluation=self.evaluation)

    @classmethod
    def get_events(cls, store):
        events = []
        for key in store:
            evaluation = store.get(key).get('evaluation', True)
            event = cls(
                date=date_parse(key),
                evaluation=evaluation
            )
            events.append(event)
        return events

    @classmethod
    def get_rate(cls, events):
        total_events = len(events)
        positives = len(filter(lambda e: e.evaluation, events))
        positive_perc = (positives * 100) / total_events
        negative_perc = 100 - positive_perc
        return positive_perc, negative_perc
