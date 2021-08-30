![Banner](https://raw.githubusercontent.com/WhitePaper233/PixGreat/main/Banner.png)

# PixGreat

![BuildWithLove](https://forthebadge.com/images/badges/built-with-love.svg)
![UsesGit](https://forthebadge.com/images/badges/uses-git.svg)
![OpenSource](https://forthebadge.com/images/badges/open-source.svg)
![MakesPeopleSmile](https://forthebadge.com/images/badges/makes-people-smile.svg)

![License](https://img.shields.io/github/license/WhitePaper233/PixGreat?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/WhitePaper233/PixGreat?style=for-the-badge)
![CollectionQuantity](https://img.shields.io/badge/Collection%20Quantity-43-66ccff?style=for-the-badge)
![GiteeMirrorSyncingStatus](https://img.shields.io/github/workflow/status/WhitePaper233/PixGreat/GitHub%20Actions%20Mirror?label=Gitee%20Mirror%20Sync&style=for-the-badge)

A carefully chosen pixiv picture API repo.



## Usage

1. Get index from this link `https://raw.githubusercontent.com/WhitePaper233/PixGreat/main/indexs/%23<Tag>.json`

   You can retrieve all available tags [here](https://github.com/WhitePaper233/PixGreat/tree/main/indexs)

2. Use the random function in your programming language to select a Pixiv illust ID randomly

   This is the json format you will get:

   ```json
   {
       "Pixiv illust ID 1": ["PixGreatID"],
   	"Pixiv illust ID 2": ["PixGreatID 1", "PixGreatID 2"]
   }
   ```

   

3. Randomly select a picture from the alternative list, and recorded it as PixGreatID

4. Get detailed information from this link: `https://raw.githubusercontent.com/WhitePaper233/PixGreat/main/database/<PixGreatID>.json`

### Mirror

If you are in China or other places where you can't visit GitHub stably, here is a mirror in China  that you can try.

#### Mirror Usage

1. Check the [Usage](#Usage)
2. Replace  `https://raw.githubusercontent.com/WhitePaper233/PixGreat/main/indexs/%23<Tag>.json`  to `https://gitee.com/whitepaper233/PixGreat/raw/main/indexs/%23<Tag>.json`
3. Replace `https://raw.githubusercontent.com/WhitePaper233/PixGreat/main/database/<PixGreatID>.json` to `https://gitee.com/whitepaper233/PixGreat/raw/main/database/<PixGreatID>.json`

**Note: DO NOT TRY TO PR IN MIRROR REPO.IT WILL BE CLOSED.**



## Example

Here is an example usage in Python. You can just download the codes in the example folder and add them to your codes

`Python:`

```python
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

```

You can also PR libraries that available in other languages, and any high-quality code is welcome



## Pull Request

**Note: any PR that does not meet the PR requirements will be closed**

