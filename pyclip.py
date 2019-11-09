from clips import Environment,Symbol

env = Environment()

#rule
env.load('rule.clp')

#fact
fact = env.assert_string('(total-point 5)')
fact = env.assert_string('(semua sudut sama)')
#env.assert_string('(semua sudut sama)')

template = fact.template
assert template.implied == True

env.run()