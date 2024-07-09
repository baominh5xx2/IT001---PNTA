def quadratic_probing_hash(m, a, b, keys):
    table = [None] * m
    
    def probe(k, i):
        return ((k % m) + a * i + b * i * i) % m
    
    for key in keys:
        inserted = False
        for i in range(m):
            pos = probe(key, i)
            if table[pos] is None:
                table[pos] = key
                inserted = True
                break
    
    return table

def process_input():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    i = 0
    results = []
    while i < len(data):
        line = data[i].strip()
        if line == '0':
            break
        
        m, a, b = map(int, line.split())
        i += 1
        keys = list(map(int, data[i].strip().split()))
        
        table = quadratic_probing_hash(m, a, b, keys)
        results.append(table)
        
        i += 1
    
    for table in results:
        print(', '.join(str(x) if x is not None else 'None' for x in table))

if __name__ == "__main__":
    process_input()
