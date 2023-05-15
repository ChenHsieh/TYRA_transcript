# WIP: This script is a work in progress. It is not yet ready for use.

import pandas as pd 

videos = pd.read_csv('./scripts/video_list.csv', sep=";")

for video_title,url in zip(videos['video_title'], videos['url']):
    with open("./_posts/2023-04-26-{}.md".format(video_title.replace(" ", "-")), "w") as f:
        f.write("---\n")
        f.write("layout: post\n")
        f.write('title: "{}"\n'.format(video_title))
        f.write('date: 2023-04-26 00:00:00 -0000\n')
        f.write('categories: Spring2023\n')
        f.write('---\n')
        f.write('\n')
        embed_url = url.replace("watch?v=", "embed/")
        f.write(f'<iframe width="560" height="315" src="{embed_url}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>')
        f.write('\n\n')
        # read the tsv file in out with the same name as the video title
        transcripts = pd.read_csv(f'./out/{video_title}.tsv', sep="\t")
        # write the contents of the tsv file to the markdown file
        f.write(f"## Transcript\n\n")
        
        for sn,info in transcripts.iterrows():

            time_string = '{:02d}:{:02d}:{:06.3f}'.format((info['start'] // 3600000) % 24, (info['start'] // 60000) % 60, (info['start'] % 60000) / 1000)
            f.write(f"[{time_string}]({url}&t={int(info['start']/1000)})\t{info['text']}")
            f.write('\n\n')

