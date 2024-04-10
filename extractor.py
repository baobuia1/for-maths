import json
with open('./data.csv') as f:
    data = []
    for x in f:
        dat = x.replace('\n','').replace(';','').split(',')
        try:
            if 0.0 not in [float(dat[1]),float(dat[3]),float(dat[2])]:
                data.append(
                    {
                        dat[0]:[float(dat[1]),float(dat[3]),float(dat[2])]
                    }
                )
            else:
                raise ValueError
        except ValueError:
            print(
                [dat[1],dat[3],dat[2]]
            )

with open('./data.json','w') as f:
    json.dump(data,f)