import sys
from Play_Experta_Cons import Play_Experta_Cons

engine=Play_Experta_Cons('./Futebol.json.txt')
engine.reset()
engine.run()

del(engine)

sys.exit(0)
