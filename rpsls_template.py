#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ���ľ1������
���ڣ�2020.11.19
"""

import random  #�������ģ��



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name == "ʯͷ":
        number=int(0)
        return number
    elif name == "ʷ����":
        number=int(1)
        return number
    elif name == "ֽ":
        number=int(2)
        return number
    elif name == "����":
        number=int(3)
        return number
    elif name == "����" :
        number=int(4)
        return number
    else : print("Error:No Correct Name.")



def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number == 0:
        name="ʯͷ"
    elif number == 1:
        name="ʷ����"
    elif number == 2:
        name="ֽ"
    elif number == 3:
        name="����"
    else : name="����"
    print("�������ѡ��Ϊ%s"%name)
    return


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    number=name_to_number(player_choice)
    comp_number=random.randint(0,5)
    number_to_name(comp_number)
    if number == 0 and comp_number == 4:   #һһ�оٲ�ͬ���
        print("��Ӯ�ˣ�")
    elif number == 0 and comp_number == 3:
        print("��Ӯ�ˣ�")
    elif number == 1 and comp_number == 4:
        print("��Ӯ�ˣ�")
    elif number == 1 and comp_number == 0:
        print("��Ӯ�ˣ�")
    elif number == 2 and comp_number == 0:
        print("��Ӯ�ˣ�")
    elif number == 2 and comp_number == 2:
        print("��Ӯ�ˣ�")
    elif number == 3 and comp_number == 2:
        print("��Ӯ�ˣ�")
    elif number == 3 and comp_number == 1:
        print("��Ӯ�ˣ�")
    elif number ==4 and comp_number == 2:
        print("��Ӯ�ˣ�")
    elif number == 4 and comp_number == 3:
        print("��Ӯ�ˣ�")
    elif number == comp_number:
        print("���ͼ��������һ����")
    else : print("�����Ӯ��")


    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�




# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
player_choice=input()
rpsls(player_choice)


