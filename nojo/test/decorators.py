# coding: utf-8
def data_provider(fn_data_provider):
    """Data provider decorator, allows another callable to provide the data for the test
    Usage:
    <code>
    sum_provider = lambda: (
        ( 3, (1, 2)),
        ( 6, (1, 5))
    )

    @data_provider(sum_provider):
    def test_sum(self, result, operands):
        self.assertEquals(result, operands[0] + operands[1])

    </code>
    Credit goes to Gerard van Helden (melp.nl) and Ian Bicking (blog.ianbicking.org)
    """
    def test_decorator(fn):
        def repl(self, *args):
            step = 1
            for data_set in fn_data_provider():
                try:
                    fn(self, *data_set)
                    step += 1
                except AssertionError, e:
                    args = e.args
                    arg0 = ''
                    if args:
                        arg0 = args[0]
                    arg0 += ' (Caught with data set #%i %s)' % (step, data_set)
                    e.args = (arg0,) + args[1:]
                    raise
        return repl
    return test_decorator