# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from dateutil.parser import parse as date_parse
from collections import OrderedDict

EVALUATION_POSITIVE = True
EVALUATION_NEGATIVE = False

THIS_MONTH_FILTER = 'This Month'
THIS_WEEK_FILTER = 'This Week'
TODAY_FILTER = 'Today'
ALL_FILTER = 'All'

FILTERS = OrderedDict([
    (TODAY_FILTER, 'get_num_days_today'),
    (THIS_WEEK_FILTER, 'get_num_days_week'),
    (THIS_MONTH_FILTER, 'get_num_days_month'),
    (ALL_FILTER, '')
])


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
        positive_perc = (positives * 100) / float(total_events)
        negative_perc = 100 - positive_perc
        return positive_perc, negative_perc

    @classmethod
    def filter(cls, store, filter_by):
        get_num_days_method = getattr(cls, FILTERS.get(filter_by), lambda: None)
        num_days = get_num_days_method()
        events = cls.filter_by_num_days(store, num_days)
        return events

    @classmethod
    def get_num_days_week(cls):
        today_week_number = datetime.today().weekday()
        return today_week_number

    @classmethod
    def get_num_days_month(cls):
        today_month_day = datetime.today().day
        return today_month_day - 1

    @classmethod
    def get_num_days_today(cls):
        return 0

    @classmethod
    def filter_by_num_days(cls, store, num_days):
        events = cls.get_events(store)
        if num_days is None:
            return events

        today = datetime.now().date()
        initial_date = today - timedelta(days=num_days)
        filtered_events = []
        for event in events:
            delta = event.date.date() - initial_date
            if delta.days <= num_days and delta.days >= 0:
                filtered_events.append(event)
        return filtered_events
