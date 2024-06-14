import flask_marshmallow as ma


class SchemaBase(ma.Schema):
    @classmethod
    def schema_many(cls, arg):
        if len(arg) > 1:
            return cls(many=True).dump(arg)
        else:
            return cls(many=False).dump(arg[0])


class UserSchema(SchemaBase, ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email')
