## your favourite indexed enumerator

def enum(*sequential, **named):
    enumerator = dict(zip(sequential, range(len(sequential))), **named)
    return type('enumerator', (), enumerator)

