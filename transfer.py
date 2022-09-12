with open('C:/Users/18251/Desktop/a/pictor_ppe_crowdsourced_approach-01_test.txt', 'r', encoding='utf-8') as f1:
    for item in f1:
        name = item.split('\t')[0].replace('.jpg', '.txt')
        with open('C:/Users/18251/Desktop/a'+'/'+name, 'w', encoding='utf-8') as f2:
            f2.write(item.replace(item.split('\t')[0] + '\t', ''))
