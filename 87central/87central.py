from __future__ import print_function
import datetime
from dateutil import parser
from dateutil.relativedelta import *
from dateutil.tz import *
from time import gmtime, strftime
from tzlocal import get_localzone

def one_hour_early(date):
    '''
    this function will return one hour early than the current input time
    '''
    current_datetime = parser.parse(date)
    time_delta = relativedelta(hours=1)
    return (current_datetime - time_delta).strftime('%Y-%m-%d %I:%M %p %Z')

def is_central_time():
    '''
    this function calcuates the utc_offset via local timezone, obtrains from 
    /etc/localtime. If utc_offset is not -6 then return False; otherwise return
    true. This is because Central time is UTC-6.
    '''
    utc_offset = get_utc_offset()
    return utc_offset == -6.0

def get_utc_offset():
    tz = get_localzone()
    d = datetime.datetime.now(tz)
    return d.utcoffset().total_seconds() // 3600

def to_calendar_format(date):
    '''
    this function will return an input date's UTC time in ISO 8601 format
    '''
    current_datetime = parser.parse(date)
    utc_offset = datetime.datetime.utcnow() - datetime.datetime.now()
    current_utc_time = current_datetime + utc_offset

    return current_utc_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

def rounding_time(dt=None, deltaTime=relativedelta(minutes=1)):
    if dt is None:
        dt = datetime.datetime.now()
    elif type(dt) is str:
        dt = parser.parse(dt)

    roundTo = deltaTime.total_seconds()
    seconds = (dt.replace(tzinfo=None) - dt.min).seconds
    rounding = (seconds + roundTo / 2)
    return dt + datetime.timedelta(0, rounding - seconds, -dt.microsecond)

if __name__ == '__main__':
    datetime_stamp = '2015/01/07 2:29 PM'
    print('one hour early than %s is %s' % (datetime_stamp, one_hour_early(datetime_stamp)))
    datetime_stamp = '2015/01/01 12:34 AM'
    print('one hour early than %s is %s' % (datetime_stamp, one_hour_early(datetime_stamp)))
    print('is current timezone CST? %s' % is_central_time())

    current_timestamp = '2014-02-08 06:00 PM PST' # PST Time
    current_iso_utc_time = rounding_time(to_calendar_format(current_timestamp), deltaTime=datetime.timedelta(seconds=2))
    print('PST time %s is UTC %s' % (current_timestamp, datetime.datetime.strftime(current_iso_utc_time, '%Y-%m-%dT%H:%M:%S.%fZ')))

    current_timestamp = '2014-02-08 05:00 PM MST' # PST Time
    current_iso_utc_time = rounding_time(to_calendar_format(current_timestamp), deltaTime=datetime.timedelta(seconds=2))
    print('MST time %s is UTC %s' % (current_timestamp, datetime.datetime.strftime(current_iso_utc_time, '%Y-%m-%dT%H:%M:%S.%fZ')))
