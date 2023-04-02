from django.core.serializers.json import DjangoJSONEncoder


class JSONEncoder(DjangoJSONEncoder):
    def default(self, o):
        try:
            return o.dict()
        except AttributeError:
            pass
        return super().default(o)