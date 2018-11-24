#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of convertdate.
# http://github.com/fitnr/convertdate

# Licensed under the GPL-v3.0 license:
# http://opensource.org/licenses/MIT
# Copyright (c) 2016, fitnr <fitnr@fakeisthenewreal>

'''Convert to and from the Dublin day count'''

from . import daycount

EPOCH = 2415020  # Julian Day Count for Dublin Count 0

_dublin = daycount.DayCount(EPOCH)

to_gregorian = _dublin.to_gregorian

from_gregorian = _dublin.from_gregorian

to_jd = _dublin.to_jd

from_jd = _dublin.from_jd

from_julian = _dublin.from_julian

to_julian = _dublin.to_julian

to_datetime = _dublin.to_datetime

from_datetime = _dublin.from_datetime