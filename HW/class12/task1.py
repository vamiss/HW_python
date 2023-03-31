def create_triangle(l1, l2, l3):
    print(f'{False if l1 >= l2 + l3 or l2 >= l1 + l3 or l3 >= l1 + l2 else True}')

create_triangle(l1 = int(input()), l2 = int(input()), l3 = int(input()))