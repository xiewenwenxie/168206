# ��������Ҫʱ��ʱ
# �տ������ʱ��
def bak(c, t):
    a = int((c-1) / 8)
    t = t + (a+1)*180 + 10
    return t


# �ܻ���ʱ��
def time(c):
    t = 0
    t = bak(c, t)
    return t


# �˿��ڰ�̨ƽ���ȴ�ʱ�䣨ֻ�й˿�����20����Ҫ�ȴ���
def wb(c):
    if c < 21:
        t = 0
    else:
        a = int((c - 1) / 20)
        t = (a * 10)/c
    return t


# �˿����տ��ܵȴ�ʱ��
def ws(c):
    if c < 9:
        t = 0
    else:
        a = int((c - 1) / 8)
        b = int((c - 1) / 20)
        t = (a * 180 - b * 10) / c
    return t


print(time(1))
print(time(8))
print(time(25))
print(time(100))
print(ws(9))


# �������60Sʱ
# ��ȫ���˿ͽ����̨������ϵ�����ʱ��
def cus(c):
    t = (c - 1) * 60 + 10
    return t


# �ܻ���ʱ��
def time(c):
    t = cus(c)+180
    return t
#���������60Sʱ����̨����Ҫ�ȴ����տ������῾����ʳ�Ҳ����Ҫ�ȴ�
print(time(25))


# �������120Sʱ
# ��ȫ���˿ͽ����̨������ϵ�����ʱ��
def cus(c):
    t = (c - 1) * 120 + 10
    return t


def time(c):
    t = cus(c)+180
    return t
#���������60Sʱ����̨����Ҫ�ȴ����տ������῾1.5��ʳ�Ҳ����Ҫ�ȴ�
print(time(100))