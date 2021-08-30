# -*- coding:utf-8 -*-
import requests
import random


class PixGreat:
    """PixGreat API"""
    def __init__(self, tag: str, use_mirror: bool = False):
        """
        :param tag: Which kind of pictures do you want
        :param use_mirror: If use the Gitee mirror source
        """
        self.tag = tag
        # The default API links
        self.index = f'https://raw.githubusercontent.com/WhitePaper233/PixGreat/main/indexs/%23{self.tag}.json'
        self.database = 'https://raw.githubusercontent.com/WhitePaper233/PixGreat/main/database/{}.json'
        if use_mirror:
            # The mirror API links
            self.index = f'https://gitee.com/whitepaper233/PixGreat/raw/main/indexs/%23{self.tag}.json'
            self.database = 'https://gitee.com/whitepaper233/PixGreat/raw/main/database/{}.json'

    def get(self) -> dict:
        """Get a random picture's data from the PixGreat API repo"""
        # Get index
        with requests.get(self.index) as r:
            index = r.json()
            # Randomly pick a picture
            illust_id_list = list(index.keys())
            pix_great_id = illust_id_list[random.randint(0, (len(illust_id_list) - 1))]

        # Get picture data
        with requests.get(self.database.format(pix_great_id)) as r:
            return r.json()
