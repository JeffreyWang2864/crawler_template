class output:
    def __init__(self, e):
        self.data = dict()
        self.data_count = int()
        self.total_data_count = int()
        self.buffer_trigger = e
        self.buffer_size = 50
        self.end_writing = False
    def collectData(self, data):
        assert data is not None
        self.data_count += len(data)
        self.total_data_count += len(data)
        self.data.update(data)
    def writeSomeKindOfFile(self, path):
        pass
    def writeTXT(self, path):
        "This is an example"
        file = open(path, 'w')

        while not self.end_writing:
            self.buffer_trigger.wait()
            for sentence, rating in zip(self.data.values(), self.data.keys()):
                file.write(rating)
                file.write("\t")
                file.write(str(sentence))
                file.write("\n")
            print("\n***\nwrote %d lines of file on %s\n***\n" % (len(self.data), path))
            self.data = dict()
            self.data_count = int()
            self.buffer_trigger.clear()
        file.close()
