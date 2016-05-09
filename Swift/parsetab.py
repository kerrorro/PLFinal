
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '8E7EADB517FE2DCF08C657C5B5506662'
    
_lr_action_items = {'FALSE':([0,2,4,5,6,7,8,13,14,15,16,17,19,20,21,22,24,26,],[5,-21,-17,-20,-14,-16,-15,-19,5,-4,5,-10,5,-11,-9,-12,-13,-5,]),'NIL':([0,2,4,5,6,7,8,13,14,15,16,17,19,20,21,22,24,26,],[2,-21,-17,-20,-14,-16,-15,-19,2,-4,2,-10,2,-11,-9,-12,-13,-5,]),'QUOTE':([0,2,4,5,6,7,8,13,14,15,16,17,19,20,21,22,24,26,],[9,-21,-17,-20,-14,-16,-15,-19,9,-4,9,-10,9,-11,-9,-12,-13,-5,]),'SIMB':([0,1,2,4,5,6,7,8,13,14,15,16,17,19,20,21,22,24,26,],[6,14,-21,-17,-20,-14,-16,-15,-19,6,-4,6,-10,6,-11,-9,-12,-13,-5,]),'NUM':([0,2,4,5,6,7,8,13,14,15,16,17,19,20,21,22,24,26,],[7,-21,-17,-20,-14,-16,-15,-19,7,-4,7,-10,7,-11,-9,-12,-13,-5,]),'LPAREN':([0,2,4,5,6,7,8,9,13,14,15,16,17,19,20,21,22,24,26,],[1,-21,-17,-20,-14,-16,-15,16,-19,1,-4,1,-10,1,-11,-9,-12,-13,-5,]),'TEXT':([0,2,4,5,6,7,8,13,14,15,16,17,19,20,21,22,24,26,],[4,-21,-17,-20,-14,-16,-15,-19,4,-4,4,-10,4,-11,-9,-12,-13,-5,]),'RPAREN':([2,4,5,6,7,8,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-21,-17,-20,-14,-16,-15,-19,-8,-4,-8,-10,24,-8,-11,-9,-7,26,-13,-6,-5,]),'TRUE':([0,2,4,5,6,7,8,13,14,15,16,17,19,20,21,22,24,26,],[13,-21,-17,-20,-14,-16,-15,-19,13,-4,13,-10,13,-11,-9,-12,-13,-5,]),'$end':([0,2,3,4,5,6,7,8,10,11,12,13,15,24,26,],[-18,-21,-2,-17,-20,-14,-16,-15,0,-1,-3,-19,-4,-13,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'quoted_list':([0,14,16,19,],[3,17,17,17,]),'items':([14,16,19,],[18,23,25,]),'list':([9,],[15,]),'item':([14,16,19,],[19,19,19,]),'bool':([0,14,16,19,],[8,8,8,8,]),'exp':([0,],[10,]),'atom':([0,14,16,19,],[11,21,21,21,]),'call':([0,14,16,19,],[12,20,20,20,]),'empty':([14,16,19,],[22,22,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('exp -> atom','exp',1,'p_exp_atom','yacc.py',11),
  ('exp -> quoted_list','exp',1,'p_exp_qlist','yacc.py',15),
  ('exp -> call','exp',1,'p_exp_call','yacc.py',19),
  ('quoted_list -> QUOTE list','quoted_list',2,'p_quoted_list','yacc.py',23),
  ('list -> LPAREN items RPAREN','list',3,'p_list','yacc.py',27),
  ('items -> item items','items',2,'p_items','yacc.py',31),
  ('items -> empty','items',1,'p_items_empty','yacc.py',35),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',39),
  ('item -> atom','item',1,'p_item_atom','yacc.py',43),
  ('item -> quoted_list','item',1,'p_item_list','yacc.py',51),
  ('item -> call','item',1,'p_item_call','yacc.py',55),
  ('item -> empty','item',1,'p_item_empty','yacc.py',59),
  ('call -> LPAREN SIMB items RPAREN','call',4,'p_call','yacc.py',63),
  ('atom -> SIMB','atom',1,'p_atom_simbol','yacc.py',70),
  ('atom -> bool','atom',1,'p_atom_bool','yacc.py',74),
  ('atom -> NUM','atom',1,'p_atom_num','yacc.py',78),
  ('atom -> TEXT','atom',1,'p_atom_word','yacc.py',82),
  ('atom -> <empty>','atom',0,'p_atom_empty','yacc.py',86),
  ('bool -> TRUE','bool',1,'p_bool','yacc.py',90),
  ('bool -> FALSE','bool',1,'p_bool','yacc.py',91),
  ('atom -> NIL','atom',1,'p_nil','yacc.py',103),
]
