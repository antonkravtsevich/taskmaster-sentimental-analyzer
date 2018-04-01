class TempStorage:

    def __init__(self, storage_max_length=5):
        self.request_count = 0
        self.temp_storage = []
        self.storage_max_length = storage_max_length


    def __str__(self):
        result = '=============================================================================<br>'
        result += 'Requests processed: {}<br>'.format(self.request_count)
        result += '_____________________________________________________________________________<br>'
        result += 'Last requests: <br>'
        result += '_____________________________________________________________________________<br>'
        for request in self.temp_storage:
            result += 'Polarity: {}<br>'.format(request['polarity'])
            result += 'Text    : {}<br>'.format(request['text'])
            result += '_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _<br>'
        result += '=============================================================================<br>'
        return(result)
    

    def add_new_record(self, text, polarity):
        self.request_count += 1
        new_record = {'text': text, 'polarity': polarity}
        if len(self.temp_storage) == self.storage_max_length:
            del self.temp_storage[0]
        self.temp_storage.append(new_record)