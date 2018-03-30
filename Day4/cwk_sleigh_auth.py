class Sleigh(object):
    def authenticate(self, name, password):
        return True if name == 'Santa Claus' and password == 'Ho Ho Ho!' else False


sleigh = Sleigh()
print(sleigh.authenticate('Santa Claus', 'Ho Ho Ho!'))
print(sleigh.authenticate('Santa Claus', 'Ho Ho!'))
print(sleigh.authenticate('S Claus', 'Ho Ho Ho!'))
print(sleigh.authenticate('Santa', 'Ho Ho Ho!'))


# best practice
class Sleigh(object):
    def authenticate(self, name, password):
        return name == 'Santa Claus' and password == 'Ho Ho Ho!'