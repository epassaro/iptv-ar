#!/usr/bin/env bash

import os
from collections import OrderedDict

import youtube_dl
import m3u8

channels = OrderedDict({"Televisión Pública": "https://www.youtube.com/user/TVPublicaArgentina",
                        "Telefe Córdoba": "https://www.youtube.com/channel/UC3OQ66wEJaOPHK25IBdWR_g",
                        "Telefe Rosario": "https://www.youtube.com/channel/UCPr0HEFKN8wtDIfcPsVB10Q",
                        #"Telefe Salta": "https://www.youtube.com/channel/UCy-r-BQ5BQRU6rzGS73-WBQ",
                        #"Todo Noticias": "https://www.youtube.com/c/todonoticias",
                        #"A24": "https://www.youtube.com/c/A24com",
                        #"C5N": "https://www.youtube.com/user/c5n",
                        #"La Nación+": "https://www.youtube.com/c/LaNacionMas",
                        #"Crónica HD": "https://www.youtube.com/c/cronicatv",
                        #"Canal 26": "https://www.youtube.com/c/canal26",
                        #"DeporTV": "https://www.youtube.com/c/canaldeportv",
                        #"KZO": "https://www.youtube.com/c/CanalKZO",
                        #"RTVE Noticias": "https://www.youtube.com/c/rtvenoticias",
                        #"FRANCE 24": "https://www.youtube.com/c/FRANCE24Espa%C3%B1ol",
                        #"DW": "https://www.youtube.com/c/dwespanol",
                        #"Euronews": "https://www.youtube.com/c/euronewses",
                        #"Vorterix": "https://www.youtube.com/c/VorterixOficial",
                        ##"Urbana Play 104.3 FM": "https://www.youtube.com/c/UrbanaPlay1043FM",
                        #"El Destape Radio": "https://www.youtube.com/channel/UCgOvQwLB387CWMrseINhyCg",
                        #"La 100": "https://www.youtube.com/c/La100",
                        #"POP Radio": "https://www.youtube.com/c/popradio1015",
                        })

ydl_opts = {"format": "best[height=720]",
            "skip_download": True,
            "forceurl": True,
            "quiet": False}

playlist = m3u8.M3U8()
for channel, url in channels.items():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:

        try:
            info = ydl.extract_info(f"{url}/live")

        except:
            print(f"Oops! Something went wrong with {channel}")
            continue

    playlist.add_playlist(f"#EXTINF:-1,{channel}\n{info['url']}")

os.makedirs("_build", exist_ok=True)
playlist.dump("_build/live.m3u")
