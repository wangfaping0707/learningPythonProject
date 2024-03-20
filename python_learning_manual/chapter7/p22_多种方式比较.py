template = '%(motto)s,%(pork)s and %(food)s' % {'motto': 'I', 'pork': 'love', 'food': 'world'}
print('template:', template)

template1 = '%(motto)s,%(pork)s and %(food)s' % dict(motto='I', pork='love', food='world')
print('template1:', template1)

template2 = '{motto},{pork} and {food}'.format(motto='I', pork='love', food='world')
print('template2:', template2)

