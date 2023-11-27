rmdir /s /q ..\out\test
python scripts/amg.py --checkpoint ..\checkpoints\sam_vit_l_0b3195.pth --model-type vit_l --input ../imgs/test2017/000000000180.jpg --output ../out/test

rem python scripts\maskToImage.py --baseDir ..\out\test --fileName Screenshot_2023.11.09_10.27.36.101