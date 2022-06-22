# Captcha-Dataset
Captcha-Dataset is a dataset that has images of English alphabets (A-Z) and numbers (0-9) stored in each directory.
## Motivation
Looked for a captcha dataset however was not able to find one. So I am making a dataset for future use. Since I do not want any more developers wasting their time with datset, I am making this repository open.
## How It Works
### Example
![Example Captcha](https://raw.githubusercontent.com/gooday2die/Captcha-Dataset/main/github/pics/1.png)
This example captcha will be divided and classified into 5 different letters.

|Letter|Image|Stored In|
|--|--|--|
|4|![4](https://raw.githubusercontent.com/gooday2die/Captcha-Dataset/main/github/pics/s_1.png)|`/training_data/4`|
|9|![9](https://raw.githubusercontent.com/gooday2die/Captcha-Dataset/main/github/pics/s_2.png)|`/training_data/9`| 
|5|![5](https://raw.githubusercontent.com/gooday2die/Captcha-Dataset/main/github/pics/s_3.png)|`/training_data/5`|
|A|![A](https://raw.githubusercontent.com/gooday2die/Captcha-Dataset/main/github/pics/s_4.png)|`/training_data/A`|
|S|![S](https://raw.githubusercontent.com/gooday2die/Captcha-Dataset/main/github/pics/s_5.png)|`/training_data/S`|

## Info
1. Currently has 200 alphabet letters and numbers.
2. This dataset uses [https://github.com/tzutalin/labelImg](labelImg) to label each images. 
3. After the labeling process is done, `/tool/split_files.py` is used to split each letter and number images into its directory.

## PRs and Issues
If you found any mislabeling or incorrect classification, please PR or report issue.

## License
- MIT License
- Citation: Isu Kim. Captcha-Dataset. Git code (2022). [https://github.com/gooday2die/Captcha-Dataset](https://github.com/gooday2die/Captcha-Dataset)