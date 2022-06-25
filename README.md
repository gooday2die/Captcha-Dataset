# Captcha-Dataset
Captcha-Dataset is a dataset that has images and sounds of English alphabets (A-Z) and numbers (0-9) stored in each directory.

## Motivation
Looked for a captcha dataset however was not able to find one. So I am making a dataset for future use. Since I do not want any more developers wasting their time with datset, I am making this repository open.

## How It Works - Images
### Example
![Example Captcha](https://raw.githubusercontent.com/gooday2die/Captcha-Dataset/main/github/pics/1.png)
This example captcha will be divided and classified into 5 different letters.

|Letter|Image|Stored In|
|--|--|--|
|4|![4](https://raw.githubusercontent.com/gooday2die/Captcha-Dataset/main/github/pics/s_1.png)|`/data/images/training_data/4`|
|9|![9](https://raw.githubusercontent.com/gooday2die/Captcha-Dataset/main/github/pics/s_2.png)|`/data/images/training_data/9`| 
|5|![5](https://raw.githubusercontent.com/gooday2die/Captcha-Dataset/main/github/pics/s_3.png)|`/data/images/training_data/5`|
|A|![A](https://raw.githubusercontent.com/gooday2die/Captcha-Dataset/main/github/pics/s_4.png)|`/data/images/training_data/A`|
|S|![S](https://raw.githubusercontent.com/gooday2die/Captcha-Dataset/main/github/pics/s_5.png)|`/data/images/training_data/S`|

## How It Works - Sounds
Some catpchas offer listening sound instead of reading the symbols. in directory `/data/sounds/` there is a `csv` file that was exported by [LabelStudio](https://labelstud.io/).  The `csv` file includes all timelines and labels sorted out so that it can be imported by `pandas` or some other libraries. 

## Info
1. Currently has 1000 alphabet letters and numbers for each sound and images.
2. This dataset uses [labelImg](https://github.com/tzutalin/labelImg) to label each images. 
3. This dataset uses [LabelStudio](https://labelstud.io) to label each sounds.
4. After the labeling process is done, `/tool/split_files.py` is used to split each letter and number images into its directory.

## Projects using this dataset
- [Anti-Captcha-Sound](https://github.com/gooday2die/Anti-Captcha-Sound) by Gooday2die

## PRs and Issues
If you found any mislabeling or incorrect classification, please PR or report issue.

## Contribution
If you have more captcha data and would like to share your dataset, please PR so that other people can get help from this repository

## License
- MIT License
- Citation: Isu Kim. Captcha-Dataset. Git code (2022). [https://github.com/gooday2die/Captcha-Dataset](https://github.com/gooday2die/Captcha-Dataset)
