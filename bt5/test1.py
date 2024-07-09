  if b < 2:
            return False
        elif b == 2:
            return True
        elif b % 2 == 0:
            return False
        else:
            for d in range(3, 1 + math.floor(math.sqrt(b)), 2):
                if b % d == 0:
                    return False
            return True



39.12745714187622 giây
    