project=int(input('Enter the project score:'))
external=int(input('Enter external score:'))
internal=int(input('Enter internal score:'))
if project >=50 and internal >=50 and external>=50:
    total=((70*project)+(10*internal)+(20*external))/100
    print('total score is :',total)
    if total >=90:
        print('A grade')
    elif total >80:
        print('B grade')
    else:
        print('C grade')
else:
    if project < 50:
        print('failed in project and  score is', project)
    if external < 50:
        print('failed in external and  score is ', external)
    if internal < 50:
        print('failed in and internal score is', internal)