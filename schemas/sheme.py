import flask_marshmallow as ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email')

