import cv2  # type: ignore
import argparse
import os
import json
import csv

parser = argparse.ArgumentParser(
    description=(
        "get image from mask . Requires open-cv "
    )
)


parser.add_argument(
    "--baseDir",
    type=str,
    required=True,
    help=(
        "Path to the directory where original image and masks are"
    ),
)

parser.add_argument(
    "--fileName",
    type=str,
    required=True,
    help=(
        "file name"
    ),
)

def main(args: argparse.Namespace) -> None:
    print("mask to img...")
    #os.makedirs(args.output, exist_ok=True)
    origFileName = os.path.join(args.baseDir, args.fileName+'.png')
    print(origFileName)
    image = cv2.imread(origFileName)
    masksDir = os.path.join(args.baseDir, args.fileName)
    metadataCsvName = os.path.join(masksDir, 'metadata.csv')
    print(metadataCsvName)
    colRow = None
    itms = []

    outdirName = os.path.join(args.baseDir, args.fileName+'.out')
    os.makedirs(outdirName, exist_ok=True)
    with open(metadataCsvName) as csvfile:
        csvRdr = csv.reader(csvfile, delimiter=',')
        for row in csvRdr:
            itm = {}
            if colRow is None:
                colRow = row
            else:
                for col, dta in zip(colRow, row):
                    #print(col+':'+dta)
                    itm[col] = dta
        
                itms.append(itm)
            #print(itm)
    print(itms)

    for itm in itms:        
        print('id='+itm["id"])
        print(itm)
        #bbox_x0': '740', 'bbox_y0': '76', 'bbox_w': '22', 'bbox_h
        maskFileName = os.path.join(masksDir, itm["id"]+'.png')
        print(maskFileName)
        maskFile = cv2.imread(maskFileName)
        x = int(itm["bbox_x0"])
        w = int(itm["bbox_w"])
        y = int(itm["bbox_y0"])
        h = int(itm["bbox_h"])
        crop = image[y: y+h, x: x+w]
        cv2.imwrite(os.path.join(outdirName, itm["id"]+'.png'), crop)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)