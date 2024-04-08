import csv
import codecs

#genres parser
def genres_parser(genres):
    res_s = ''
    if len(genres) == 0:
        return res_s
    else:
        s_list = genres.split(',')
        for str_g in s_list:
            if str_g.find(' \"name\": \"') != -1:
                try:
                    buff_st = str_g[10::]
                    end_ch = buff_st.index('\"')
                    res_s += buff_st[0:end_ch] + ' '
                except ValueError:
                    continue
    return res_s


tegs_titles = ['id', 'title', 'tags']

with codecs.open(filename='./data/movies.csv', encoding='utf_8_sig') as f_r:
    reader = csv.DictReader(f_r)
    with codecs.open( filename='./data/tags.csv', mode='w', encoding='utf_8_sig') as f_w:
        writer = csv.writer(f_w)
        writer.writerow(tegs_titles)

        for row in reader:
            try:
                print(row['original_title'])
                id, title = row['id'], row['title']
                tags = genres_parser(row['genres']) + genres_parser(row['keywords'])
                tags += row['overview'] + ' ' + row['tagline']
                print(tags)
                
                writer.writerow([id, title, tags])
            except UnicodeDecodeError:
                print('UnicodeDecodeError cached')

    f_w.close()
f_r.close()