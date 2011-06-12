# coding: utf-8
def data_provider(data_provider):
    """Data provider decorator, allows another callable to provide the data for the test
    Usage:
    <code>
    sum_provider = (
        ( 3, (1, 2)),
        ( 6, (1, 5))
    )

    @data_provider(sum_provider)
    def test_sum(self, result, *args):
        operands = args[0]
        self.assertEquals(result, operands[0] + operands[1])

    </code>
    Credit goes to Gerard van Helden (melp.nl) and Ian Bicking (blog.ianbicking.org)
    """
    def test_decorator(fn):
        def repl(self):
            step = 1
            for data_set in data_provider:
                try:
                    fn(self, unicode(data_set[0]), data_set[1])
                    step += 1
                except AssertionError, e:
                    args = e.args
                    arg0 = ''
                    if args:
                        arg0 = args[0]
                    arg0 += u' (Caught with data set #%i %s)' % (step, data_set)
                    e.args = (arg0,) + args[1:]
                    raise
        return repl
    return test_decorator
