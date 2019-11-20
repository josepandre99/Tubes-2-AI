import clips
import logging
from clips import Environment, Symbol, LoggingRouter

def callRule (rule) :
    listRuleActivated.append(rule)

listFactUsed = []
listRuleActivated = []

#logformat = '%(asctime)s - %(levelname)s - %(message)s'
#logging.basicConfig(level=10, format=logformat)

env = Environment()
#logger = LoggingRouter()
#logger.add_to_environment(env)

env.define_function(callRule)

#rule
env.load('rule.clp')
env.reset()

#fact
env.assert_string('(total-point 3)')
env.assert_string('(sudut utama sama 90)')
#env.assert_string('(is siku)')
env.assert_string('(ada dua sudut sama)')

#for rule in env.rules() :
#    rule.watch_firings = True

#for rule in env.activations() :
#    print(rule.name)

env.run()

for f in env.facts() :
    listFactUsed.append(f)

#for ag in clips.agenda.Agenda.activations(env) :
#    listRuleActivated.append(ag)

#for fact in listFactUsed :
#    print(fact)

#for rule in listRuleActivated :
#    print(rule)
