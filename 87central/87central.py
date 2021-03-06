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
    time_delta       = relativedelta(hours = 1)
    return (current_datetime - time_delta).strftime('%Y-%m-%d %I:%M %p %Z')

def is_central_time():
    '''
    this function return a given time from the computer is a central time or not.
    return true if it is; false otherwise.
    '''
    utc_offset = get_utc_offset()
    central_offset = get_utc_offset('America/Regina')
    return utc_offset == central_offset

def get_utc_offset(tz=None):
    '''
    calculates the utc offset base on current time zone
    the return is offset in hour; or if time zone (tz) is
    passed in, return the utc offset from a that.
    '''
    if tz is None:
       tz = get_localzone() # get local time zone
    else:
       tz = gettz(tz)

    d          = datetime.datetime.now(tz) # get current time base on time zone we know about
    utc_offset = int(d.utcoffset().total_seconds() // 3600) # get utc offset base hour units
    return utc_offset

def to_calendar_format(date, tz=None):
    '''
    this function will return an input date's UTC time in ISO 8601 format. if
    tz (time zone) is none, calculate will base on current time zone; otherwise
    use a tz for the calculation.
    '''
    current_datetime = parser.parse(date)
    utc_offset       = get_utc_offset(tz)
    current_utc_time = current_datetime + relativedelta(hours=utc_offset)

    return current_utc_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')


if __name__ == '__main__':
    datetime_stamp = '2015/01/07 2:29 PM'
    print('one hour early than %s is %s' % (datetime_stamp, one_hour_early(datetime_stamp)))
    datetime_stamp = '2015/01/01 12:34 AM'
    print('one hour early than %s is %s' % (datetime_stamp, one_hour_early(datetime_stamp)))
    print('is current timezone CST? %s' % is_central_time())

    current_timestamp    = '2014-02-08 06:30 PM'
    current_iso_utc_time = to_calendar_format(current_timestamp)
    print('PST time %s is UTC %s' % (current_timestamp, current_iso_utc_time))

    current_timestamp    = '2014-02-08 06:30 PM'
    current_iso_utc_time = to_calendar_format(current_timestamp, 'America/Phoenix')
    print('MST time %s is UTC %s' % (current_timestamp, current_iso_utc_time))

    current_timestamp    = '2014-02-08 06:30 PM'
    current_iso_utc_time = to_calendar_format(current_timestamp, 'America/Monterrey')
    print('CST time %s is UTC %s' % (current_timestamp, current_iso_utc_time))

    current_timestamp    = '2014-02-08 06:30 PM'
    current_iso_utc_time = to_calendar_format(current_timestamp, 'America/New_York')
    print('EST time %s is UTC %s' % (current_timestamp, current_iso_utc_time))
