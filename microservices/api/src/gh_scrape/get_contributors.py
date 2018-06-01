from src.db.contributor_table import add_contributor
from src.db.contributor_table import get_contributors_list as getcon
from src.utils.login import login
import requests
import os

def get_full_name(username):
    url = "https://api.github.com/users/"+username
    fullname = requests.get(url).json()['name']
    return str(fullname)

def get_contributors(org_name,project_name):
    # https://api.github.com/repos/KRSSG/robocup-stp/contributors?page=1

    all_contributors = list()
    page_count = 1
    while True:
        contributors = requests.get("https://api.github.com/repos/"+org_name+'/'+project_name+"/contributors?page=%d"%page_count)
        if contributors != None and contributors.status_code == 200 and len(contributors.json()) > 0:
            all_contributors = all_contributors + contributors.json()
            # print(page_count)
        else:
            # print("breaking")
            break
        page_count = page_count + 1
    all_contributors = list(map(lambda x: x['login'],all_contributors))
    return all_contributors


def get_contributors_list(org_name, project_name):
    print(org_name,project_name)
    contributors_username = get_contributors(org_name, project_name) 
    contributors_list = []
    for username in contributors_username:
        fullname = get_full_name(username)
        contributors_list.append([str(username),str(fullname)])
    print(contributors_list)

    return contributors_list
    return [['mulx10',"Mehul Kumar Nirala"],['parulagg27',"Parul Aggarwal"]]
    
def main(org_name,project_name):
    contributors = get_contributors_list(org_name,project_name)
    add_contributor(headers=headers,org_name=org_name,project_name=project_name,contributors=contributors)
    print(getcon(headers=headers,org_name=org_name,project_name=project_name))
    
if __name__ == '__main__':
    # print(get_full_name('mulx10'))
    org_name = 'KRSSG'
    project_name = 'robocup-stp'
    
    headers = login('mehul','mehul@hasura') 
    main(org_name,project_name)

    

    # contributors = get_contributors_list('KRSSG','robocup')
    # add_contributor(headers=headers,org_name='KRSSG',project_name='robocup',contributors=contributors)
    # print(getcon(headers=headers,org_name='KRSSG',project_name='robocup-stp'))
    # print(get_contributors('KRSSG','robocup-stp'))
    # print (get_contributors_list('KRSSG','robocup-stp'))