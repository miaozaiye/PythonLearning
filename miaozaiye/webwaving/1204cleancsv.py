import sys



def clean_group(fh):
    '''


    :param fh:
    :return: List of dics, dic = {name,mailbox,reg_time,Log_time,file_count}
    '''

    group = []

    return group

def loyal_group(group):
    '''

    :param group:
    :return: group of file_count > 10
    '''
    loyalgroup = []
    return loyalgroup

def last_login(group,period = 'w'):
    '''

    :param group:
    :param period:
    :return: last_login group in asked period.
    '''


    if period == 'w':

        group = []
    elif period == 'm':
        group = []

    return group

def find_duplicate(group1,group2):
    '''

    :param group1:
    :param group2:
    :return: group of the duplicated date in group1, and group2
    '''
    group = []
    return group


def main(path):
    fh = open(path,'r')
    group = clean_group(fh)
    loyalgroup = loyal_group(group)
    last_week_group = last_login(group,'w')
    high_potential_group = find_duplicate(loyalgroup,last_week_group)

