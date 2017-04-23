# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil.parser import parse as date_parse

EVALUATION_POSITIVE = True
EVALUATION_NEGATIVE = False

THIS_WEEK_FILTER = 'This Week'
TODAY_FILTER = 'Today'

FILTERS = {
    THIS_WEEK_FILTER: 'filter_by_week',
    TODAY_FILTER: 'filter_by_day'
}


class Event(object):
    """An event"""
    def __init__(self, date, evaluation=EVALUATION_POSITIVE):
        super(Event, self).__init__()
        self.date = date
        self.iso_date = date.isoformat()
        self.evaluation = evaluation

    def __unicode__(self):
        return "{}: {}".format(self.iso_date, self.evaluation)

    def __str__(self):
        return self.__unicode__()

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
    def reset_store(cls, store):
        for key in store:
            store.delete(key)
        return []

    @classmethod
    def get_rate(cls, events):
        total_events = len(events)
        positives = len(filter(lambda e: e.evaluation, events))
        positive_perc = (positives * 100) / total_events
        negative_perc = 100 - positive_perc
        return positive_perc, negative_perc

    @classmethod
    def filter(cls, store, filter_by):
        filter_method = getattr(cls, FILTERS.get(filter_by))
        events = filter_method(cls, store)
        return events

    @classmethod
    def filter_by_day(cls, store):
        events = cls.get_events(store)
        today_events = []
        for event in events:
            if event.date.date() == datetime.now().date():
                today_events.append(event)
        return today_events

    @classmethod
    def filter_by_week(cls, store):
        events = cls.get_events(store)
        today_events = []
        for event in events:
            if event.date.date() == datetime.now().date():
                today_events.append(event)
        return today_events
