from SublimeLinter.lint import NodeLinter, util

class Alex(NodeLinter):
	npm_name = 'alex'
	cmd = ('alex', '--stdin')
	regex = (
		r'^\s+(?P<line>\d+):(?P<col>\d+).+'
		r'(?:(?P<error>error)|(?P<warning>warning))\s+'
		r'(?P<message>.+)'
	)
	defaults = {
		'selector': 'text.plain, text.html.markdown'
	}
	error_stream = util.STREAM_STDERR
