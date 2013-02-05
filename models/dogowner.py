# coding: utf8

db.define_table('t_owner',
    Field('f_name', type='string', label=T('Name')),
    format='%(f_name)s',
    singular='Owner', plural='Owners',
    migrate=True)
          
db.define_table('t_dog',
    Field('f_name', type='string', label=T('Name')),
    Field('f_owner', type='reference t_owner', label=T('theOwner')),
    format='%(f_name)s',
    singular='Dog', plural='Dogs',
    migrate=True)
