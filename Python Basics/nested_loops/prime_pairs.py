ab_start = int(input())
cd_start = int(input())
ab_range = int(input())
cd_range = int(input())
ab_end = ab_start + ab_range
cd_end = cd_start + cd_range

for ab in range(ab_start, ab_end + 1):
    ab_is_prime = True
    for range_ab in range(2, ab):
        if ab % range_ab == 0:
            ab_is_prime = False
            break
    for cd in range(cd_start, cd_end + 1):
        cd_is_prime = True
        for range_cd in range(2, cd):
            if cd % range_cd == 0:
                cd_is_prime = False
                break
        if ab_is_prime and cd_is_prime:
            print(f'{ab}{cd}')