class ErrorBubbling:
    def __init__(self):
        self.error_list = []

    def insert_error(self, error):
        self.error_list.insert(0, error)

    def clear_error_list(self):
        self.error_list.clear()

    def get_error_list(self):
        return self.error_list
