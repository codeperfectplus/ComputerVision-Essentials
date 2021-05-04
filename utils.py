from google_drive_downloader import GoogleDriveDownloader as gdd

download_dict = {
    "16gAKScYAW0bZkyRgcLF71x28du_mLY8-": "assets/res10_300x300_ssd_iter_140000.caffemodel",
    "1jUIwxXjxz8oC7I2Ta9vtiozsB4i95043": "Media/people-walking.mp4",
    "1Q7qfr11olEFguRRkKRnC1Yah3ZnJCUnM": "assets/mask_rcnn_coco.h5"
}

for file_id, dest_path in download_dict.items():

    gdd.download_file_from_google_drive(file_id=file_id,
                                        dest_path=dest_path,
                                        unzip=True)
