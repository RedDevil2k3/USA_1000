filenames = ['USA100.csv', 'USA200.csv', 'USA300.csv', 'USA400.csv', 'USA500.csv', 'USA600.csv', 'USA700.csv', 'USA800.csv', 'USA900.csv', 'USA1000.csv']
with open('complete_urls.csv', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write("%s" % line)
