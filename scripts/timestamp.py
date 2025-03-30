import datetime
import sys
import re

def get_args():
	args = sys.argv[1:]
	parsed_args = {}
	for arg in args:
		arg_name = arg.split('=')[0].replace('--', '')
		arg_value = arg.split('=')[1]
		parsed_args.update({arg_name: arg_value})
	return parsed_args

args = get_args()
strtime_format = '%Y%m%d %H%M'

if 'format' in args:
	time_format = ''

	args['format'] = args['format'].replace('\"', '')
	args['format'] = args['format'].replace('\'', '')

	for letter in args['format']:
			if(re.match(r'[a-zA-Z]', letter)):
				time_format += '%'
				time_format += letter
			else:
				time_format += letter
	strtime_format = time_format

print(datetime.datetime.now().strftime(strtime_format))
