#!/usr/bin/env python3
#
#  __init__.py
"""
Helper functions for pytest.
"""
#
#  Copyright © 2020-2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
import datetime
import sys

# this package
from coincidence.fixtures import fixed_datetime, original_datadir, path_separator, tmp_pathplus
from coincidence.params import count, testing_boolean_values, whitespace_perms
from coincidence.regressions import (
		AdvancedDataRegressionFixture,
		AdvancedFileRegressionFixture,
		SupportsAsDict,
		advanced_data_regression,
		advanced_file_regression,
		check_file_output,
		check_file_regression
		)
from coincidence.selectors import (
		max_version,
		min_version,
		not_docker,
		not_macos,
		not_pypy,
		not_windows,
		only_docker,
		only_macos,
		only_pypy,
		only_version,
		only_windows,
		platform_boolean_factory
		)
from coincidence.utils import (
		generate_falsy_values,
		generate_truthy_values,
		is_docker,
		whitespace,
		whitespace_perms_list,
		with_fixed_datetime
		)

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2020-2021 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "0.4.1"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = ["pytest_report_header", "PEP_563"]


def pytest_report_header(config, startdir):
	"""
	Prints the start time of the pytest session.
	"""

	return f"Test session started at {datetime.datetime.now():%H:%M:%S}"


PEP_563: bool = (sys.version_info[:2] >= (3, 11))
"""
:py:obj:`True` if the current Python version implements :pep:`563` -- Postponed Evaluation of Annotations.
"""
