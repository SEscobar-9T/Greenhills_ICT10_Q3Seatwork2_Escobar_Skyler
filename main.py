from pyscript import display, document

def register_select(e):
    document.getElementById('output').innerHTML = " "

    register_confirm = int(document.querySelector('input[name="online_reg"]:checked').value)
    medclear_confirm = int(document.querySelector('input[name="med_cert"]:checked').value)
    section_confirm = int(document.querySelector('input[name="Grade"]:checked').value)
    level_confirm = int(document.querySelector('input[name="Section"]:checked').value)

    if register_confirm == 1 and medclear_confirm == 3 and section_confirm == 11 and (level_confirm == 7 and level_confirm == 8 and level_confirm == 9 and level_confirm == 10):
        display(f'You have been qualified, your team is Green Hornets!', target='output')
    elif register_confirm == 1 and medclear_confirm == 3 and section_confirm == 12 and (level_confirm == 7 and level_confirm == 8 and level_confirm == 9 and level_confirm == 10):
        display(f'You have been qualified, your team is Red Bulldogs!', target='output')
    elif register_confirm == 1 and medclear_confirm == 3 and section_confirm == 13 and (level_confirm == 7 and level_confirm == 8 and level_confirm == 9 and level_confirm == 10):
        display(f'You have been qualified, your team is Blue Bears!', target='output')
    elif register_confirm == 1 and medclear_confirm == 3 and section_confirm == 14 and (level_confirm == 7 and level_confirm == 8 and level_confirm == 9 and level_confirm == 10):
        display(f'You have been qualified, your team is Yellow Tigers!', target='output')
    elif register_confirm == 1 and medclear_confirm == 4:
        display(f'Please ensure that you have been given clearance by the school clinic before registering.', target='output')
    elif register_confirm == 2 and medclear_confirm == 3:
        display(f'Please accomplish the online registration form before signing up.', target='output')
    elif register_confirm == 2 and medclear_confirm == 4:
        display(f'Please make sure you have these requirements before signing up.', target='output') 
    else:
        display(f'Please complete the form before checking your team.', target='output')
