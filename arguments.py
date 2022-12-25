import argparse


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--tok", default="gogamza/kobart-base-v2", type=str)
    parser.add_argument("--data-path", default="한국어 대화", type=str,
                        help="ONLY DIRNAME")
    parser.add_argument("--mode", choices=["all", "make", "sample"], type=str)

    return parser.parse_args()
