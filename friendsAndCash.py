
def friends(friendsAndCash):
    s = '0$'
    p = 0
    CashAndFriends = {}
    for name, cash in friendsAndCash.items():
        CashAndFriends[cash] = name
        p = p + int(cash.strip('$'))
        if int(s.strip('$')) < int(cash.strip('$')):
            s = cash
            n = name
    print("Total money we have is", p)
    print(n + ' has the most money')
    print(CashAndFriends)
friendsAndCash = {'John': '20$', 'Dan': '35$', 'Lois': '14$', 'Doug': '144$'}
friends(friendsAndCash)