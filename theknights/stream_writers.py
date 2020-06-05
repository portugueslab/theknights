
class ChannelWriterBase(object):
    """
    Defines base class for all NI-DAQmx stream writers.
    """

    def __init__(self, task_out_stream, auto_start=None):
        self._out_stream = task_out_stream
        self._task = task_out_stream._task
        self._handle = task_out_stream._task._handle
        self._verify_array_shape = True
        self._auto_start = auto_start


class AnalogSingleChannelWriter(ChannelWriterBase):

    def write_many_sample(self, data, timeout=10.0):

        return data.shape[0]
