from dateutil.parser import parse


class DateConverter:
    regex = '[0-9]{4}-?[0-9]{2}-?[0-9]{2}'

    def to_python(self, value):
        return parse(value).date()

    def to_url(self, value):
        return value
