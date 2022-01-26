r=""
def parse64(text):
	a=str(text)[1:][1:][:-1]
	return a
def parse(text):
	exec(f'global r;r={text}')
	return r
